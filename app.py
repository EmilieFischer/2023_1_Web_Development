######################### 
from bottle import default_app, get, post, run 
import git 

@post('/secret_url_for_git_hook')
def git_update():
    repo = git.Repo('./2023_1_Web_Development')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return "" 

##############################
@get("/") 
def _():
    return "One" 

# Halløjsa dette er en test

############################## 
try:
    import production
    application = default_app() 
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=6000, debug=True, reloader=True)