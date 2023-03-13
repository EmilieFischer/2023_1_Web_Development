from bottle import post, request, response
import x

################################
# The first thing you do is this: you test the API in thunderclient
# @post("/api-sign-up")
# def _():
#     return "ok1"

# Next step is this
@post("/api-sign-up")
def _():
    try:
        user_name = x.validate_user_name()
        user_id = 1
        # create dictionary for user
        user = {
            "user_id":user_id,
            "user_name":user_name
        }
        values = ""
        for key in user:
            values = values + f":{key},"
        values = values.rstrip(",") #remove whatever you have in the last strip (the comma)
        print(values)
        # db.execute("INSERT INTO users VALUES()",)
        db.execute(f"INSERT INTO users VALUES({values})", user)
        return "ok"
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close() 