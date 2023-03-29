from bottle import get, static_file


#########################
@get("/output.css")
def _():
    return static_file("output.css", root=".")