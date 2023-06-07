from bottle import view

@view("/test")
def _():
    name = "Emilie"
    return dict(name=name)
