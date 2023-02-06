from bottle import get, run

#########################
@get("/")
def render_index():
    return "hi"

#########################
#synonym for localhost, men brug altid nedenstående
run(host="127.0.0.1", port=3000, reloader=True, debug=True)