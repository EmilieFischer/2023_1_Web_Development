from bottle import get, template, request
import sqlite3
import x


##############################
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


@get("/connect")
def _():
    try:
      cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)
      db = sqlite3.connect("./twitter.db")
      db.row_factory = dict_factory
      tweets = db.execute("SELECT * FROM tweets").fetchall()
      trends = db.execute("SELECT * FROM trends").fetchall()
      users = db.execute("SELECT * FROM users").fetchall()
      return template("connect", trends=trends, tweets=tweets, users=users, cookie_user=cookie_user, tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN)
    except Exception as ex:
      print(ex)
      return "error"
    finally:
      if "db" in locals(): db.close()