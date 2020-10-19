import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.testdb

todo_collection = db.todos

todo_collection.create_index([("titolo", pymongo.ASCENDING)])
todo_collection.create_index([("descrizione", pymongo.ASCENDING)])

# menu principale dell'applicazione
def application_menu():
    print("\n")
    print("\t\t---------------------")
    print("\t\t* * * TODO LIST * * *\n\n")
    print("\t\t|0| Esci dal programma\n")
    print("\t\t|1| Nuovo Todo\n")
    print("\t\t|2| Lista tutti i Todo\n")
    print("\t\t|3| Modifica un Todo\n")
    print("\t\t|4| Elimina un Todo\n")
    print("\t\t---------------------")

# fa i listing di tutti i task presneti nella collection
def list_all_todos():
    print("\nElenco dei task da fare oggi:\n")
    all_todos = todo_collection.find({})
    for todo in all_todos:
        print(todo) 

# crea un nuovo document e lo inserisce nella collection
def create_new_todo():
    print("\nCrea il tuo task...\n")
    titolo = str(input("\nInserisci il titolo del task: "))
    descrizione = str(input("\nInserisci la descrizione del task: "))
    new_todo = {"titolo": titolo, "descrizione": descrizione}
    todo_collection.insert_one(new_todo)
    print("\nTask inserito nella lista...\n")

# cancella il primo elemento della collection
def delete_a_todo():
    todo_collection.delete_one({})
    print("\nTask rimosso dalla lista.\n")
    
