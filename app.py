# 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
# https://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@github.com/EmilieFischer/2023_1_Web_Development.git

from bottle import default_app, post, get, run, template, static_file, request, view
import git 
import os
import pathlib
import x
# sqlite3 = the function that will connect us to the database
import sqlite3 
# this data will come from the database (we will make an array for our tweets)
# for now, we just cided the data


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

# try:
#     import production
#     application = default_app() 
# except Exception as ex:
#     print("Running local server")
#     run(host="127.0.0.1", port=6000, debug=True, reloader=True)

# kør index siden
# @get("/")
# def render_index():
#     try:
#         db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")    
#         db.row_factory = dict_factory
#         users = db.execute("SELECT * FROM users")
#         tweets = db.execute("SELECT * FROM tweets ORDER BY created_at DESC").fetchall()
#         return template("index", users=users, tweets=tweets, title="Twitter")
#     except:
#         print(ex)
#         return "error"
#     finally:
#         if "db" in locals(): db.close()

@get("/")
def render_index():
    try:
       db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
       db.row_factory = dict_factory
       tweets = db.execute("SELECT * FROM tweets").fetchall()
       trends = db.execute("SELECT * FROM trends").fetchall()
       users = db.execute("SELECT * FROM users").fetchall()
       return template("index", title="Twitter", trends=trends, tweets=tweets, users=users)
    except Exception as ex:
        print(ex)
        return "error"
    finally:
        if "db" in locals(): db.close()

##############################
@get("/<username>")
# @view("profile")
def _(username):
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
    db.row_factory = dict_factory
    user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE",(username,)).fetchall()[0]
    # Get the user's id

    user_id = user["user_id"]
    #print("#"*30)
    #print(f"user id:{user_id}")
    # With that id, look up/get the respectives tweets
    tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=?", (user_id)).fetchall()
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


##############################
# VIEWS
import views.tweet

##############################
# APIS
# makes sure that the app.py calls the api_tweet.py file 
import apis.api_tweet

##############################
# run in AWS
# purpose: PythonAnywhere kan aflæse 'production', så det er når man er koblet op til PA at dette ikke er en fejl.
try:
    import production
    print("server running in AWS")
    application = default_app()
# run in local computer
except Exception as ex:
    print("Server running locally")
    run(host="127.0.0.1", port=3001, debug=True, reloader=True, server="paste")
