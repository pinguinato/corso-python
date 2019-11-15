# La Classe ContoCorrente

class ContoCorrente:
    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
        self.saldo = importo
    def preleva(self, importo):
        self.saldo -= importo
        print("\nHai prelevato dal conto: " + str(importo))
    def deposita(self, importo):
        self.saldo += importo
        print("\nHai depositato sul conto: " + str(importo))
    def descrizione(self):
        print("\nIntestatario del conto: " + str(self.nome))
        print("Conto Corrente: " + str(self.conto))
        print("Saldo Conto: " + str(self.saldo))

contoTest = ContoCorrente('Roberto Gianotto', 'AX123', 100)
contoTest.descrizione()
contoTest.preleva(50)
contoTest.descrizione()
contoTest.deposita(234)
contoTest.descrizione()