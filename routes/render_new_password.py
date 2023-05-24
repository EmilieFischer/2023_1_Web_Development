from bottle import get, template

#########################
@get("/new_password")
def _():
    return template("new_password")