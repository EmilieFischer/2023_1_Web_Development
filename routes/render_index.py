from bottle import get, run, post, static_file, template, response, request, default_app
import sqlite3 
import x

##############################
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}

@get("/")
def render_index():
    response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)

    cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)

    try:
      # db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve()) + "/twitter.db")
      db = sqlite3.connect("./twitter.db")
      db.row_factory = dict_factory
      tweets = db.execute("SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id ORDER BY tweet_created_at DESC LIMIT 10").fetchall()
      print (tweets)
      trends = db.execute("SELECT * FROM trends").fetchall()
      users = db.execute("SELECT * FROM users").fetchall()
      return template("index", trends=trends, tweets=tweets, users=users, cookie_user=cookie_user, tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN)
    except Exception as ex:
      print(ex)
      return "error"
    finally:
      if "db" in locals(): db.close()


