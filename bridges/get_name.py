from bottle import post, request

@post("/test")
def _():
    name = request.forms.get("name")
    return "Hej"