from bottle import run, post, response, request, default_app
import git 
import pathlib
import sqlite3 
import traceback
import os
import uuid


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
import apis.api_create_new_password 
import apis.api_upload_pictures

############################
# EMAILS
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

############################## github will inform PA that a new code has been pushed to Github
@post('/24cab7a8d5c54cc89090b7271775361c')
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
    # db = sqlite3.connect("/2023_1_Web_Development/twitter.db")
    # print("server running in AWS")
    application = default_app()
# run in local computer
except Exception as ex:
    print("Server running locally")
    run(host="127.0.0.1", port=5009, reloader=True, debug=True)

# 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
# https://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@github.com/EmilieFischer/2023_1_Web_Development.git