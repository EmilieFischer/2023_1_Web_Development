from bottle import get, template

#########################
@get("/resetpassword/<user_reset_password_key>")
def _(user_reset_password_key):
    return template("reset_password")