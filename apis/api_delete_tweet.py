from bottle import request, delete
import traceback
import x

@delete("/delete-tweet/<tweet_id>")
def _(tweet_id):
    try:
        print(tweet_id)

        db = x.db()
        db.row_factory = x.dict_factory

        db.execute("DELETE FROM tweets WHERE tweet_id=?", (tweet_id, )).rowcount

        db.commit()

        return f"tweet deleted: {tweet_id}"
    except Exception as ex:
        traceback.print_exc()
        print(ex)
    finally:
        if 'db' in locals(): db.close()