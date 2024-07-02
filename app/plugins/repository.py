from enum import Enum
from os import getenv
from dotenv import load_dotenv

from pymongo import MongoClient
from pymongo.collection import Collection


class _Collections(Enum):
    POSTS = "posts"


class RepositoryPlugin:
    def __init__(self) -> None:
        load_dotenv()
        self._db = MongoClient(getenv("MONGODB"))["wakre"]

    # 데이터베이스 가져오기 함수
    def getDB(self, name: _Collections) -> Collection:
        if name in _Collections:
            return self._db[name.value]
        else:
            raise ValueError("Invalid collection name")
