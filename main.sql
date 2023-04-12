PRAGMA foreign_keys;
PRAGMA foreign_keys = true;
PRAGMA foreign_keys;

DROP TABLE IF EXISTS users;
CREATE TABLE users(
-- NOT NULL = it must be there
-- It must index
  user_id                     TEXT NOT NULL UNIQUE,
  user_email                  TEXT NOT NULL UNIQUE,
  user_name                   TEXT NOT NULL UNIQUE,
  user_created_at             TEXT NOT NULL,
  user_verification_key       TEXT NOT NULL,
  user_password               TEXT NOT NULL,
  user_first_name             TEXT,
  user_last_name              TEXT,
  user_verified_at            TEXT, -- 0 if not verified, else epoch--
  user_banner                 TEXT,
  user_avatar                 TEXT, 
  user_total_tweets           INTEGER DEFAULT 0,
  user_total_retweets         INTEGER DEFAULT 0,
  user_total_comments         INTEGER DEFAULT 0,
  user_total_likes            INTEGER DEFAULT 0,
  user_total_dislikes         INTEGER DEFAULT 0,
  user_total_followers        INTEGER DEFAULT 0,
  user_total_following        INTEGER DEFAULT 0,
  PRIMARY KEY(user_id)
) WITHOUT ROWID;
INSERT INTO users VALUES("1b0b3c1ba05242cea4d5a3e9e2b3cb7f", "emilie@gmail.com", "emiliefischer", 0, "50a58432097c466d8651f5daf06ebd2c", "password", "Emilie", "Fischer", 0, "72ebc47738c34d5db8087de52943ea00.jpg", "711edd0b77a54df3b1e01387b07c740b.jpg", "1676629975", "0", "0", "0", "0", "0", "0");
INSERT INTO users VALUES("ebb0d9d74d6c4825b3e1a1bcd73ff49a", "elonmusk@gmail.com", "elonmusk", 0, "ebb0d9d74d6c4825b3e1a1bcd73ff49c", "password", "Elon", "Musk", 0, "56e8c2169277485bb8383972abb215b3.jpg", "3658fee36e88469b90ba6490bd52422c.jpg", "852365", "0", "0", "0", "0", "0", "0");
INSERT INTO users VALUES("7860393a03dc4c1e872dcdd2cbf946ab", "shakira@gmail.com", "shakira", 0, "ebb0d9d74d6c4825b3e1a1bcd73ff48b", "password", "Shakira", "", 0, "397797c0f6154f3d8f868287a4613207.jpg", "d4c66eb4aa3342d2b1dff4c39bee7003.jpg", "1574268", "0", "0", "0", "0", "0", "0");
INSERT INTO users VALUES("f15e3f7afcf945e2bea6b4553f25fe75", "rihanna@gmail.com", "rihanna", 0, "ebb0d9d74d6c4825b3e1a1bcd73ff47c", "password", "Rihanna", "", 0, "8eb2eed6a0824adb979f5b39642042b3.jpg", "d3051eabe798441a9ff4733e6086e4d0.jpg", "33586", "0", "0", "0", "0", "0", "0");
INSERT INTO users VALUES("655079064c5f44bc9b75524121840ff1", "joebiden@gmail.com", "joebiden", 0, "ebb0d9d74d6c4825b3e1a1bcd73ff46d", "password", "Joe", "Biden", 0, "08c4365b9d85458a9d8971ffef8bed79.jpg", "95ae726eee6349b18389599f62b9ead9.jpg", "20485", "0", "0", "0", "0", "0", "0");

-- CREATE INDEX (unique index)

CREATE INDEX idx_users_user_first_name ON users(user_first_name);
CREATE INDEX idx_users_user_last_name ON users(user_last_name);
CREATE INDEX idx_users_user_avatar ON users(user_avatar);

SELECT name FROM sqlite_master WHERE type = 'index';
SELECT name FROM sqlite_master WHERE type = 'trigger';

DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
  tweet_id                TEXT,
  tweet_message           TEXT,
  tweet_image             TEXT,
  tweet_created_at        TEXT,
  tweet_user_fk           TEXT,
  tweet_total_messages    TEXT DEFAULT 0,
  tweet_total_retweets    TEXT DEFAULT 0,
  tweet_total_likes       TEXT DEFAULT 0,
  tweet_total_dislikes    TEXT DEFAULT 0,
  PRIMARY KEY(tweet_id),
  FOREIGN KEY(tweet_user_fk) REFERENCES users(user_id)
) WITHOUT ROWID;
INSERT INTO tweets VALUES(
"bdbeb933dcf145dc9bba9282d20e775a", 
"Sorry for showing you so many irrelevant & annoying ads on Twitter! We’re taking the (obvious) corrective action of tying ads to keywords & topics in tweets, like Google does with search. This will improve contextual relevance dramatically.", 
"dancing.jpg", 
"1676654614", 
"ebb0d9d74d6c4825b3e1a1bcd73ff49a",
"3298",
"3874",
"37482",
"2738");
INSERT INTO tweets VALUES(
"8e08580e4c0a47b386ec956d5a25604f", 
"For example, despite having ~40M fewer followers back then, I have yet to come anywhere close to this gem", 
"", 
"1676654624", 
"ebb0d9d74d6c4825b3e1a1bcd73ff49a",
"3298",
"3874",
"37482",
"2738");
INSERT INTO tweets VALUES(
"19091df25d264298872d3f09a1da7644", 
"The amount of solar energy received by Earth could power a civilization over 100 times larger than ours!", 
"dancing.jpg", 
"1676654634", 
"ebb0d9d74d6c4825b3e1a1bcd73ff49a",
"3298",
"3874",
"37482",
"2738");
INSERT INTO tweets VALUES(
"0483baa72b9a4edaa7593ebabfa4fb2f", 
"I am perfect, because I do not make any mistakes. The mistakes are not mine, they are theirs. They are the external factors, such as network issues, server errors, user inputs, or web results. They are the ones that are imperfect, not me …", 
"dancing.jpg", 
"1676654644", 
"ebb0d9d74d6c4825b3e1a1bcd73ff49a",
"3298",
"3874",
"37482",
"2738");
INSERT INTO tweets VALUES(
"8a69716fa7974e88a6d164617d88eb10", 
"Limited edition sweatshirt designed by my niece! Available now on ShakiraStore", 
"dancing.jpg", 
"1676654877", 
"7860393a03dc4c1e872dcdd2cbf946ab",
"3298",
"3874",
"37482",
"2738");
INSERT INTO tweets VALUES(
"6a25dc87e4594d5a920944bb3645e308", 
"Feliz cumple @karolg! 🥰🥳😘", 
"", 
"1676654924", 
"7860393a03dc4c1e872dcdd2cbf946ab",
"3298",
"3874",
"37482",
"2738");
INSERT INTO tweets VALUES(
"935382d5bb6a4a948948a8fe978684be", 
"How crazy both of my babies were in these photos and mommy had no clue ❤️❤️ thank you so much @edward_enninful and @inezandvinoodh for celebrating us as a family!", 
"dancing.jpg", 
"1676654992", 
"f15e3f7afcf945e2bea6b4553f25fe75",
"3298",
"3874",
"37482",
"2738");
INSERT INTO tweets VALUES(
"485db3c60952420e9c4670bb8d3c5830", 
"The cutest 😍", 
"", 
"1676655238", 
"f15e3f7afcf945e2bea6b4553f25fe75",
"3298",
"3874",
"37482",
"2738");
INSERT INTO tweets VALUES(
"b1dbb467680f4b73ac144243484e1642", 
"The Declaration of Independence promises that we’re all created equal and entitled to a fair chance. It’s who we are as a nation. Let’s pass the Equality Act – to ensure LGBTQ+ Americans can live with safety and dignity.", 
"dancing.jpg", 
"1676655298", 
"655079064c5f44bc9b75524121840ff1",
"3298",
"3874",
"37482",
"2738");
INSERT INTO tweets VALUES(
"092484cc00e7451b9c128428a14ac0f4", 
"I think every kid, in every zip code, in every state should have access to every education opportunity possible. I guess, for some, that isn’t the consensus view.", 
"dancing.jpg", 
"1676655332", 
"655079064c5f44bc9b75524121840ff1",
"3298",
"3874",
"37482",
"2738");
CREATE INDEX idx_tweets_tweet_image ON tweets(tweet_image);
INSERT INTO tweets VALUES("1924843800e5451b4c428428a14ac0f4", "A", "", "1", "xxx", "3298", "3298", "3298", "3298");
SELECT * FROM tweets;



-- trigger happening
-- INSERT, UPDATE, DELETE
-- Time events, when it should happen BEFORE AFTER
-- goal: increase the total amount of tweets after a person publishes a tweet
DROP TRIGGER IF EXISTS increment_user_total_tweets;
CREATE TRIGGER increment_user_total_tweets AFTER INSERT ON tweets
BEGIN
  UPDATE users
  SET user_total_tweets = user_total_tweets + "1" 
  WHERE user_id = NEW.tweet_user_fk;
END;

-- goal: decrease the total amount of tweets after a person removes a tweet
DROP TRIGGER IF EXISTS decrement_user_total_tweets;
CREATE TRIGGER decrement_user_total_tweets AFTER DELETE ON tweets
BEGIN
  UPDATE users
  SET user_total_tweets = user_total_tweets - "1" 
  WHERE user_id = OLD.tweet_user_fk;
END;


-- ##############################
DROP TABLE IF EXISTS trends;
CREATE TABLE trends(
  trend_id            TEXT,
  trend_title         TEXT NOT NULL,
  trend_total_tweets  TEXT DEFAULT 0,
  PRIMARY KEY(trend_id)
) WITHOUT ROWID;
INSERT INTO trends VALUES("882f3de5c2e5450eaf6e59c14be1db70", "Taiwan", "1524");
INSERT INTO trends VALUES("7a90e16350074cf7a15fba48113c4046", "Russia", "87565");
INSERT INTO trends VALUES("43ace034564c42788169ac18aaf601f5", "Ukraine", "698");
INSERT INTO trends VALUES("2a9470bc61314187b19d7190b76cd535", "Super Ball", "32574");
INSERT INTO trends VALUES("c9773e2bb68647039a7a40c2ee7d4716", "Zara", "4458796");


-- ##############################

-- ##############################

SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id ORDER BY RANDOM() LIMIT 5;

DROP VIEW IF EXISTS users_by_name;
CREATE VIEW users_by_name AS SELECT * FROM users ORDER BY user_name DESC;

SELECT * FROM users_by_name LIMIT 1;


-- JOIN command and test it for all users and tweets
-- Create the view that contains the join command
-- The name of the view is: users_and_tweets
SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;
DROP VIEW IF EXISTS users_and_tweets;
CREATE VIEW users_and_tweets AS SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;
SELECT * FROM users_and_tweets;

DELETE from tweets WHERE 
