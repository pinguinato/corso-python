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
    print("\t\t|5| Elimina tutti i Todo\n")
    print("\t\t|6| Lista tutti i Todo solo con solo i valori\n")
    print("\t\t---------------------")

# fa i listing di tutti i task presneti nella collection
def list_all_todos():
    print("\nElenco dei task da fare oggi:\n")
    all_todos = todo_collection.find({})
    print("\nTotale task = ", str(todo_collection.find().count()))
    if(todo_collection.find().count() == 0):
        print("\nNon sono presenti cose da fare oggi...\n")
    else:
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
    if (todo_collection.find().count() == 0):
        print("\nNon ci sono cose da fare oggi, non posso eliminare niente...\n")
    else:
        todo_collection.delete_one({})
        print("\nTask rimosso dalla lista.\n")

# cancello tutti i todo - delete all documents in a collection
def delete_all():
    #verifico che ci siano documenti e se collection vuota non cacello
    if (todo_collection.find().count() == 0):
        print("\nNon ci sono cose da fare oggi, non posso eliminare niente...\n")
    else:
        document_deleted = todo_collection.delete_many({})
        print("\nHo cancellato ", str(int(document_deleted.deleted_count)), " tasks...\n")

# modifica di un todo
def modify_a_todo():
    # TODO: implementare metodo per l'update di un todo
    print("\nModifica di un todo...\n")

# metodo per stampare i singoli campi di un document
def list_all_todos_only_values():
    print("\nElenco dei task da fare oggi:\n")
    all_todos = todo_collection.find({})
    print("\nTotale task = ", str(todo_collection.find().count()))
    for todo in all_todos:
        print("TITOLO: ",todo['titolo'], " DESCRIZIONE: ", todo['descrizione'])

 