class MyClass:
    def __new__(cls, message):
        istanza = super(MyClass, cls).__new__(cls)
        print("++++ Creata istanza e ritorno ++++")
        return istanza

    def __init__(self, message):
        self.message = message
        print("++++ Sono in INIT ++++")
        print(self.message)


mc = MyClass("Python")


class MyClassSenzaMessage:
    def __new__(cls):
        istanza = super(MyClassSenzaMessage, cls).__new__(cls)
        return istanza

    def __init__(self):
        print("Init senza message")


mcsm = MyClassSenzaMessage()
