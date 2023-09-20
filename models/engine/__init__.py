#!/usr/bin/python3
"""docujjj"""
from os import getenv
from models.db_storage import DBStorage
from models.file_storage import FileStorage


if getenv("HBNB_TYPE_STORAGE") == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
