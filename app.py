from bottle import get, run, template, static_file, response, request

# sqlite3 = the function that will connect us to the database
import sqlite3 
# this data will come from the database (we will make an array for our tweets)
# for now, we just cided the data
# tweets = [
#     {"image_name":"1.jpg", "fullname":"Elon Musk", "username":"@elonmusk"}
# ]

tweets = [
  { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet", "total_messages":"21","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":0, "image_name":"2.jpg", "fullname":"Joe Biden", "username":"joebiden","message":"I am THE president","message_image":"1.jpg","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":0, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","message_image":"1.jpg","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet", "total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
  { "verified":0, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","message_image":"1.jpg","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
]

# list = array
# dictionary is {}. think of it as JSON
trends = [
    {"title":"one", "total_hash":1},
    {"title":"two", "total_hash":2},
    {"title":"three", "total_hash":3}
]

people = [
    {"profile_picture":"1.jpg", "title":"Elon Musk", "user_mail":"elonmusk"},
    {"profile_picture":"1.jpg", "title":"Joe Biden", "user_mail":"joebiden"},
    {"profile_picture":"1.jpg", "title":"Shakira", "user_mail":"shakira"},
    {"profile_picture":"1.jpg", "title":"Shakira", "user_mail":"shakira"},
    {"profile_picture":"1.jpg", "title":"Shakira", "user_mail":"shakira"}
]

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
@get("/")
def render_index():
    return template("index", title="Twitter", tweets=tweets, trends=trends, people=people)

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

#########################
# APIs do not return HTML... there are exceptions
# APIs returns most likely JSON
# Rule 1 - to test the API you use thunderclient or Postman!
@get("/api-get-name")
def _():
    try: # best case scenario
        # get the id, name and lastname from the database
        id = request.query.get("id")
        name = request.query.get("name")
        lastname = request.query.get("lastname")

        if id != "1": raise Exception("the ID is wrong")
        if name != "a": raise Exception("the name is wrong")
        if lastname != "b": raise Exception("the lastname is wrong")

        # connect/open to the database
        db = sqlite3.connect ("twitter.db") # this opens the database
        users = db.execute("SELECT * FROM users").fetchall()
        print(users) # this is for the terminal
        
        # send the name to the client (browser) - the response
        return {"id":id, "name": name, "lastname": lastname}
    except Exception as ex: # the scenario where something went wrong
        print(ex)
        # send a 400 to the client (browser)
        response.status = 400
        return {"error": str(ex)}
    finally: # it must be done, whether something is wrong or right, it just has to happen
        # close the database
        # locals is a function that calls every variables that I have made in this function def_():
        if "db" in locals(): db.close()
        print("I am here")

#########################
#synonym for localhost, men brug altid nedenstående
run(host="127.0.0.1", port=3000, reloader=True, debug=True, server="paste")