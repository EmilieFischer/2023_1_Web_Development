from bottle import post, request, response
import x
import uuid
import time
import os
import traceback
import pprint 
import pathlib

# 'post' is the same as 'create'
# ? = placeholder - the only way you should talk to the database = safety. It is to prevend sequal invention
@post("/tweet")
def _():
  try: # SUCCESS
    print("*"*30)
    x.validate_tweet()
    user = request.get_cookie("user", secret=x.COOKIE_SECRET)
    userData = user.copy()
    del userData["user_password"]
    pprint.pprint(userData)
    if not user: print("User not found")
    tweet_message = request.forms.get("message","")
    tweet_user_fk = user['user_id']

    
    the_picture = x.uploadPictures()
    print(the_picture)
   
    
    db = x.db()

    tweet = {
    "tweet_id" : str(uuid.uuid4().hex), # .hex removes the dashes
    "tweet_message" : tweet_message,
    "tweet_image" : the_picture,
    "tweet_created_at" : int(time.time()),
    "tweet_user_fk" : tweet_user_fk,
    "tweet_total_messages" : "0",
    "tweet_total_retweets" : "0",
    "tweet_total_likes" : "0",
    "tweet_total_dislikes" : "0"
    }

    values = ""
    for key in tweet:
      values = values + f":{key},"
    values = values.rstrip(",")
    total_rows_inserted = db.execute(f"INSERT INTO tweets VALUES({values})", tweet).rowcount
    if total_rows_inserted != 1: raise Exception("Please, try again")

    db.commit()
    return {"info":"ok", "user":userData, "tweet":tweet}
  except Exception as ex: # SOMETHING IS WRONG
    response.status = 400
    traceback.print_exc()
    return {"info":str(ex)}
  finally: # This will always take place
    if "db" in locals(): db.close()
