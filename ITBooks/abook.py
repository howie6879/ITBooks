"""abook

Usage:
    abook.py search <title> <author>
    abook.py title <title>
    abook.py author <author>

Examples:
    abook.py search Mastering+Python Hattem
"""
from docopt import docopt
from console import Console


def cli():
    kwargs = docopt(__doc__)
    title = kwargs.get('<title>', None).replace('+', ' ') if kwargs.get(
        '<title>', None) else None
    author = kwargs.get('<author>', None).replace('+', ' ') if kwargs.get(
        '<author>', None) else None
    console = Console()
    console.search_book(title, author)


if __name__ == "__main__":
    cli()
