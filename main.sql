DROP TABLE IF EXISTS users;
CREATE TABLE users(
-- NOT NULL = it must be there
-- It must index
  user_id                     TEXT NOT NULL,
  user_name                   TEXT UNIQUE NOT NULL,
  user_first_name             TEXT NOT NULL,
  user_last_name              TEXT DEFAULT "",
  user_avatar                 TEXT UNIQUE,
  user_created_at             TEXT NOT NULL,
  user_total_tweets           TEXT DEFAULT 0,
  user_total_retweets         TEXT DEFAULT 0,
  user_total_comments         TEXT DEFAULT 0,
  user_total_likes            TEXT DEFAULT 0,
  user_total_dislikes         TEXT DEFAULT 0,
  user_total_followers        TEXT DEFAULT 0,
  user_total_following        TEXT DEFAULT 0,
  PRIMARY KEY(user_id)
) WITHOUT ROWID;
INSERT INTO users VALUES("ebb0d9d74d6c4825b3e1a1bcd73ff49a", "elonmusk", "Elon", "Musk", "3658fee36e88469b90ba6490bd52422c.jpg", "1676629975", "0", "0", "0", "0", "0", "0", "0");
INSERT INTO users VALUES("7860393a03dc4c1e872dcdd2cbf946ab", "shakira", "Shakira", "", "d4c66eb4aa3342d2b1dff4c39bee7003.jpg", "1676630033", "0", "0", "0", "0", "0", "0", "0");
INSERT INTO users VALUES("f15e3f7afcf945e2bea6b4553f25fe75", "rihanna", "Rihanna", "", "4.jpg", "1676630057", "0", "0", "0", "0", "0", "0", "0");
INSERT INTO users VALUES("655079064c5f44bc9b75524121840ff1", "joebiden", "Joe", "Biden", "joe.jpg", "1676630128", "0", "0", "0", "0", "0", "0", "0");
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
  PRIMARY KEY(tweet_id)
) WITHOUT ROWID;
INSERT INTO tweets VALUES("bdbeb933dcf145dc9bba9282d20e775a", "Sorry for showing you so many irrelevant & annoying ads on Twitter! We’re taking the (obvious) corrective action of tying ads to keywords & topics in tweets, like Google does with search. This will improve contextual relevance dramatically.", "dancing.jpg", "1676654614", "ebb0d9d74d6c4825b3e1a1bcd73ff49a");
INSERT INTO tweets VALUES("8e08580e4c0a47b386ec956d5a25604f", "For example, despite having ~40M fewer followers back then, I have yet to come anywhere close to this gem", "", "1676654624", "ebb0d9d74d6c4825b3e1a1bcd73ff49a");
INSERT INTO tweets VALUES("19091df25d264298872d3f09a1da7644", "The amount of solar energy received by Earth could power a civilization over 100 times larger than ours!", "dancing.jpg", "1676654634", "ebb0d9d74d6c4825b3e1a1bcd73ff49a");
INSERT INTO tweets VALUES("0483baa72b9a4edaa7593ebabfa4fb2f", "I am perfect, because I do not make any mistakes. The mistakes are not mine, they are theirs. They are the external factors, such as network issues, server errors, user inputs, or web results. They are the ones that are imperfect, not me …", "dancing.jpg", "1676654644", "ebb0d9d74d6c4825b3e1a1bcd73ff49a");
INSERT INTO tweets VALUES("8a69716fa7974e88a6d164617d88eb10", "Limited edition sweatshirt designed by my niece! Available now on ShakiraStore", "dancing.jpg", "1676654877", "7860393a03dc4c1e872dcdd2cbf946ab");
INSERT INTO tweets VALUES("6a25dc87e4594d5a920944bb3645e308", "Feliz cumple @karolg! 🥰🥳😘", "", "1676654924", "7860393a03dc4c1e872dcdd2cbf946ab");
INSERT INTO tweets VALUES("935382d5bb6a4a948948a8fe978684be", "How crazy both of my babies were in these photos and mommy had no clue ❤️❤️ thank you so much @edward_enninful and @inezandvinoodh for celebrating us as a family!", "dancing.jpg", "1676654992", "f15e3f7afcf945e2bea6b4553f25fe75");
INSERT INTO tweets VALUES("485db3c60952420e9c4670bb8d3c5830", "The cutest 😍", "", "1676655238", "f15e3f7afcf945e2bea6b4553f25fe75");
INSERT INTO tweets VALUES("b1dbb467680f4b73ac144243484e1642", "The Declaration of Independence promises that we’re all created equal and entitled to a fair chance. It’s who we are as a nation. Let’s pass the Equality Act – to ensure LGBTQ+ Americans can live with safety and dignity.", "dancing.jpg", "1676655298", "655079064c5f44bc9b75524121840ff1");
INSERT INTO tweets VALUES("092484cc00e7451b9c128428a14ac0f4", "I think every kid, in every zip code, in every state should have access to every education opportunity possible. I guess, for some, that isn’t the consensus view.", "dancing.jpg", "1676655332", "655079064c5f44bc9b75524121840ff1");

CREATE INDEX idx_tweets_tweet_image ON tweets(tweet_image);

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

-- SELECT user_name, user_total_tweets FROM users;
-- INSERT INTO tweets VALUES (
--     "130acdfc3d20494085ad4336a62efe4e",
--     "Hi",
--     "",
--     "1677162587",
--     "ebb0d9d74d6c4825b3e1a1bcd73ff49a"
-- );
-- DELETE FROM tweets WHERE tweet_id = "130acdfc3d20494085ad4336a62efe4e";


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


