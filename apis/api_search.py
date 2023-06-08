import sqlite3
from bottle import post, request, response
import json
import x
import pathlib
import traceback

@post("/search")
def _():
    try:
        db = x.db()
        db.row_factory = x.dict_factory

        #get logged user
        cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)
        user_name = cookie_user["user_name"]

        # Get the search query from the JSON payload
        search_input = request.forms.get("search_input")
        print("I am here")
        print(search_input)

        # Execute the SELECT statement to get all users
        results = db.execute("SELECT * FROM users WHERE user_name LIKE ? AND user_name != ?", ('%' + search_input + '%', user_name,)).fetchall()
        print(results)
        # Convert the rows to a list of dictionaries
        users = []
        for row in results:
            user = {
                "user_id": row["user_id"],
                "user_email": row["user_email"],
                "user_name":row["user_name"],
                "user_avatar":row["user_avatar"]
            }
            users.append(user)

        # Return the list of users as JSON
        response.set_header("content-type", "application/json")
        print(type(users))
        if not search_input:
            return json.dumps([])
        return json.dumps(users)

    except Exception as e:
        print(e)

    finally:
        db.close()