CREATE TABLE blah (
  id          INTEGER PRIMARY KEY NOT NULL,
  title       TEXT,
  cover       TEXT,
  author      TEXT,
  category    TEXT,
  description TEXT,
  score TEXT,
  download_epub    TEXT,
  download_mobi    TEXT,
  download_txt    TEXT,
  url         TEXT,
  spider      TEXT,
  date        TEXT
);
CREATE UNIQUE INDEX blah_url_uindex ON blah(url)