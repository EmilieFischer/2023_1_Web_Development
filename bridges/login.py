from bottle import post, response

@post("/login")
def _():
    # Redirection if the login goes wrong. So you take the browser to a different page
    # the status code
    # the redirected page
    user = {
        "user_name":"emiliefischer", 
        "user_first_name":"Emilie", 
        "user_last_name":"Fischer"
    }
    # cookie_expiration_date = int(time.time()) + 7200
    response.set_cookie("user", user, secret="my-secret", httponly=True)
    response.status = 303
    response.set_header("Location", "/")
    return
