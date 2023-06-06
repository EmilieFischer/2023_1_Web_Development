from bottle import response, request, post
import x
import bcrypt

@post("/create-new-password")
def _():
    try:
        user_reset_password_key = request.forms.get("user_reset_password_key")
        if user_reset_password_key == "":
            raise Exception(400, "User reset key not found")
        user_password = x.validate_user_password()

        salt = bcrypt.gensalt()
        user_password = bcrypt.hashpw(user_password.encode('utf-8'), salt)

        db = x.db()

        total_changes = db.execute("""
            UPDATE users
            SET user_password = ?, user_reset_password_key = ""
            WHERE user_reset_password_key = ?
        """, (user_password, user_reset_password_key)).rowcount
        
        db.commit()

        if not total_changes: raise Exception(400, "Could not update password. Please doublecheck that the reset key is valid.")
        return {"info":"Reset password succes"}

    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback()
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":e.args[1]}
        except:
            response.status = 500
            return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
