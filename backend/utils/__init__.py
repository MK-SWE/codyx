from utils.db import DBStorage
from utils.cache import Cache


STORAGE = DBStorage()
STORAGE.reload()

CACHE= Cache('localhost', 6379, 0)
