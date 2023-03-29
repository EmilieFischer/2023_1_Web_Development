from bottle import get, static_file


##############################
@get("/js/<filename>")
def _(filename):
  return static_file(filename, "js")
