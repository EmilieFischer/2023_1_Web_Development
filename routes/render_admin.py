from bottle import get, template

#########################
@get("/admin")
def _():
    return template("admin")