CREATE TABLE allitebooks (
  id          INTEGER PRIMARY KEY NOT NULL,
  title       TEXT,
  cover       TEXT,
  author      TEXT,
  isbn        TEXT,
  year        TEXT,
  pages       TEXT,
  language    TEXT,
  file_size   TEXT,
  file_format TEXT,
  category    TEXT,
  description TEXT,
  download    TEXT,
  url         TEXT,
  spider      TEXT,
  date        TEXT
);
CREATE INDEX allitebooks_url_index ON allitebooks(url)