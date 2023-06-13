from bottle import get, template

@get("/test")
def _():
    return template("test")
