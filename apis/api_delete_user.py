from bottle import request, delete
import traceback
import x

@delete("/delete-user/<user_id>")
def _(user_id):
    try:
        print(user_id)

        db = x.db()
        db.row_factory = x.dict_factory

        db.execute("DELETE FROM users WHERE user_id=?", (user_id, )).rowcount
        db.commit()

        return f"user deleted: {user_id}"
    except Exception as ex:
        traceback.print_exc()
        print(ex)
    finally:
        if 'db' in locals(): db.close()