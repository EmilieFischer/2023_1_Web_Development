from bottle import get, template


#########################
@get("/timeout")
def _():
    return template("timeout")

