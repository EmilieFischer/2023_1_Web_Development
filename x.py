from bottle import request, response
import sqlite3
import pathlib
import re
import magic
import os
import uuid


############################## GETS COOKIE SECRET
COOKIE_SECRET = "41ebeca46feb-4d77-a8e2-554659074C6319a2fbfb-9a2D-4fb6-Afcad32abb26a5e0"

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################

def db():
  try:
    print(str(pathlib.Path(__file__).parent.resolve()))
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
    db.execute("PRAGMA foreign_key==ON")
    db.row_factory = dict_factory
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass

############################## MIMETYPE UPLOAD PICTURE  
def uploadPictures():
  try:
    # tjekker om der er et billede i tweetet. Hvis der ikke er (og hvis filnavnet er tomt), så returner ingenting
    the_picture = request.files.get("image", "")
    if not the_picture : return None
    if the_picture.filename == "" or the_picture.filename == "empty":
      return None
    # hvis der er, tjek ext 
    _, ext = os.path.splitext(the_picture.filename) 
    
    # tjek om ext er tilladt
    if ext not in (".png", ".jpg", ".jpeg"):
        raise Exception("This picture is not allowed")
    
    # gem billedet
    picture_name = str(uuid.uuid4().hex) + ext
    the_picture.save(str(pathlib.Path(__file__).parent.resolve())+f"/images/{picture_name}")
    
    # tjek mimetype
    mimetype = magic.from_file(str(pathlib.Path(__file__).parent.resolve())+f"/images/{picture_name}", mime=True)
    print(mimetype)
     # tjek om mimetype er tilladt
    if mimetype not in ("image/jpg", "image/png", "image/jpeg"):
        os.remove(str(pathlib.Path(__file__).parent.resolve())+f"/images/{picture_name}")
        raise Exception("This mimetype is not allowed")
    
    return picture_name
  except Exception as ex:
      print(ex)
  finally:
      pass


##############################
def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)

############################## TWEET VALIDATION
# LEN = length
TWEET_MIN_LEN = 2
TWEET_MAX_LEN = 50

def validate_tweet():
  error = f"message min {TWEET_MIN_LEN} max {TWEET_MAX_LEN} characters"
  if len(request.forms.message) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.message) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.get("message")


############################## EMAIL VALIDATION
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


############################## USER LOGGED VALIDATION
def validate_user_logged():
    user = request.get_cookie("user", secret=COOKIE_SECRET)
    if user is None: raise Exception("user must login")
    return user


############################## USER NAME VALIDATION
USER_NAME_MIN = 4
USER_NAME_MAX = 15
USER_NAME_REGEX = "^[a-zA-Z0-9_]*$"

def validate_user_name():
  print("*"*30)
  print (request.forms.user_name)
  error = f"user_name {USER_NAME_MIN} to {USER_NAME_MAX} english letters or numbers from 0 to 9"
  # strip = removes the empty "letters" if the user by accident uses the space-button before or after the username
  request.forms.user_name = request.forms.user_name.strip()
  if len(request.forms.user_name) < USER_NAME_MIN: raise Exception(error)
  if len(request.forms.user_name) > USER_NAME_MAX: raise Exception(error)
  # if the virable we have does not match what we want to send
  if not re.match(USER_NAME_REGEX, request.forms.user_name): raise Exception(error)
  return request.forms.user_name
