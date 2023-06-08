from bottle import post, request
import x

@post("/api-unfollow")
def _():
    try:
        db = x.db()
        db.row_factory = x.dict_factory

        cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)

        follower_id = cookie_user['user_id']
        print(follower_id)

        followee_id = request.forms.get("user_followee_id")
        print(followee_id)

        unfollowed = db.execute("DELETE FROM followers WHERE follower_fk = ? AND followee_fk =?", (follower_id, followee_id)).rowcount
        if not unfollowed:raise Exception("user not unfollowed")
        db.commit()

        return {"info":"user unfollowed", "followee_id":followee_id, "follower_id":follower_id}
    except Exception as e:
        print(e)
    finally:
        if "db" in locals(): db.close()
