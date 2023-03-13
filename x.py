from bottle import request
import sqlite3
import pathlib
import re

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
    db.row_factory = dict_factory
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass

# LEN = length
TWEET_MIN_LEN = 2
TWEET_MAX_LEN = 5

# Create error-message for the user if done tweet wrong

def validate_tweet():
  error = f"message min {TWEET_MIN_LEN} max {TWEET_MAX_LEN} characters"
  if len(request.forms.message) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.message) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.get("message")


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
