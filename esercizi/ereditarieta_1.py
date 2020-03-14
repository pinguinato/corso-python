class SuperClasse:
    a = 10

class SottoClasse(SuperClasse):
    print("Sono la SottoClasse e stampo a che ho ereditato da SuperClasse => ", SuperClasse.a)

prova = SottoClasse()

print("Sono la SottoClasse, ho creato una istanza prova e richiamo a  ==> ", prova.a)
