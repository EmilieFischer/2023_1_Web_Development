from bottle import post, request, response
import x
import uuid
import time
import os

# 'post' is the same as 'create'
# ? = placeholder - the only way you should talk to the database = safety. It is to prevend sequal invention
@post("/tweet")
def _():
  try: # SUCCESS
    x.validate_tweet()
    user = request.get_cookie("user", secret=x.COOKIE_SECRET)
    if not user: print("User not found")

    # the_picture = request.files.get("images")
    # name, ext = os.path.splitext(the_picture.filename) #filename = happy.jpg (name = happy, ext = .jpg)
      
    # Check if the file extension is allowed
    # if ext not in (".png", ".jpg", ".jpeg"): # how to check the mime type
      # response.status = 400
      # return "This picture is not allowed"
      
    # Generate a unique filename
    # picture_name = str(uuid.uuid4().hex)
    # picture_name = picture_name + ext #this will become the uuid.jpg
      
    # Save the picture to the 'images' directory
    # the_picture.save(f"images/{picture_name}")

    
    db = x.db()

    tweet = {
    "tweet_id" : str(uuid.uuid4().hex), # .hex removes the dashes
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
