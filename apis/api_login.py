from bottle import post, request, response
import x
import bcrypt
import traceback
##############################
@post("/api-login")
def _():
    try:
        # if user is logged, go to the profile page of that user
        user = request.get_cookie("user", secret=x.COOKIE_SECRET)
        if user: return {"info":"success login", "user_name":user["user_name"]}
        # Validate
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()

        # Connect to database
        db = x.db() #
        user = db.execute("SELECT * FROM users WHERE user_email = ? LIMIT 1", (user_email,)).fetchone()
        # print(user)
        if not user: raise Exception(400, "Cannot login") # hvis ikke user er til at finde, så bring fejlen "cannot login"

        # if not bcrypt.checkpw(user_password.encode("utf-8"), user["user_password"]):
        # raise Exception(400, "Invalid credentials")

        # ÅBNER INDEX-SIDEN NÅR DER LOGGES KORREKT IND
        response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
        response.add_header("Pragma", "no-cache")
        # response.add_header("Expires", 0)   
        response.set_cookie("user", user, secret=x.COOKIE_SECRET)
        response.status = 303
        response.set_header("Location", "/") #fortæller at det er index-siden der åbnes

        try:
            import production
            is_cookie_https = True
        except:
            is_cookie_https = False
        response.set_cookie("user", user, secret=x.COOKIE_SECRET, httponly=True, secure=is_cookie_https)
        return {"info":"success login", "user_name":user["user_name"]}
    except Exception as e:
        print(e)
        traceback.print_exc()
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":e.args[1]}
        except: # Something unknown went wrong
            response.status = 500
            return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()


