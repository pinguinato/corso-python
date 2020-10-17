import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.testdb 
persone_collection = db.persone

query = persone_collection.find({"computer": "msi"})

print("\n-------------------------")

for persona in query:
    print(persona)

print("-------------------------\n")

'''
metodo update_one che serve ad aggiornare un solo documento
$set viene definito un operatore di MongoDB -> gli operatori hanno il carattere $ iniziale, qui vado a modificare l'eta di Mario Rossi
'''
res = persone_collection.update_one({"nome": "Mario"}, {"$set": {"eta": 50} })
p = persone_collection.find_one({"nome":"Mario"}) 
print(p)