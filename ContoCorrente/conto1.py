# La Classe ContoCorrente

class ContoCorrente:
    # inizializzatore
    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
        self.__priv_saldo = importo

    # getter
    @property
    def saldo(self):
        print("sono dentro getter")
        return self.__priv_saldo

    # setter
    @saldo.setter
    def saldo(self, importo):
        print("sono dentro setter")
        self.preleva(self.__priv_saldo)
        self.deposita(importo)

    # prelievo
    def preleva(self, importo):
        self.__priv_saldo -= importo
        print("\nHai prelevato dal conto: " + str(importo))

    # deposito
    def deposita(self, importo):
        self.__priv_saldo += importo
        print("\nHai depositato sul conto: " + str(importo))

    # stampa
    def descrizione(self):
        print("\nIntestatario del conto: " + str(self.nome))
        print("Conto Corrente: " + str(self.conto))
        print("Saldo Conto: " + str(self.__priv_saldo))

# testing

c1 = ContoCorrente('Roberto', '123456', 1000)
c1.descrizione()
c1.saldo = 1000000
print(c1.saldo)