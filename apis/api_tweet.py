from bottle import post, request, response
import x
import uuid
import time


############################## FRA ORANGE
# @post("/api-tweet")
# def _():
#     try:
#         user = x.validate_user_logged()
#         x.validate_tweet_message()
#         tweet_id = str(uuid.uuid4()).replace("-", "")
#         db = x.db()
#         # db.execute("INSERT INTO usersx VALUES(?,?)")
#         db.execute("INSERT INTO users VALUES(?,?)")
#         return {"info":"tweet created", "tweet_id":tweet_id}
#     except Exception as e:
#         print(e)
#         try: # Controlled exception, usually comming from the x file
#             response.status = e.args[0]
#             return {"info":e.args[1]}
#         except: # Something unknown went wrong
#             response.status = 500
#             return {"info":str(e)}
#     finally:
#         print("closing db")
#         if "db" in locals(): db.close()


############################## TIDLIGERE API_TWEET

# 'post' is the same as 'create'
# ? = placeholder - the only way you should talk to the database = safety. It is to prevend sequal invention
@post("/tweet")
def _():
  try: # SUCCESS
    x.validate_tweet()
    cookie = request.get_user("user", secret=x.COOKIE_SECRET)
    user = request.get_cookie("user", secret=x.COOKIE_SECRET)
    if not user: print("User not found")
    print(user)
    db = x.db()
    # .hex removes the dashes
    tweet_id = str(uuid.uuid4().hex)
    tweet_message = request.forms.get("message")
    tweet_image = request.forms.get("image")
    # SELECT user_name, user_image, user_first_name, user_last_name FROM users WHERE user_id = tweet_user_fk
    tweet_created_at = int(time.time())
    tweet_user_fk = cookie['user_id']
    tweet_total_messages = "0"
    tweet_total_retweets = "0"
    tweet_total_likes = "0"
    tweet_total_dislikes = "0"
    db.execute("INSERT INTO tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (tweet_id, tweet_message, tweet_image, tweet_created_at, tweet_user_fk, tweet_total_messages, tweet_total_retweets, tweet_total_likes, tweet_total_dislikes))
    db.commit()
    return {"info":"ok", "tweet_id":tweet_id, "user": user}
  except Exception as ex: # SOMETHING IS WRONG
    response.status = 400
    return {"info":str(ex)}
  finally: # This will always take place
    if "db" in locals(): db.close()
