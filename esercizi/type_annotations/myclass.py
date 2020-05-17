class MyClass:
    nome: str
    cognome: str

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome


mc = MyClass(nome = "Roberto", cognome = "Gianotto")
print(mc)
print(mc.nome)
print(mc.cognome)