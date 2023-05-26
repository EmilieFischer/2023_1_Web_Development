from bottle import get, template, response, request
import x


#########################
@get("/verification/<user_verification_key>")
def _(user_verification_key):
    cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)

    try:
        db = x.db()
        user = db.execute("SELECT * FROM users WHERE user_verification_key = ?",(user_verification_key, )).fetchone()
        user_verified = db.execute("UPDATE users SET user_verified_at = '1' WHERE user_verification_key=?", (user_verification_key,)).fetchone()
        print(user)
       
        tweets = db.execute("SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id ORDER BY tweet_created_at DESC LIMIT 10").fetchall()
        print (tweets)
        trends = db.execute("SELECT * FROM trends").fetchall()
        users = db.execute("SELECT * FROM users").fetchall()
        db.commit()
        return template("index", trends=trends, tweets=tweets, users=users, cookie_user=cookie_user, cookie_admin=False, tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN)
    except Exception as e:
            response.status = 400
            return {"info":str(e)}
    finally:
        if 'db' in locals(): db.close()

