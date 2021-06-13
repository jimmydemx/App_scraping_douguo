import pymongo
from pymongo.collection import Collection

class c_mongo(object):
    def __init__(self):
        self.client=pymongo.MongoClient(host="localhost",port=27017)
        self.db_data=self.client["douguo"]
        self.db_douguo=Collection(self.db_data,'douguo_table')

    def insert_item(self,item):
        try:
            # eliminate duplicated entries
            self.db_douguo.insert(item)
        except pymongo.errors.DuplicateKeyError as e:
            
            return
            
    
  

db_douguo_mongo=c_mongo()
