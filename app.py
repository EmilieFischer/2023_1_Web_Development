from bottle import run, post, default_app
import git 


##############################
# ROUTES 
import routes.render_profile
import routes.render_index
import routes.render_about
import routes.render_login
import routes.render_contact
import routes.render_timeout
import routes.render_connect
import routes.render_explore
import routes.render_signup
import routes.render_verification
import routes.render_reset_password
import routes.render_forgot_password

##############################
# APIS
import apis.api_tweet
import apis.api_sign_up
import apis.api_follow
import apis.api_unfollow
import apis.api_login
import apis.api_search
import apis.api_deactivate_user
import apis.api_create_new_password 
import apis.api_delete_tweet
import apis.api_delete_user

############################
# EMAILS
import emails.send_deactivate_user_email
import emails.send_forgot_password_email


############################
# BRIDGES
import bridges.render_logout

##############################
# STATIC FILES
import static_files.get_css 
import static_files.get_images
import static_files.get_js


##############################
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}

############################## 
@post('/secret_url_for_git_hook')
def git_update():
    repo = git.Repo('./2023_1_Web_Development')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return "" 

##############################
try:
    import production
    application = default_app()
except Exception as ex:
    print("Server running locally")
    run(host="127.0.0.1", port=5009, reloader=True, debug=True)