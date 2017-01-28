CREATE TABLE taiwanebook (
  id          INTEGER PRIMARY KEY NOT NULL,
  title       TEXT,
  rename TEXT,
  author      TEXT,
  cover       TEXT,
  publication TEXT,
  publisher TEXT,
  year TEXT,
  edition_number TEXT,
  pages TEXT,
  accession_number TEXT,
  isbn TEXT,
  source TEXT,
  pre_organization TEXT,
  category    TEXT,
  download   TEXT,
  url         TEXT,
  spider      TEXT,
  date        TEXT
);
CREATE INDEX taiwanebook_url_index ON taiwanebook(url)