from bottle import post, request, response, template
import x
import bcrypt
import traceback
##############################
@post("/api-login")
def _():
    try:
        # check if 'admin' is there
        if request.forms.get("user_email") != "admin":

            # if user is logged, go to the profile page of that user
            user = request.get_cookie("user", secret=x.COOKIE_SECRET)
            print(user)
            if user: return {"info":"success login", "user_name":user["user_name"]}
        
            # Validate
            user_email = x.validate_user_email()
            user_password = x.validate_user_password()

            # Connect to database
            db = x.db() #
            user = db.execute("SELECT * FROM users WHERE user_email = ? LIMIT 1", (user_email,)).fetchone()
            print(user)
            if not user:
                response.status=303
                response.set_header("Location", "/")
                raise Exception ("user not found i database")
                
            if user['user_verified_at'] == 0:
                raise Exception ("User not verified")       

            # if not bcrypt.checkpw(user_password.encode("utf-8"), user["user_password"]):
            # raise Exception(400, "Invalid credentials")

            # ÅBNER INDEX-SIDEN NÅR DER LOGGES KORREKT IND
            response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
            response.add_header("Pragma", "no-cache")
            response.add_header("Expires", 0)

            
            # create the jwt with the user's data
            # user_jwt = jwt.encode(user, "the secret", algorithm="HS256")
            # response.set_cookie("user", user, secret=x.COOKIE_SECRET)
            # response.status = 303
            # response.set_header("Location", "/") #fortæller at det er index-siden der åbnes

            try:
                import production
                is_cookie_https = True
            except:
                is_cookie_https = False
            response.set_cookie("user", user, secret=x.COOKIE_SECRET, httponly=True, secure=is_cookie_https)
            return {"info":"Login succes"}
        
        # hvis der er 'admin' i input-feltet gør dette:
        elif request.forms.get("user_email") == "admin":
            db = x.db()
            admin = db.execute("SELECT * FROM admins WHERE admin_name = ? LIMIT 1", ("admin",)).fetchone()
            
            try:
                import production
                is_cookie_https = True
            except:
                is_cookie_https = False
            response.set_cookie("admin", admin, secret=x.COOKIE_SECRET, httponly=True, secure=is_cookie_https)
            return {"info":"Login succes"}
        
    except Exception as e:
        print(e)
        traceback.print_exc()
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":"Login failed", "cause":e.args[1]}
        except: # Something unknown went wrong
            response.status = 500
            return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
