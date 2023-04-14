from bottle import get, template
import x

@get("/verification/<user_verification_key>")
def _(user_verification_key):
    return template("verification")

#########################
# @get("/verification/<user_verification_key>")
# def _(user_verification_key):
#     try:
#         db = x.db()
#         rowsInserted=db.execute("UPDATE users SET user_active WHERE user_verification_key=?", (user_verification_key,)).rowcount

#         if rowsInserted == 0: raise Exception("user not active")
#         return template("verification", succes=1)
#         return {'info':'Ok'}
#     except Exception as ex:
#         if 'db' in locals(): db.rollback()
#         print(ex)
#         return template("verification", succes=0)
#     finally:
#         if 'db' in locals(): db.close()
