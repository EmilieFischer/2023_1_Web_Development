from bottle import post, request, response
import x
import uuid
import time

# 'post' is the same as 'create'
# ? = placeholder - the only way you should talk to the database = safety. It is to prevend sequal invention
@post("/tweet")
def _():
  try: # SUCCESS
    # x.validate_tweet()
    # cookie = request.get_user("user", secret=x.COOKIE_SECRET)
    user = request.get_cookie("user", secret=x.COOKIE_SECRET)
    if not user: print("User not found")
    db = x.db()
    # .hex removes the dashes
    tweet = {
    "tweet_id" : str(uuid.uuid4().hex),
    "tweet_message" : request.forms.get("message"),
    "tweet_image" : request.forms.get("image"),
    "tweet_created_at" : int(time.time()),
    "tweet_user_fk" : user['user_id'],
    "tweet_total_messages" : "0",
    "tweet_total_retweets" : "0",
    "tweet_total_likes" : "0",
    "tweet_total_dislikes" : "0"
    }

    values = ""
    for key in tweet:
      values = values + f":{key},"
    values = values.rstrip(",")

    db.execute(f"INSERT INTO tweets VALUES({values})", tweet)
    db.commit()
    return {"info":"ok", "user": user, "tweet":tweet}
  except Exception as ex: # SOMETHING IS WRONG
    response.status = 400
    return {"info":str(ex)}
  finally: # This will always take place
    if "db" in locals(): db.close()
