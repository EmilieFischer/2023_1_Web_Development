# 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
# https://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@github.com/EmilieFischer/2023_1_Web_Development.git

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
    return "Please subscribe and like!" 

############################## 
try:
    import production
    application = default_app() 
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=6000, debug=True, reloader=True)