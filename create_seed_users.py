from faker import Faker
import x
import time
import uuid
import random
import bcrypt

salt = bcrypt.gensalt()
faker = Faker()
user_password = "password"

for fake_user in range(10):
    db = x.db()
    user_id= str(uuid.uuid4().hex)
    user = {
            "user_id" : user_id,
            "user_email" : faker.ascii_email(),            
            "user_name" : faker.user_name(),
            "user_created_at" : int(time.time()),
            "user_verification_key" : str(uuid.uuid4().hex),
            "delete_user_verification_key" : str(uuid.uuid4().hex),
            "user_reset_password_key" : "",
            "user_password": bcrypt.hashpw(user_password.encode('utf-8'), salt),
            "user_first_name" : faker.first_name(),
            "user_last_name" : faker.last_name(),
            "user_verified_at" : 1,
            "user_banner" : "cover.jpg",
            "user_avatar" : "profile.jpg",
            "user_total_tweets" : 0,
            "user_total_retweets" : 0,
            "user_total_comments" : 0,
            "user_total_likes" : 0,
            "user_total_dislikes" : 0,
            "user_total_followers" : 0,
            "user_total_following" : 0
        }
        # create placed holders for values
    values = ""
    for key in user:
        values += f":{key},"
    values = values.rstrip(",")

    db = x.db()
    total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount
    db.commit()
    for tweet in range(random.randint(1,50)):
        tweet = {
          "tweet_id" : str(uuid.uuid4().hex),
          "tweet_message" : faker.text(),
          "tweet_image" : None,
          "tweet_created_at" : int(time.time()),
          "tweet_user_fk" : user_id,
          "tweet_total_messages" : "0",
          "tweet_total_retweets" : "0",
          "tweet_total_likes" : "0",
          "tweet_total_dislikes" : "0"
          }

        # create placed holders for values
        values = ""
        for key in tweet:
            values += f":{key},"
        values = values.rstrip(",")

        total_rows_inserted = db.execute(f"INSERT INTO tweets VALUES({values})", tweet).rowcount
        if total_rows_inserted != 1: raise Exception("Please, try again")
        db.commit()
    if total_rows_inserted != 1: raise Exception("Please, try again")