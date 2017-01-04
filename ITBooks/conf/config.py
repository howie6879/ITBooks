import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Add ITBooks to path
sys.path.append(os.path.dirname(BASE_DIR))

# DATABASE
DATABASE_DIR = os.path.join(BASE_DIR, 'database')
SQLITE_FILE = os.path.join(os.path.join(DATABASE_DIR, 'sqlite'), 'books.db')
SQLITE_TABLE = 'allitebooks'
