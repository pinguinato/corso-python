'''
Esempio di utilizzo di un filtro su query in MongoDB
Autore: Gianotto Roberto
'''

import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.testdb 
persone_collection = db.persone

print("****")
persona = persone_collection.find_one({"nome": {"$gt": "Mario"}})
print(persona)