from bottle import post, request, response
import x
import uuid
import time
import bcrypt
import traceback
from emails import send_verification_email

@post("/api-sign-up")
def _():
    try:
        user_name = x.validate_user_name()
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        user_first_name = request.forms.user_first_name
        user_last_name = request.forms.user_last_name
        x.validate_user_confirm_password()
        salt = bcrypt.gensalt()
        user_id = str(uuid.uuid4()).replace("-","")
        user_verification_key = str(uuid.uuid4()).replace("-","")
        delete_user_verification_key = str(uuid.uuid4()).replace("-","")

        user = {
            "user_id" : user_id,
            "user_email" : user_email,            
            "user_name" : user_name,
            "user_created_at" : int(time.time()),
            "user_verification_key" : user_verification_key,
            "delete_user_verification_key" : delete_user_verification_key,
            "user_reset_password_key" : "",
            "user_password": bcrypt.hashpw(user_password.encode('utf-8'), salt),
            "user_first_name" : user_first_name,
            "user_last_name" : user_last_name,
            "user_verified_at" : 0,
            "user_banner" : "cover.jpg",
            "user_avatar" : "profile.jpg",
            "user_total_tweets" : 0,
            "user_total_retweets" : 0,
            "user_total_comments" : 0,
            "user_total_likes" : 0,
            "user_total_dislikes" : 0,
            "user_total_followers" : 0,
            "user_total_following" : 0
        }
        
        # create place holders for values
        values = ""
        for key in user:
            values = values + f":{key},"
        values = values.rstrip(",") #remove whatever you have in the last strip (the comma)
        print(values)
        
        db = x.db()
        total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount
    
        if total_rows_inserted != 1: raise Exception("Please, try again")

        db.commit()
        send_verification_email.send_verification_email(user_email, user_verification_key)

        print(user)
        return {
            "info" : "user created", 
            "user_id" : user_id,
            "user_email" : user_email, 
            "user_name" : user_name, 
            "user_created_at" : int(time.time())
        }
        
    except Exception as e:
        traceback.print_exc()
        print(e)
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":e.args[1]}
        except: # Something unknown went wrong
            if "user_email" in str(e): 
                response.status = 400 
                return {"info":"user_email already exists"}
            if "user_name" in str(e): 
                response.status = 400 
                return {"info":"user_name already exists"}
            response.status = 500
            return {"info":str(e)}
    finally:
        if "db" in locals(): db.close() 