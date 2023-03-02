from bottle import default_app, get, template, run, view, static_file
import os
import sqlite3

trends = [
    {"title":"Sports - Trending", "trend_name":"Holland", "total_hash":6.795},
    {"title":"Trending in Denmark", "trend_name":"Denmark", "total_hash":6.795},
    {"title":"Entertainment - Trending", "trend_name":"Holland", "total_hash":6.795},
    {"title":"Entertainment - Trending", "trend_name":"Holland", "total_hash":6.795},
    {"title":"Entertainment - Trending", "trend_name":"Holland", "total_hash":6.795},
    {"title":"Entertainment - Trending", "trend_name":"Holland", "total_hash":6.795}
]

heros = [
  {"cover_img":"elon_cover.jpg"}
]

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
@get("/js/<filename>")
def _(filename):
  return static_file(filename, "js")


##############################

@get("/")
def _():
  return "Home page"


@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

@get("/output.css")
def _():
  return static_file("output.css", root=".")

##############################
@get("/<username>")
# @view("profile")
def _(username):
  try:
    db = sqlite3.connect(os.getcwd()+"/twitter.db")
    db.row_factory = dict_factory
    user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE",(username,)).fetchall()[0]
    # Get the user's id
    user_id = user["user_id"]
    print("#"*30)
    print(f"user id:{user_id}")
    # With that id, look up/get the respectives tweets
    tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=?", (user_id,)).fetchall()
    trends = db.execute("SELECT * FROM trends").fetchall()
    print("#"*30)
    print(tweets)
    print("#"*30)

    users = db.execute("SELECT * FROM users")
    # pass the tweets to the view. Template it
    
   # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
    return template("profile", user=user, trends=trends, heros=heros, users=users, tweets=tweets)
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()

##############################
# VIEWS
import views.tweet

##############################
# APIS
# makes sure that the app.py calls the api_tweet.py file 
import apis.api_tweet


##############################
# run in AWS
try:
    import production
    print("server running in AWS")
    application =         default_app()
# run in local computer
except Exception as ex:
    print("Server running locally")
    run(host="127.0.0.1", port=4000, debug=True, reloader=True)
