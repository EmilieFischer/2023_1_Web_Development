DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id              TEXT,
    username        TEXT,
    name            TEXT,
    last_name       TEXT,
    total_followers TEXT,
    total_following TEXT,
    total_tweets    TEXT,
    avatar          TEXT,
    PRIMARY KEY(id)
) WITHOUT ROWID;


INSERT INTO users VALUES("3658fee36e88469b90ba6490bd52422c", "elonmusk", "Elon", "Musk", "128900000", "177", "22700", "3658fee36e88469b90ba6490bd52422c.jpg");
INSERT INTO users VALUES("d4c66eb4aa3342d2b1dff4c39bee7003", "shakira", "Shakira", "", "53700000", "235", "7999", "d4c66eb4aa3342d2b1dff4c39bee7003.jpg");
INSERT INTO users VALUES("07a08c8b225f4713a8b427f7de39f67d", "rihanna", "Rihanna", "", "107900000", "980", "10600", "07a08c8b225f4713a8b427f7de39f67d.jpg");