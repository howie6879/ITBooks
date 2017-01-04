"""abook

Usage:
  abook.py search <title> <author>
  abook.py title <title>
  abook.py author <author>
"""
from docopt import docopt
from GetITBooks import GetITBooks


def cli():
    kwargs = docopt(__doc__)
    title = kwargs.get('<title>', None)
    author = kwargs.get('<author>', None)
    get_book = GetITBooks()
    get_book.search_book(title, author)


if __name__ == "__main__":
    cli()
