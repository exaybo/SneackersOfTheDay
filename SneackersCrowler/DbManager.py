from pymongo import MongoClient
import LoadAttempt
import bson

class CDbManager(object):
    _instance = None
    _client = None
    _db = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.__init__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._client =  MongoClient("host.docker.internal", 27017)
        self._db = self._client.sneackers_db

    def GetAttempts(self):
        return list(self._db.attempts.find())

    def GetSneackers(self):
        return list(self._db.sneakers.find())
    
    def SaveAttempt(self, attempt):
        self._db.attempts.insert_one(attempt)
        
    def SaveSneakers(self, sneakerList):
        #self._db.sneakers.insert_many(sneakerList)
        for snk in sneakerList:
            self._db.sneakers.update_one({"Uri": snk["Uri"]},
                                         {"$set": snk},
                                         upsert = True)
    


