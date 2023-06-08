from bottle import post, request, response
import x


@post("/api-follow")
def _():
    try:
        db = x.db()

        cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)

        follower_id = cookie_user['user_id']
        print(follower_id)

        followee_id = request.forms.get("user_followee_id")
        print(followee_id)

        followed = db.execute("INSERT INTO followers VALUES(?,?)", (follower_id, followee_id))
        if not followed:raise Exception("user not followed")
        db.commit()

        return {"info":"user followed", "followee_id":followee_id, "follower_id":follower_id}
    except Exception as e:
        print(e) #is made so we can see the exception in the terminal
    finally:
        if "db" in locals(): db.close()

