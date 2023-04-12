from bottle import get, template


#########################
@get("/verification/<user_verification_key>")
def _():
    return template("verification")