from bottle import get, run, post, static_file, template, response, request, default_app
import git 
import pathlib
import sqlite3 
import traceback
import os
import uuid
import x



@post("/upload-picture")
def _():
   try:
      the_picture = request.files.get("picture")
      name, ext = os.path.splitext(the_picture.filename) #filename = happy.jpg (name = happy, ext = .jpg)
      if ext not in (".png", ".jpg", ".jpeg"): # how to check the mime type
         response.status = 400
         return "Picture not allowed"
      picture_name = str(uuid.uuid4().hex)
      picture_name = picture_name + ext #this will become the uuid.jpg
      the_picture.save(f"pictures/{picture_name}")

      # read the mime type
      # if it is not one that is allowed 
      # delete the picture
      # tell the user to "stop being funny and mess with the code"
      # if it is the real thing
      # repsond with "ok"

      return "picture uploaded"
   except Exception as e:
      print(e)
   finally:
      pass


##############################
# ROUTES 
import routes.render_profile
import routes.render_index
import routes.render_logout
import routes.render_about
import routes.render_login
import routes.render_contact
import routes.render_timeout
import routes.render_test
import routes.render_connect
import routes.render_explore
import routes.render_signup
import routes.render_verification
import routes.render_reset_password
import routes.render_forgot_password

##############################
# VIEWS
import views.tweet
import views.test

##############################
# APIS
# makes sure that the app.py calls the api_tweet.py file 
import apis.api_tweet
import apis.api_sign_up
import apis.api_follow
import apis.api_login
import apis.api_test
import apis.api_get_latest_tweets
import apis.api_search
import apis.api_unfollow
import apis.api_delete_user
import emails.send_delete_user_email
import emails.send_forgot_password_email


############################
# BRIDGES
import bridges.login

##############################
# STATIC FILES
import static_files.get_css 
import static_files.get_images
import static_files.get_js


##############################
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}

##############################
@post('/secret_url_for_git_hook')
def git_update():
    repo = git.Repo('./2023_1_Web_Development')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return "" 

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
