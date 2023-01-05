from pymongo import MongoClient

config={
    "host":"localhost",
    "port":27017,
    "username":"",
    "password":""
}

class Connection:
    def __new__(cls, database=None):

        connection=MongoClient(**config)

        if database is None:
            return connection

        return connection[database]

