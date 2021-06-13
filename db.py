import pymongo
from pymongo.collection import Collection

class c_mongo(object):
    def __init__(self):
        self.client=pymongo.MongoClient(host="localhost",port=27017)
        self.db_data=self.client["douguo"]

    def insert_item(self,item):
        db_douguo=Collection(self.db_data,'douguo_table')
        try:
            # 批量插入数据,ordered=False
            db_douguo.insert(item)
        except pymongo.errors.DuplicateKeyError as e:
            # 获取插入成功的数据量
            return


db_douguo_mongo=c_mongo()
