CREATE TABLE taiwanebook (
  id          INTEGER PRIMARY KEY NOT NULL,
  title       TEXT,
  cover       TEXT,
  info        TEXT,
  download    TEXT,
  url         TEXT,
  spider      TEXT,
  date        TEXT
);
CREATE INDEX taiwanebook_url_index ON taiwanebook(url)