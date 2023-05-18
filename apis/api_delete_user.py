from bottle import get, template, response, request
import traceback
import x


@get("/delete-user/<user_id>")
def _(user_id):
    print(user_id)
    cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)

    try:
        db = x.db()
        # user_id = request.forms.get("user_id")
        # print("user_id")
        user = db.execute("SELECT * FROM users WHERE user_id = ?",(user_id, )).fetchone()
        if not user: raise Exception ("invalid user id")
        user_deactivated = db.execute("UPDATE users SET user_verified_at = '0' WHERE user_id=?", (user_id,)).rowcount
        if user_deactivated == 0:
             raise Exception ("user not deactivated")
        # Hent alt om brugeren
        tweets = db.execute("SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id ORDER BY tweet_created_at DESC LIMIT 10").fetchall()
        print (tweets)
        trends = db.execute("SELECT * FROM trends").fetchall()
        users = db.execute("SELECT * FROM users").fetchall()
        db.commit()
        return template("index", trends=trends, tweets=tweets, users=users, cookie_user=cookie_user, tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN)
    except Exception as e:
            traceback.print_exc()
            response.status = 400
            return {"info":str(e)}
    finally:
        if 'db' in locals(): db.close()

