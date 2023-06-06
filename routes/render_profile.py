from bottle import get, template, response, request
import pathlib
import sqlite3 
import x


##############################
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}

##############################
@get("/<username>")
# @view("profile")
def _(username):
  try:
    response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)
    cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)

    db = sqlite3.connect(str(pathlib.Path(__file__).parent.parent.resolve())+"/twitter.db")
    db.row_factory = dict_factory
    user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE",(username, )).fetchall()[0]
    user_id = cookie_user["user_id"] # Get the user's id
    user_followed = set(row["followee_id_fk"] for row in db.execute("SELECT followee_id_fk FROM followers WHERE follower_id_fk = ?", (user_id,)))
    
    # tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=?", (user_id, )).fetchall()
    tweets = db.execute("SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id WHERE tweet_user_fk=? ORDER BY tweet_created_at DESC LIMIT 10",(user_id,)).fetchall() # With that id, look up/get the respectives tweets
    trends = db.execute("SELECT * FROM trends").fetchall()
    users = db.execute("SELECT * FROM users").fetchall()
    return template("personal_profile", user=user, trends=trends, users=users, tweets=tweets, cookie_user=cookie_user, user_followed=user_followed) # pass the tweets to the view. Template it
  
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()
