from bottle import get, run, template, static_file, response, request

# sqlite3 = the function that will connect us to the database
import sqlite3 
# this data will come from the database (we will make an array for our tweets)
# for now, we just cided the data


tweets = [
  { "verified":1, "might_like":"you might like", "image_name":"3658fee36e88469b90ba6490bd52422c.jpg", "fullname":"Elon Musk", "username":"elonmusk", "hours":"· 9h", "message":"This is looking great! I just love my new mansion", "message_image":"2.jpg", "total_messages":"578","total_retweets":"4492","total_likes":"4726","total_dislikes":"365",},
  { "verified":0, "might_like":"Elon commented this", "image_name":"joe.jpg", "fullname":"Joe Biden", "username":"joebiden", "hours":"· 3h", "message":"I am THE new president! I will now make it the best country evaaaaaaaaar! BELIEVE ME!","message_image":"president.jpg","total_messages":"7482","total_retweets":"894","total_likes":"75832","total_dislikes":"3359",},
  { "verified":1, "might_like":"you might like", "image_name":"d4c66eb4aa3342d2b1dff4c39bee7003.jpg", "fullname":"Shakira", "username":"shakira", "hours":"· 2h", "message":"Just filmed my new musicvideo! It went amaaaaaazing and I was so beautiful - you would not believe it! Just look at this picture - wow!", "message_image":"dancing.jpg", "total_messages":"253","total_retweets":"7482","total_likes":"3","total_dislikes":"527",},
  { "verified":0, "might_like":"Shakira commented this", "image_name":"07a08c8b225f4713a8b427f7de39f67d.jpg", "fullname":"Britney Spears", "username":"britneyspears", "hours":"· 17h", "message":"Just sitting here missing my ex-boyfriend! Justin Timberlake was just so handsome you would not believe it!","message_image":"scandal.jpg","total_messages":"748","total_retweets":"885","total_likes":"393","total_dislikes":"2501",},
  { "verified":1, "might_like":"you might like", "image_name":"michael.jpg", "fullname":"Michael Jackson", "username":"michaeljackson", "hours":"· 14h", "message":"Just finished my last show tonight. Thank you all for always believing in me - it has been an amazing journey - see you in heaven! Peace and love to you all!","message_image":"show.jpg", "total_messages":"5839","total_retweets":"5729","total_likes":"87584","total_dislikes":"329",},
]

# list = array
# dictionary is {}. think of it as JSON
trends = [
    {"title":"Sports - Trending", "trend_name":"Holland", "total_hash":6.795},
    {"title":"Trending in Denmark", "trend_name":"Denmark", "total_hash":6.795},
    {"title":"Entertainment - Trending", "trend_name":"Holland", "total_hash":6.795},
    {"title":"Entertainment - Trending", "trend_name":"Holland", "total_hash":6.795},
    {"title":"Entertainment - Trending", "trend_name":"Holland", "total_hash":6.795},
    {"title":"Entertainment - Trending", "trend_name":"Holland", "total_hash":6.795}
]

# people = [
#     {"profile_picture":"3658fee36e88469b90ba6490bd52422c.jpg", "title":"Elon Musk", "user_mail":"elonmusk"},
#     {"profile_picture":"joe.jpg", "title":"Joe Biden", "user_mail":"joebiden"},
#     {"profile_picture":"d4c66eb4aa3342d2b1dff4c39bee7003.jpg", "title":"Shakira", "user_mail":"shakira"},
#     {"profile_picture":"07a08c8b225f4713a8b427f7de39f67d.jpg", "title":"Britney Spears", "user_mail":"britneyspears"},
#     {"profile_picture":"michael.jpg", "title":"Michael Jackson", "user_mail":"michaeljackson"}
# ]

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
    return template("index", title="Twitter", tweets=tweets, trends=trends)
    # return template("index", title="Twitter", tweets=tweets, trends=trends, people=people)


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
run(host="127.0.0.1", port=3000, reloader=True, debug=True)