from bottle import get, run, post, static_file, template, response, request, default_app
import git 
import pathlib
import sqlite3 
import traceback


@get("/")
def render_index():
    response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)

    cookie_user = request.get_cookie("user", secret="my-secret")

    try:
      # db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve()) + "/twitter.db")
      db = sqlite3.connect("./twitter.db")
      db.row_factory = dict_factory
      tweets = db.execute("SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id").fetchall()
    #   print (tweets)
      trends = db.execute("SELECT * FROM trends").fetchall()
      users = db.execute("SELECT * FROM users").fetchall()
      return template("index", trends=trends, tweets=tweets, users=users, cookie_user=cookie_user)
    except Exception as ex:
      print(ex)
      return "error"
    finally:
      if "db" in locals(): db.close()

@get("/personal_profile")
def _():
    response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)

    cookie_user = request.get_cookie("user", secret="my-secret")

    try:
      # db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve()) + "/twitter.db")
      db = sqlite3.connect("./twitter.db")
      db.row_factory = dict_factory
      tweets = db.execute("SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id").fetchall()
      print (tweets)
      trends = db.execute("SELECT * FROM trends").fetchall()
      users = db.execute("SELECT * FROM users").fetchall()
      user = db.execute("SELECT * FROM users WHERE user_name = ? COLLATE NOCASE", (cookie_user["user_name"],)).fetchall()[0] 
      return template("personal_profile", trends=trends, tweets=tweets, users=users, cookie_user=cookie_user, user=user)
    except Exception as ex:
      traceback.print_exc()
      print(ex)
      return "error"
    finally:
      if "db" in locals(): db.close()

@post('/secret_url_for_git_hook')
def git_update():
    repo = git.Repo('./2023_1_Web_Development')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return "" 

##############################
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


##############################
@get("/js/<filename>")
def _(filename):
  return static_file(filename, "js")

#########################
#gør sådan så alle jpg'er bliver læst
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

#########################
@get("/output.css")
def _():
    return static_file("output.css", root=".")

#########################
# skaber stien til about-siden, så brugeren bare kan søge "about" i browseren i stedet for hele html-navnet
@get("/about")
def _():
    return template("about-us")


#########################
@get("/login")
def _():
    return template("login")

#########################
# skaber stien til contact-siden, så brugeren bare kan søge "about" i browseren i stedet for hele html-navnet
# inkluderer eksempel på hvordan man tilføjer title via variabler i app.py
@get("/contact")
def _():
    return template("contact-us", title="Contact us")

#########################
# skaber stien til explore-siden, så brugeren bare kan søge "about" i browseren i stedet for hele html-navnet
@get("/explore")
def _():
    return template("explore")


##############################
@get("/<username>")
# @view("profile")
def _(username):
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
    db.row_factory = dict_factory
    user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE",(username, )).fetchall()[0]
    # Get the user's id

    user_id = user["user_id"]
    #print("#"*30)
    #print(f"user id:{user_id}")
    # With that id, look up/get the respectives tweets
    tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=?", (user_id, )).fetchall()
    trends = db.execute("SELECT * FROM trends").fetchall()
    #print("#"*30)
    #print(tweets)
    #print("#"*30)

    users = db.execute("SELECT * FROM users").fetchall()
    # pass the tweets to the view. Template it
    
   # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
    return template("profile", user=user, trends=trends, users=users, tweets=tweets)
  except Exception as ex:
    print(ex)
    return "error"
  finally:
    if "db" in locals(): db.close()


############################
@get("/login")
def _():
    return template("login")

@get("/logout")
def _():
    response.set_cookie("user", "", expires=0)
    response.status = 303
    response.set_header("Location", "/login")
    return


##############################
# VIEWS
import views.tweet

##############################
# APIS
# makes sure that the app.py calls the api_tweet.py file 
import apis.api_tweet

############################
import bridges.login


##############################
# run in AWS
# purpose: PythonAnywhere kan aflæse 'production', så det er når man er koblet op til PA at dette ikke er en fejl.
try:
    import production
    db = sqlite3.connect("/2023_1_Web_Development/twitter.db")
    print("server running in AWS")
    application = default_app()
# run in local computer
except Exception as ex:
    print("Server running locally")
    run(host="127.0.0.1", port=5009, reloader=True, debug=True)
