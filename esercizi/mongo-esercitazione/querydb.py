import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.testdb # se non c'è il db lo crea, se esiste si connette

persone_collection = db.persone

p = persone_collection.find_one() # leggo il primo documento nel db persone

print(p)

query = persone_collection.find({"computer": "msi"}) # query che richiede tutte le persone che posseggono un computer msi

print("* * *")

for persona in query:
    print(persona)

print("* * *")