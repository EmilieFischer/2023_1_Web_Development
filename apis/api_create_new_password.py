from bottle import get, template, response, request, post
import x

@post("/create_new_password")
def _():
    try:
        
        return {'info':'Ok'}
    except Exception as ex:
        if 'db' in locals(): db.rollback()
        print(ex)
    finally:
        if 'db' in locals(): db.close()
