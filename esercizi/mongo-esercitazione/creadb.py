import pymongo
from pymongo import MongoClient

# eseguo la connessione con Mongo DB

client = MongoClient('localhost', 27017)

# creo un database

db = client.testdb

# creo la collection persone

persone_collection = db.persone

# creo una serie di indici

persone_collection.create_index([("nome", pymongo.ASCENDING)])
persone_collection.create_index([("cognome", pymongo.ASCENDING)])
persone_collection.create_index([("computer", pymongo.ASCENDING)])

# creo un documento

p1 = {"nome": "Mario", "cognome": "Rossi", "eta": 30, "computer": ["asus", "msi", "acer"]}

# inserisco il documento nella collezione
persone_collection.insert_one(p1)
# inserisco un secondo documento nella collezione
p2 = {"nome": "Roberto", "cognome": "Gianotto", "eta": 42, "computer": ["lenovo", "msi"]}
persone_collection.insert_one(p2)