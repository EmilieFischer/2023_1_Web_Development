from bottle import get, template, response, request
import traceback
import x

@get("/delete-tweet/<tweet_id>")
def _(tweet_id):
    try:
        tweet_id = request.forms.get("delete_tweet", "")

        db = x.db()
        tweet = db.execute("SELECT * FROM tweets WHERE tweet_id = ?",(tweet_id, )).fetchone()
        if not tweet: raise Exception ("invalid tweet id")
    
        tweet_deleted = db.execute("DELETE * FROM tweets WHERE tweet_id=?", (tweet_id,)).rowcount
        if tweet_deleted == 0:
            raise Exception ("tweet not deleted")
        
        db.commit()

    
        return {'info':'Ok'}
    except Exception as ex:
        traceback.print_exc()
        response.status = 400
        return {"info":str(ex)}
    finally:
        if 'db' in locals(): db.close()