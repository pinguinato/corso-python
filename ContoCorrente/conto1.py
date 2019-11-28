# La Classe ContoCorrente

class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto

class ContoCorrente(Conto):
    # inizializzatore
    def __init__(self, nome, conto, importo):
        # dalla superclasse
        super().__init__(nome, conto)
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


# Gestore di Conti Conrrenti - classe chd non istanzia
class GestoreContiCorrenti():
    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        print("\nEffettua un bonifico di € " + str(importo))
        sorgente.preleva(importo)
        destinazione.deposita(importo)

# testing

c1 = ContoCorrente('Roberto', '123456', 1000)
c1.descrizione()

c2 = ContoCorrente('Stefania', '4567', 2500)
c2.descrizione()

GestoreContiCorrenti.bonifico(c1, c2, 500)

c1.descrizione()

c2.descrizione()