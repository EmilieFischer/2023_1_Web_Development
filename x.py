from bottle import request, response
import sqlite3
import pathlib
import re


##############################
COOKIE_SECRET = "41ebeca46feb-4d77-a8e2-554659074C6319a2fbfb-9a2D-4fb6-Afcad32abb26a5e0"

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################

def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
    db.execute("PRAGMA foreign_key==ON")
    db.row_factory = dict_factory
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass


##############################
def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)

##############################
# def validate_user_logged():
#     user = request.get_cookie("user", secret=COOKIE_SECRET)
#     if user is None: raise Exception(400, "user must login")
#     return user

##############################
# LEN = length
TWEET_MIN_LEN = 2
TWEET_MAX_LEN = 50

# Create error-message for the user if done tweet wrong
def validate_tweet():
  error = f"message min {TWEET_MIN_LEN} max {TWEET_MAX_LEN} characters"
  if len(request.forms.message) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.message) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.get("message")


##############################
USER_EMAIL_MIN = 6
USER_EMAIL_MAX = 100
USER_EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"

def validate_user_email():
	error = f"user_email invalid"
	request.forms.user_email = request.forms.user_email.strip()
	if len(request.forms.user_email) < USER_EMAIL_MIN : raise Exception(400, error)
	if len(request.forms.user_email) > USER_EMAIL_MAX : raise Exception(400, error)  
	if not re.match(USER_EMAIL_REGEX, request.forms.user_email): raise Exception(400, error)
	return request.forms.user_email


############################## PASSWORD VALIDATION

USER_PASSWORD_MIN = 6
USER_PASSWORD_MAX = 50

def validate_user_password():
	error = f"user_password need to be between {USER_PASSWORD_MIN} to {USER_PASSWORD_MAX} characters"
	request.forms.user_password = request.forms.user_password.strip()
	if len(request.forms.user_password) < USER_PASSWORD_MIN : raise Exception(400, error)
	if len(request.forms.user_password) > USER_PASSWORD_MAX : raise Exception(400, error)
	return request.forms.user_password

def validate_user_confirm_password():
	error = f"user_password and user_confirm_password do not match"
	request.forms.user_password = request.forms.user_password.strip()
	request.forms.user_confirm_password = request.forms.user_confirm_password.strip()
	if request.forms.user_confirm_password != request.forms.user_password: raise Exception(400, error)
	return request.forms.user_confirm_password


# ------------------ reset password validation
# USER_PASSWORD_MIN = 6
# USER_PASSWORD_MAX = 50

# def validate_user_password():
#   password = request.forms.user_password 
#   error = f"The password you entered did not match our records. Please double check and try again." 
#   user_password = request.forms.user_password = request.forms.user_password.strip() 
#   if len(request.forms.user_password) < USER_PASSWORD_MIN:
#     raise Exception(error) 
#   if len(request.forms.user_password) > USER_PASSWORD_MAX: 
#     raise Exception(error) 
#   return request.forms.user_password


# def validate_user_confirm_password():
# 	error = f"user_password and user_confirm_password do not match"
# 	user_password = request.forms.get("user_password", "").strip()
# 	user_confirm_password = request.forms.get("user_confirm_password", "").strip()
# 	if user_confirm_password != user_password: raise Exception(400, error)
# 	return user_confirm_password


##############################
def validate_user_logged():
    user = request.get_cookie("user", secret=COOKIE_SECRET)
    if user is None: raise Exception(400, "user must login")
    return user



##############################
# the rules for the username
# why capitalize? = a constant that I should never change
# regex = what the user is allowed to put inside the username = english letters only and numbers from 0 to 9
USER_NAME_MIN = 4
USER_NAME_MAX = 15
USER_NAME_REGEX = "^[a-zA-Z0-9_]*$"
# now create the function to validate
def validate_user_name():
  print("*"*30)
  # analize in the terminal
  print (request.forms.user_name)
  error = f"user_name {USER_NAME_MIN} to {USER_NAME_MAX} english letters or numbers from 0 to 9"
  # strip = removes the empty "letters" if the user by accident uses the space-button before or after the username
  request.forms.user_name = request.forms.user_name.strip()
  if len(request.forms.user_name) < USER_NAME_MIN: raise Exception(error)
  if len(request.forms.user_name) > USER_NAME_MAX: raise Exception(error)
  # if the virable we have does not match what we want to send
  if not re.match(USER_NAME_REGEX, request.forms.user_name): raise Exception(error)
  # if everything is okay, then return
  return request.forms.user_name
