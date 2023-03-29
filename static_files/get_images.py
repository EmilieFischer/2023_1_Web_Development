from bottle import get, static_file



@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")