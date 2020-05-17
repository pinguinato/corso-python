from dataclasses import dataclass

@dataclass
class MyClass:
    nome: str
    cognome: str

mc = MyClass(nome = "Roberto", cognome = "Gianotto")

print(mc)
print(mc.nome)
print(mc.cognome)