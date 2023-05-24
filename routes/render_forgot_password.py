from bottle import get, template

#########################
@get("/forgotpassword")
def _():
    return template("forgot_password")