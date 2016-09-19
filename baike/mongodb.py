# mongodb test

from pymongo import MongoClient

class mongo:
    # init db

    def get_db(dbname):
        client = MongoClient('mongodb://localhost:27017/')
        db = client[dbname]
        return db

    # init collection

    def get_collection(db, col):
        collection = db[col]
        return collection

    # create

    def create_data(db, col, data):
        collection = db[col]
        insert_id = collection.insert(data)
        return insert_id

    # read

    def read_data(db, col):
        collection = db[col]
        for data in collection.find({}):
            print data

    # update
    def update_data(db, col, old_data, new_data):
        collection = db[col]
        result = collection.replace_one(old_data, new_data)
        return result

    # delete

    def delete_data(db, col, data):
        collection = db[col]
        result = collection.delete_one(data)
        return result

# for test

# db = get_db('baike')
# id = create_data(db, 'crawed', {"url": "http://nba.hupu.com"})
# print id
# read_data(db, 'crawed')