DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
  full_name       TEXT,
  user_name       TEXT,
  id              TEXT,
  user_fk         TEXT,
  created_at      TEXT,
  message         TEXT,
  message_image   TEXT,
  updated_at      TEXT,
  total_retweets  TEXT,
  total_likes     TEXT,
  total_views     TEXT,
  total_replies   TEXT,
  PRIMARY KEY(id)
) WITHOUT ROWID;

INSERT INTO tweets VALUES(
  "Elon Musk",
  "elonmusk",
  "75544dcd995745ba83557143458a6546", 
  "3658fee36e88469b90ba6490bd52422c",
  "1676283561",
  "My first tweet",
  "2.jpg",
  "0",
  "0",
  "0",
  "0",
  "0"
  );

