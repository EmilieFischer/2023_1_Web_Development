from bottle import post, request, response
import x

# post = creating something in the system (what is really says). I know that it is a post because we want to insert something in the database. Also we have a form that is a post
@post("/api-follow")
def _():
    try:
        # TODO: get user from cookie
        # user = request.get_cookie("user", secret="xxxxxx")

        # if user is logged, go to the profile page of that user
        user = request.get_cookie("user", secret=x.COOKIE_SECRET)

        # TODO: get user id from the user from the cookie 
        # TODO: validate the followeers id
        # TODO: connect to the database
        # TODO: insert into followers table
        user_followee_id = request.forms.get("user_followee_id", "") 
        return {"info":f"following user with id: {user_followee_id}"}
    except Exception as e:
        print(e) #is made so we can see the exception in the terminal
        pass
    finally:
        pass