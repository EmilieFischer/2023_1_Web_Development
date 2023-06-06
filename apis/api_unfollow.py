from bottle import post, request, response
import x

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################

# post = creating something in the system (what is really says). I know that it is a post because we want to insert something in the database. Also we have a form that is a post
@post("/api-unfollow")
def _():
    try:
        db = x.db()
        db.row_factory = dict_factory

        # TODO: get user from cookie
        cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)

        follower_id = cookie_user['user_id']
        print(follower_id)

        # TODO: get user id from the user from the cookie 
        followee_id = request.forms.get("user_followee_id")
        print(followee_id)

        # TODO: put values into table
        unfollowed = db.execute("DELETE FROM followers WHERE follower_fk = ? AND followee_fk =?", (follower_id, followee_id)).rowcount
        if not unfollowed:raise Exception("user not unfollowed")
        db.commit()

        return {"info":"user unfollowed", "followee_id":followee_id, "follower_id":follower_id}
    except Exception as e:
        print(e) #is made so we can see the exception in the terminal
    finally:
        if "db" in locals(): db.close()
