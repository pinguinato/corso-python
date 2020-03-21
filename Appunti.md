#Corso di Python
##0.1.1 Come funziona un programma
Un programma rende un computer usabile. 
Un computer è in grado di eseguire operazioni molto semplici ma è in grado di farlo in modo molto veloce e farlo ripetutamente.
Il linguaggio è la parola chiave, possiamo dire al computer cosa fare, passandogli le informazioni che servono per produrre un risultato.

##0.1.2 Linguaggio naturale vs linguaggio macchina
Il linguaggio è un mezzo per esprimere e memorizzare pensieri.
Il linguaggio macchina è molto rudimentale. Il computer risponde solo a un set di comandi conosciuti.
I comandi riconosciuti sono molto semplici. 
Un set completo di comandi è chiamato <b>Instruction List (IL)</b>.<br/>
Ogni linguaggio è formato dai seguenti elementi:
<li>un alfabeto: insieme di simboli usati per costruire parole</li>
<li>un lessico o dizionario: insieme di parole che il linguaggio offre ai suoi utilizzatori</li>
<li>una sintassi: un insieme di regole usate per definire se una stringa di parole forma una frase valida</li>
<li>una semantica: un insieme di regole che definisce se una frase ha senso</li>
I linguaggi di programmazione di alto livello sono un ponte tra il linguaggio macchina e il linguaggio umano.
Sono scritti dagli umani e comprensibili dalla macchina per essere tradotti in linguaggio macchina.<br/>
I programmi scritti in questi linguaggi vengono chiamati <b>source code</b> e i file contenenti questo codice sono chiamati <b>source file</b>

##0.1.3 Compilazione vs Interpretazione
Una volta scelto il linguaggio di programmazione, il programmatore dovrà scrivere un programma che rispetti il linguaggio scelto per i quattro
elementi indicati nel precedente paragrafo: alfabeto, lessico, sintassi e semantica. Altrimenti il 
programma non sarà completamente usabile.<br/>
Una volta scritto il programma esso dovrà essere tradotto in linguaggio macchina.
Questa traduzione verrà fatta dalla macchina e può essere fatta in 2 modalità, tramite la compilazione
o tramite l'interpretazione:
<li>compilazione: il programma viene tradotto una volta producendo un file contenente il codice macchina, questo file può essere distribuito.
Il programma che effettua questa traduzione si chiama compilatore o traduttore.</li>
<li>interpretazione: chi usa il codice effettua la traduzione ogni volta che lo esegue. L'interprete 
interpreta il codice ogni volta che lo esegue.</li>
Ci sono però linguaggi che sono sia compilati che interpretati.<br/>
Il codice sorgente è un file di testo puro, non deve essere arricchito da font, colori o immagini.<br/>
L'interprete legge il file dall'alto verso il basso e da sinistra verso destra. <br>
Come prima cosa verifica che il codice sia scritto correttamente a livello dei 4 punti che definiscono un linguaggio
(alfabeto, lessico, sintassi e semantica), se trova degli errori ferma la sua traduzione e lancia l'errore. <br>
Successivamente, se non ha trovato errori, l'interprete esegue il codice linea per linea, read-check-execute viene eseguito anche più volte per ogni riga perchè ogni riga è eseguita
separatamente.è quindi possibile che prima che venga trovato un errore in esecuzione l'interprete abbia già eseguito gran parte del codice.
<br>
<b>Python è un linguaggio interpretato.</b><br>
I linguaggi interpretati vengono anche chiamati linguaggi di scripting.<br>
Vantaggi dei linguaggi interpretati:
<li>Puoi eseguire il codice appena completato, non ci sono tempi aggiuntivi di traduzione</li>
<li>Il codice è memorizzato usando il linguaggio di programmazione non in linguaggio macchina, quindi può
essere eseguito su qualsiasi macchina e non deve essere compilato separatamente per le diverse architetture.</li>
Vantaggi dei linguaggi compilati:
<li>l'esecuzione del codice tradotto è spesso più veloce</li>
<li>l'utente finale non deve avere il compilatore per eseguire il codice</li>
<li>il codice tradotto è in linguaggio macchina quindi difficilmente comprensibile e può quindi rimanere segreto.</li>
Svantaggi dei linguaggi interpretati:
<li>L'esecuzione del codice non sarà molto veloce in quanto dovrà spartire le risorse della macchina con l'interprete/li>
<li>Programmatore e utente devono avere il compialtore</li>
Svantaggi dei linguaggi compilati:
<li>La compilazione può occupare tempo e quindi magari bisognerà aspettare un po' prima di eseguire il codice</li>
<li>Devi avere tanti compilatori per quante architetture vuoi tradurre il tuo codice</li>

## 0.3.3 Cython
Traduce il codice scritto in Python in C in modo da rendere più veloce l'esecuzione.

## 0.3.4 Jython
Python tradotto in Java quando si è in ambienti con infrastruttura Java.

IDLE è l'acronimo di Integrated Development and Learning Environment

I file scritti in Pyhton devono avere l'estensione .py

## 1.1.2 La funzione print()
Una funzione è una parte di codice a sè stante in grado di:
<li>causare degli effetti</li>
<li>valutare uno o più valori</li>
molte funzioni in Python possono essere in grado di fare entrambe le cose.
<br>Le funzioni possono provenire da:
<li>Python stesso, queste funzioni vengono chiamate built-in</li>
<li>Moduli Python, vanno installati</li>
<li>Possiamo scrivere noi delle funzioni nel nostro codice</li>
Una funzioni può quindi avere un effetto o un risultato (o entrambi).<br>
Un altro componente importante delle funzioni sono gli argomenti (da 0 a n argomenti)<br>
Quando invochiamo una funzione: print("Buongiorno") cosa fa Python:
<li>Controlla che quella funzione esista</li>
<li>Controlla che gli sia passato il corretto numero di parametri</li>
<li>Passa il controllo alla funzione che viene eseguita, causa effetti se ce ne sono, 
ritorna valori se deve farlo</li>
<li>una volta finita la sua esecuzione ritorna il controllo al chiamante</li>
<br>
In Python in una riga di codice ci deve essere una unica istruzione. Una riga può essere vuota
ma non può contenere più di una istruzione.

## 1.1.11 Escape character
Il carattere \ è l'escape character fa in modo che il carattere che segue venga interpretato in modo diverso. <br>
Per esempio \n fa andare a capo. Se vogliamo stampare solo il \ dobbiamo raddoppiarlo. Non tutti i caratteri dopo il backslach hanno un significato.

## 1.1.14 funzione print() chiamata con più argomenti
Se passiamo più argomenti alla funzione print, essa stamperà a video un elemento dopo l'altro nella stessa linea separati da uno spazio.
<br>I parametri sono passati in modo posizionale, ma ci sono alcuni parametri della print che possono essere passati per nome (keyword arguments)<br>
Uno di questi è end. Viene passato dopo i parametri posizionali e viene seguito da = e il suo valore: <br>

    print("My name is Python", end = " ")
    print("Monthy Python")

Il keyword argument end va a sostituire il carattere finale aggiunto dalla print alla fine della sua esecuzione con lo spazio, invece del valore di default
\n
<br>
Un altro keyword argument è sep, se lo indichiamo andremo a sostituire il separatore di default dei parametri 
passati alla print (lo spazio).

    print("My name","is","Python",sep="-")
Il risultato sarà: My name-is-Python<br>
Possiamo usare insieme nella stessa invocazione della funzione i 2 keyword argument.

##1.2.1 Literal
Un literal è un dato il cui valore è determinato dal literal stesso. <br>
123 è un literal. Una variabile c non lo è perchè non sappiamo quale sia il suo valore senza informazioni aggiuntive.

## 1.2.3 Literal - integer
I computer gestiscono i numeri in 2 tipi:
<li>Integer: numeri senza la parte frazioria</li>
<li>Floating point: numeri che contegono la parte frazionaria</li>
Il computer li memorizza in modo differente e cambia anche il range dei loro valori accettabili.<br>
La forma del literal definisce il tipo con cui Python memorizza il dato.<br>
Un integer può essere indicato solo scrivendo numeri, per renderlo più leggibile possiamo
introdurre gli underscore come separatore di migliaia:<br>
1111111 oppure 11_111_111 che è più leggibile ed è accettato da Python.<br>
Possiamo indicare un numero negativo ponendo davanti al numero il meno: -111.<br>
I numeri positivi non hanno bisogno di anteporre il + ma comunque è permesso.<br><br>
Python permette di rappresentare i numeri interi in base ottale: 0o123. Numero preceduto da 0O oppure 0o. <br>
Numeri in base 8 vuol dire che possiamo rappresentare un numero usando i numeri da 0 a 7.<br>
print(0o123) vale 87. Print fa la conversione del numero e lo restituisce in base 10.<br>
Python permette anche di rappresentare i numeri esadecimali: 0x123 vale 291. Anche qui print restituisce il suo valore base 10.

## 1.2.8 Literal - floating point
I numeri floating point possono rappresentare la parte frazionaria e vengono così scritti: 4.0 5.2. La parte frazionaria è dopo il punto.<br>
Si può omettere lo 0 se è l'unico numero prima o dopo il punto: 0.4 -->.4<br>
4 è un integer 4.0 o 4. è un floating point, Python li memorizza in maniera diversa. Il punto lo fa diventare un floating point<br>
Si possono scrivere i floating point usando l'esponente e 3e8 è come dire 3 * 10^8.<br>
L'esponente deve essere un intero, la base può essere un intero. Per numeri molto piccoli possiamo usare la notazione E con un numero negativo:<br>
6.62607E-34 --> 6.62607 * 10^-34<BR>
Python usa la notazione che crede sia più economica per la rappresentazione dei numeri:<br>
print(0.0000000000000000000001) stamperà 1e-22 <br>

## 1.2.20 Literal - string
Le stringhe si scrivono all'interno di "" oppure ''<br>

## 1.2.22 Literal - boolean
True e False

## 1.3.2 Operatori
un operatore è un simbolo del linguaggio di programmazione che è in grado di fare operazioni su 2 valori.<br>
Dati e operatori sono connessi tramite le espressioni. L'espressione più semplice è un literal stesso.

## 1.3.3 Operatori aritmetici - esponenziale
L'esponenziale è denotato dal doppio asterisco. A sinistra la base, a destra l'esponenziale:<br>
3 ** 2<br>
Quando entrambi gli elementi sono integer, il risultato è un integer. Se almeno uno è un float, il risultato
sarà un float.<br>
<li>2 ** 3 = 8</li>
<li>2. ** 3 = 8.0</li>
<li>2 ** 3. = 8.0</li>
<li>2. ** 3. = 8.0</li>

 ## 1.3.5 Operatori aritmetici - moltiplicazione
 E' denotata dall'asterisco, segue le stesse regole dell'esponenziale per il tipo del risultato.
 
 ## 1.3.5 Operatori aritmetici - divisione
 E' denotata dallo slash /. Il risultato è sempre un float

## 1.3.5 Operatori aritmetici - divisione intera
E' denotata dal doppio slash //. Da' il risultato intero della divisione. Segue le regole della moltiplicazione e dell'esponenziale
per il tipo restituito. Il risultato è sempre arrotondato per difetto, all'intero più piccolo.
<li>3 // 2 = 1</li>
<li>3.0 // 2 = 1.0 etc...</li>
<li>-6 // 4 = -2</li>
<li>6. // -4 = -2</li>

## 1.3.18 Operatori aritmetici - modulo
E' denotato dal %. Restituisce il resto della divisione. Segue le regole della moltiplicazione per il tipo restituito.

## 1.3.19 Divisione per zero
La divisione per zero restituisce un errore, quindi non eseguire divisione, divisione intera o modulo per zero.<br>

## 1.3.21 Operatori aritmetici - somma
E' denotata dal segno +. Segue le regole della moltiplicazione per il tipo del risultato.

## 1.3.25 Binding degli operatori con stessa priorità
Nella maggior parte dei casi il binding degli operatori con la stessa priorità viene fatto da
sinistra verso destra.<br>
Eccezione fa l'esponenziale per cui il binding viene fatto da destra verso sinistra.

## 1.3.30 Lista delle priorità
operatori unari + e -
esponenziale **
moltiplicazione divisione e modulo * / // %
somma e sottrazione + e -

Usando le parentesi possiamo dare noi la priorità che vogliamo alle espressioni.

## 1.4.1 Variabili
Una variabile può memorizzare il valore di una espressione.
Una variabile deve avere un nome e un valore.<br>
Regole per il nome di una variabile:
<li>Può contenere lettere maiuscole e minuscole, numeri e _</li>
<li>Python è case sensitive quindi lettere maiuscole e minuscole sono trattate come caratteri differenti</li>
<li>Il nome di una variabile non può iniziare con un numero</li>
<li>_ è un carattere, quindi una variabile può iniziare con esso</li>
<li>Il nome di una variabile non può essere una parola chiave di Python</li>
Python permette di usare i caratteri dei diversi alfabeti quindi possiamo chiamare una variabile quantità<br>


Le variabili possono contenere un qualsiasi valore dei tipi che abbiamo trattato e anche di altri
non ancora visti. Una variabile può prima contenere un integere, poi un float e infine può anche diventare una stringa.<br>
L'assegnazione fa diventare la variabile di quel tipo. Per creare una variabile dobbiamo darle un nome e assegnarle un valore.

variabile = 10

Non si può usare una variabile che non esiste, questo causa un errore in esecuzione.

## 1.4.13 Shortcut operator
x = x + 2 --> x += 2

y = y * 2 --> y *= 2

variabile = variabile op operation --> variabile op= operation

x = x ** 2 --> x **= 2

## 1.5.1 funzione input()
La funzione input permette di leggere un valore inserito dall'utente nella console e a ritornare il valore 
al programma che l'ha richiamata. La funzione fa passare la console in input mode, una volta
che viene inserito un valore e viene schiacciato il tasto invio, il valore immesso viene restituito 
al programma chiamante che può salvarlo e poi manipolarlo a patto che venga salvato in una variabile, se no viene perso.

La funzione input restituisce una stringa. Se viene inserito un numero e proviamo a farci delle operazioni
aritmetiche riceveremo un errore. 

Per risolvere questo problema possiamo utilizzare 2 semplici funzioni che ricevendo una stringa come argomento
restituiscono un integere o un float. Queste 2 funzioni sono int() e float()

## 1.5.10 Operatori sulle stringhe
Gli operatori + e * possono manipolare anche le stringhe.
+ l'operatore + concatena stringhe, ma devono essere entrambe stringhe altrimenti dà errore
+ l'operatore * moltiplica le stringhe, moltiplica per un intero, "James"*2 = "JamesJames"

Una funzione che possiamo applicare sulle stringhe è str() accetta un numero e dà sempre come risultato la rappresentazione in stringa del numero.
Non darà mai errore.

## 2.1.4 Uguaglianza
Per verificare se 2 valori sono uguali dobbiamo usare l'operatore == che restituisce True o False.

2 == 2 --> True
2 == 2. --> è anch'esso True perchè Python riesce a capire che hanno lo stesso valore anche sesono 2 tipi 
differenti. Converte l'integer in float.

## 2.1.12 Lista delle priorità aggiornata
+ unari + e -
+ esponenziale**
+ moltiplicazione divisione e modulo * / // %
+ somma e sottrazione + e -
+ < <= > >=
+ == != 

## 2.1.14 Condizioni ed esecuzione condizionale
    if condizione:
        fai_qualcosa

    if condizione:
        fai_se_e_vera
    else:
        altrimenti_fai_questo
        
La condizione è valutata vera se è diversa da 0, è valutata falsa se è uguale a 0.

Esiste anche gli if a cascata che possiamo scrivere con if elif else:

    if condizione:
        fai_passo_1
    elif condizione2:
        fai_passo_2
    elif condizione3:
        fai_passo_3
    else:
        passo_else
Se l'if e l'else contengono una unica istruzione Python ci permette di scrivere così:

    if condizione: fai_questo
    else: fai_questaltro
    
## 2.2.1 Looping your code with while
    while condizione_vera:
        fai_questo
finchè la condizione del while sarà vera le istruzioni al suo interno saranno ripetute.

## 2.2.12 Looping your code with for
    for i in range(100):
        #do something
        pass # questa è una keyword, non fa nulla è stata messa perchè 
             # nel for ci deve essere almento una istruzione
i è la variabile di controllo del ciclo for. range è una funzione che restituisce una lista di numeri 
da 0 a 99.

range() accetta solo interi come parametri e genera delle sequenze di numeri.

range(first,last) genera una sequenza di numeri da firt incluso a last escluso.

range(first,last,increment) genera una sequenza di numeri da first incluso a last escluso incrementando
di increment


range(2,8,3) --> genera una sequenza contenente 2 e 5.

    for i in range(1,1):
        print("valore di i",i)
Non stampa niente perchè il risultato di range è vuoto. Per restituire qualcosa la range deve avere il secondo parametro maggiore
del primo, se no non restituisce niente.
     
     for i in range(2,1)
        print("valore di i",i)
Anche in questo caso no viene stampato nulla.

## 2.2.22 Gli statement break e continue
Questi statement vengono chiamati syntactic sugar o syntactic candy, non migliorano il linguaggio ma possono essere utili al
programmatore.

break fa uscire immediatamente dal ciclo.

continue fa saltare direttamente alla iterazione successiva del ciclo senza eseguire le istruzioni ad esso successive nel body
del loop.

## 2.2.24 else nei cicli
sia il while che il for ammettono come l'if lo statement else, le istruzioni al suo interno verranno eseguire una volta
indipendentemente se il ciclo viene eseguito o meno. Se viene eseguito il ciclo l'else verrà fatto alla fine, se il ciclo
non viene eseguito l'else viene eseguito comunque. Non è molto utilizzato.

## 2.3.1 Logica del computer
Quando usiamo un and parliamo di congiunzione (conjunction), quando usiamo l'or parliamo di disgiunzione (disjunction)

L'or ha priorità minore rispetto all'and (come il + con *)

L'operatore di negazione è not (che è unario)

not (a and b) == (not a) or (not b)

not (a or b) == (not a) and (not b)

Non possiamo usare questi operatori nella forma abbreviata op=

## 2.3.9 Bitwise operators
Operatori logici bit a bit. Sono and or xor e not: & | ^ tilde è not

questi operatori accettano solo interi non possono essere usati con i float.

questi operatori possono essere scritti nella forma abbreviata x = x & y --> x &= y

## 2.3.21 Shifting
l'operatore di shifting << e >> può essere applicato solo ad interi

<< è come la moltiplicazione per 2 di un numero shifta a sinistra di un bit 

invece >> shifta a destra quindi divide per 2 un numero

    var = 17
    varRight = var >> 1
    varLeft = var << 2

varRight = 17 // 2 --> 8

varLeft = 17 * 2 * 2 = 68

## 2.2.14 Alcune operazioni sulle liste
Creazione di una lista
    lista = [1,2,3,4]

in questo modo abbiamo creato una lista. Possiamo accedere ai sui elementi tramite gli indici:

print(lista[1]) --> verrà stampato l'elemto in posizione 1 ossia il 2 perchè gli indici della lista
partono da 0. Non possiamo accedere a un elemento delle lista che non esiste.

per esempio print(lista[4]) darà errore

possiamo usare indici negativi print(lista[-1]) stamperà l'ultimo elemento di una lista.
anche qui attenzione a non acecere a posizioni inesistenti.

cancellare elementi di una lista del lista[1] cancellerà l'elemento della lista nella posizione 1.

possiamo aggiungere un elemento al fondo della lista usando il metodo append:

lista.append(6)  --> aggiungerà il numero 6 alla fine della lista.

Per aggiungere un elemento in una determinata posizione della lista useremo il metodo insert che prevede
2 parametri:

lista.insert(where, what)

lista.insert(1,8) inserirà il numero 8 in posizione 1 e shifterà a destra gli elementi seguenti.

Scambio di valore di 2 variabili:

variabile1, variabile2 = variabile2, variabile1

## 2.6.1 Liste

Il nome di una variabile scalare è il nome della variabile stessa.

Il nome di una lista è il nome del posto in memoria in cui è memorizzata

list2 = list1 copia il nome della lista non il suo contenuto.

list1 e list2 identificano la stessa locazione nella memoria del computer.

per assegnare a una lista il contenuto o parte del suo contenuto ad un'altra lista possiamo
usare lo slice, che restituisce una lista nuova, una copia del suo contenuto non del suo nome.

list2 = list1[:]

list[start:end]

restituirà una nuova lista contenente gli elementi della lista iniziare dall'indice start compreso e end escluso.

è possibile usare anche indici negativi come per l'indicizzazione.

Se nello start indichiamo un indice che è successivo all'end allora la lista restituita sarà
vuota.

Se omettiamo lo start, viene inteso che verrà copiata la lista dall'elemento 0.

list[:end]  è equivalente a list[0:end]

Se omettiamo l'end viene inteso che verrà copiata da start fino alla fine della lista.

list[star:] è equivalente a list[start:len(list)]

Se si vogliono eliminare più elementi in una lista possiamo usare lo slice che in questo caso non 
produce una nuova lista.

del list[2:5] cancellerà gli elementi della lista dall'indice 2 al 4 compreso

se vogliamo cancellare tutti gli elementi della lista:

del list[:]

Se invece si vuole proprio cancellare la lista:

del list

in questo modo la lista non esisterà più e se proveremo a fare print(list) avremo un errore.

## 2.6.14 L'operatore in
L'operatore in permette di verificare se un elemento è presente in una lista. Se presente ritorna True.

elem in list

L'operatore not in verifica se un elemento non è presente nella lista. Se non presente restituisce True.

elem not in list

## 2.7.1 Liste dentro liste
Liste che contengono liste. Abbiamo visto fino ad ora liste che contengono scalari. 

una lista però può contenere liste come elementi. Potremmo quindi creare una matrice.

List comprehension è una modalità di popolare liste al volo, vediamo la notazione:

list = [i for i in range(8)]

dove i è il dato usato per popolare la lista, il for specifica quante volte il dato sarà presente 
nella lista.

lista = [5 for i in range(8)] creerà una lista con 8 elementi con il valore 5.

altri esempi:

squares = [x**2 for x in range(10)] --> rappresenterà il quadrato dei numeri da 0 a 9.

un esempio un po' più interessante:

odds = [x for x in squares if x % 2 != 0] --> lista che conterrà i numeri dispari contenuti nella lista
squares

possiamo creare matrici con la list comprehension

matrix = [[i for i in range(8)] for j in range(8)]

la prima parte (parantesi quadre più interne) costruisce la riga. la parte esterna costruisce la matrice
quindi ripeterà la riga le volte richieste(8)

Le coordinate per accedere alla matrice sono riga,colonna

## 3.1.5 Funzioni
Le funzioni in Python possono essere principalmente di 3 tipi:
+ funzioni di Python, sono native in Python, per usarle basterà invocarle. Es: print()
+ funzioni di moduli preinstallati in Python, sono funzioni un po' meno usate di quelle built-in
ma pur sempre molto utili, per utilizzarle bisognerà fare un passo in più (si vedrà dopo)
+ funzioni scritte da noi.

Sintassi per definire una funzione:

    def nome_funzione():
        istruzioni

All'interno di una funzione ci deve essere almeno una istruzione.

Basterà poi chiamare la funzione in questo modo:

    nome_funzione()

Quando una funzione viene invocata, Python va a cercare la sua definizione, la esegue e una volta
eseguita torna dove era stata chiamata per eseguire le istruzioni successive.

L'invocazione di una funzione va sempre fatta dopo la sua definizione. Python legge il codice
dall'alto verso il basso.
Se invochiamo la funzione prima della sua definizione ci verrà ritornato un errore.

    def message():
        print("Enter a message")
    
    message = 1

Questa porzione di codice è errata, anche se non darà errore, però non potrà più essere chiamata 
la funzione message perchè non sarà più disponibile perchè ora message è diventata una variabile
siccome gli abbiamo associato un numero.

## 3.2.1 Funzioni con parametri
I parametri esistono solo all'interno delle funzioni, vengono dichiarati all'interno delle parentesi
della definizione delle funzioni. Gli vengono passati dei valori quando la funzione viene chiamata.

differenza tra parametri e argomenti: i parametri sono definiti e esistono all'interno della funzione.
gli argomenti sono i valori che vengono passati alla funzione quando viene richiamata ed esistono al di fuori della
funzione.

Dovremmo passare tanti argomenti alla funzione quanti parametri sono definiti.

Al di fuori della funzione possiamo definire delle variabili con lo stesso nome dei parametri della funzione.
Ma all'interno della funzione verrà sempre utilizzato il parametro, questo fenomeno si chiama shadowing.

Passaggio posizionale dei parametri funzione(a,b,c) --> funzione(1,2,3):

ad a sarà associato 1, a b 2 a c 3. Il passaggio è quindi posizionale.

un'altra modalità per passare i parametri è keyword argument passing, cioè passiamo gli argomenti 
per nome. in questo modo possiamo non rispettare l'ordine dei parametri:

    funzione(c=2,a=1,b=3)
    
se scriviamo il nome di un parametro che non esiste riceveremo un errore.

Possiamo anche mischiare le 2 modalità con la regola che prima vanno passati per posizione e successivamente per nome.

    funzione(1,c=2,b=3)
    
il primo argomento che è posizionale verrà associato al primo parametro che è a. Gli altri 
2 sono per nome.

Si possono indicare dei parametri di default in modo che durante l'invocazione della funzione
possano essere omessi e quindi venga preso il valore di default. Il valore di default va indicato in
fase di definizione della funzione:

    def funzione(a,b,c=0):
        print(a+b+c)

Potremmo quindi richiamare la funzione non passando l'argomento c:

    funzione(1,3)

## 3.3.2 return
La parola chiave return può essere utilizzata all'interno di una funzione e ha 2 differenti
utilizzi:
+ se non è seguita da nulla fa terminare la funzione nel punto in cui è indicata e quindi ritorna 
il controllo al chiamante
+ se è seguita da una espressione fa terminare la funzione e in più valuta l'espressione e 
ritorna il suo risultato al chiamante della funzione

None è una parola chiave, rappresenta nessun valore. Non può essere utilizzata in espressioni
per esempio non possiamo usarla come operatore in un'addizione.

Si può solo usare per assegnare il valore a una variabile o per paragonarla:

    variabile = None
    if variabile == None:
        print("La variabile non ha nessun valore")
        
Se una funzione non ritorna nessun valore, implicitamente ritorna None.

## 3.4.1. Scope
Lo scope di un nome (per esempio il nome di una variabile) è la parte di codice dove il nome è
correttamente riconoscibile.

Per esempio lo scope di un parametro di una funzione è la funzione stessa, il parametro è inaccessibile
al di fuori della funzione.

L'esempio sottostante dà errore:

    def funzione():
         x = 123
    
    funzione()
    print(x)

la x nella print non è riconosciuta, la x ha lo scope interno alla funzione e non può essere
utilizzata al di fuori.

Una variabile che è stata creata al di fuori di una funzione può essere usata all'interno della 
funzione.

    def funzione():
        print("Valore della variabile",x)
    
    x = 123
    funzione(x)
    print(x)

La situazione seguente è leggermente diversa:
    
    def funzione():
        x=2
        print("Valore della variabile",x)
    
    x = 123
    funzione(x)
    print(x)

il risultato sarà:

    Valore della variabile 2
    123
    
La variabile x creata all'interno della funzione non è la stessa che è stata definita all'esterno
sembrano 2 variabili con lo stesso nome. La variabile interna alla funzione offusca quella che è
stata creata fuori con lo stesso nome.

Una variabile esistente al di fuori di una funzione, ha lo scope anche all'interno della funzione
eccetto per quelle variabili che vengono ridefinite con lo stesso nome all'interno della funzione.

Questo significa anche che lo scope di una variabile esistente al di fuori di una funzione è
supportato solo quando leggiamo il suo valore. L'assegnazione di un valore forza la creazione di una variabile
interna alla funzione.

Con la parola chiave global cambiano le cose. Se vogliamo che una variabile definita al di fuori di una 
funzione mantenga il suo scope anche all'interno della funzione, potendo quindi oltre che leggerla
anche assegnarle dei valori, possiamo definire la variabile all'interno della funzione
come global, in questo modo sia dentro che fuori la funzione la variabile sarà la stessa e Python
non ne creerà un'altra all'interno della funzione.

    def funzione():
        global x
        x=2
        print("Valore della variabile",x)
    
    x = 123
    funzione(x)
    print(x)
    
il risultato sarà:

    Valore della variabile 2
    2

parametri e argomenti. Come sappiamo per gli scalari se passiamo un valore come argomento
la funzione modificherà il valore del parametro ma non dell'argomento.

    def prova(variabile):
        print("Avevo",variabile)
        variabile += 1
        print("Ora ho",variabile)
    
    variabile = 1
    prova(1)
    print(variabile)

il risultato sarà:

    Avevo 1
    Ora ho 2
    1

Per le liste:

    def provaListe(lista):
        print(lista)
        lista = [1,2]
    
    L = [2,3]
    provaListe(L)
    print(L)

Il risultato sarà:

    [2,3]
    [2,3]

In questo caso non cambia per le liste

Un esempio diverso per vedere i comportamenti diversi sulle liste:

    def provaListe(lista):
        print(lista)
        del lista[0]
    
    L = [2,3]
    provaListe(L)
    print(L)

Il risultato sarà:

    [2,3]
    [3]

Questo caso è diverso perchè non modifichiamo il parametro ma il contenuto della lista.

Se l'argomento è una lista e cambiamo il valore del parametro corrispondente non modifichiamo la lista
ma se cambiamo una lista indetificata dal parametro la lista riflette le modifiche.

##3.6.1 Sequenze e mutabilità
Le sequenze in python sono un tipo di dati che possono contenere 0 o più elementi su cui si può
scorrere tramite un ciclo for.

Per mutabilità si intendono tipi di dati il cui contenuto può cambiare nel tempo, per esempio nelle liste
possiamo aggiungere o rimuovere elementi.

Tipi di dati immutabili sono le tuple, una volta definito il suo contenuto non si può modificare.

Come creare una tupla:

    tupla = (1,2,3,4)
    tupla = 1., .5, 2.25, 4.0
    
Possiamo crearle all'interno di parentesi tonde oppure solo con gli elementi separati da virgole

tupla vuota:

    tupla = ()
    
tupla con un elemento:

    tupla = (1)
    tupla = 1.,
    
Per accedere agli elementi delle tuple utilizziamo la notazione usata per le stringhe:

    print(tupla[0])
    print(tupla[1:3])
    print(tupla[:2])
    print(tupla[1:])
    print(tupla[-1])
    for el in tupla:
        print(el)

Non si può modificare il contenuto di una stringa, riceveremmo un errore:

    tupla.append(2)
    del tupla[1]
    tupla[0] = 10

Possiamo concatenare le tuple tramite l'operatore +, ci restituirà una nuova tupla risultato
della concatenazione delle 2.

Non possiamo modificare il contenuto della tupla con operazioni in situ tipo quelle che 
abbiamo elencato sopra, ma possiamo invece fare quanto segue:

    tupla1 = (1,2,3)
    tupla2 = (4,5,6)
    tupla2 = tupla1+tupla2

Questo perchè andiamo ad assegnare alla variabile tupla2 una nuova tupla. Questo è concesso.

Sulle tuple possiamo usare la funzione len() come per le liste, così come possiamo usare gli operatori + * in e not in
così come li usiamo per le liste.

## 3.6.11 Dizionari
I dizionari sono delle strutture mutabili e non sequenziali ma che possono essere adattate semplicemente
a processi sequenziali.

Un dizionario è un insieme di coppie chiave-valore con le seguenti caratteristiche:
+ la chiave deve essere unica
+ la chiave può essere di qualsiasi tipo
+ un dizionario non è una lista, la lista è un elenco di valori ordinati, il dizionario è un insieme
di coppie chiave-valore
+ la funzione len() funziona anche per i dizionari e restituisce il numero di coppie key-value contentute in esso
+ il dizionario è uno strumento a senso unico, possiamo ricercare con solo la chiave e non per valore

Un dizionario può essere creato come segue:

    englishFrench = {'cat':'chat', 'dog':'chien', 'lion':'leon'}
    rubricaTelefonica = {'Roby':3341234456, 'Marta':320998877565}
    vuoto = {}

chiave e valore possono essere di qualsiasi tipo. il dizionario è delimitato dalle parentesi graffe.
le coppie sono divise da virgole e chiave e valore da i 2 punti.

Se poi stiampiamo i dizionari non è detto che l'ordine sia quello con cui abbiamo inserito, questo perchè
i dizionari non sono strutture ordinate, il loro ordine è gestito in autonomia da Python.

Come accedere ai valori di un dizionario:

    englishFrench['cat'] #cat è la chiave e verrà così restituito il valore corrispondente
    rubricaTelefonica['Roby']
    
Non possiamo accedere a valori di chiavi che non esistono, riceveremo un errore:

    rubricaTelefonica['Stefy']
    
Non esiste la chiave Stefy quindi verrà lanciato un errore.

Per evitare queste situazioni possiamo usare la parola chiave in

    nome = 'Stefy'
    if nome not in rubricaTelefonica:
        print(nome, 'Non presente nella rubrica telefonica')
        
Con delle funzionalità dei dizionari possiamo usare i for.

Il metodo keys() ritorna una lista contenente le chiavi del dizionario così possiamo effettuare un loop su tutte le chiavi del
dizionario.

    for key in dict.keys():
        print('chiave',key,' valore ->',dict[key])

possiamo anche ordinare una lista ritornata usando la funzione sorted:

    for key in sorted(dict.keys()):
        print('chiave',key,' valore ->',dict[key])

un altro metodo dei dizionari è il metodo items() esso ritorna una lista di tuple, ogni tupla 
contiene la coppia (chiave,valore)

Il metodo values() lavora in modo similare al metodo keys(), ritorna però una lista di valori.
Siccome dal valore non possiamo risalire alla chiave la sua funzionalità è limitata.

Possiamo associare un altro valore a una chiave:

    rubrica['Roby'] = 3207234635
    
Anche aggiungere una nuova coppia chiave valore è molto semplice, è come la modifica, basta indicare una chiave non esistente

Per eliminare una coppia chiave-valore usiamo l'istruzione del

    del rubrica['Roby']
    
## 4.1 I moduli
La gestione dei moduli consiste di 2 possibili problematiche:
+ l'utilizzo  di un modulo, quindi noi siamo gli utenti (user) - uso di un modulo già esistente
+ la creazione di un modulo che possa essere usato da noi o da altri, quindi noi siamo i fornitori (supplier) - creazione da 0 di un nuovo modulo

### 4.1.3 Come usare i moduli
Un modulo è identificato da un nome. Per usare un modulo bisogna conoscere il nome. Molti moduli sono rilasciati da Python.
Tutti questi moduli, insieme alle funzioni built-in, formato la Python standard library.

Ogni modulo consiste di entità, le entità possono essere funzioni, variabili, classi, costanti o oggetti.

Se si sa come accedere a un modulo allora si potranno usare le entità in esso contenute.

Per poter usare un modulo bisogna importarlo, utilizzando la parola chiave <b>import</b>

    import math
    
La riga sopra importa il modulo math di Python. L'import possiamo richiamarlo ovunque nel codice
ma va sempre messo prima di utilizzare le sue entità.

Per importare più di un modulo possiamo o ripetere l'import specificando l'altro modulo oppure separando i vari moduli 
con la virgola per una unica istruzione di import

    import math,sys
    
namespace: è uno spazio in cui esistono alcuni nomi univoci.

Se un modulo esiste, quindi esiste il suo nome può essere importato. Tutti inomi definiti nel modulo
diventano conosciuti. Ma non entrano nel namespace del tuo file. Questo vuol dire che possiamo
definire una funzione chiamata sim o un a variabile pi senza che vengano influenzate dall'import.
Per far riferimento a sim e pi del modulo math dobbiamo anteporre il nome del modulo.

    math.sin
    math.pi
In questo modo abbiamo palesato il namespace di questi 2 oggetti, se definiamo degli oggetti con lo stesso nome
non c'è nessun conflitto.

    import math
    print(math.sin(1/math.pi))

Se togliamo il math. davanti ai 2 nomi il codice sarà errato.

Vediamo un esempio per vedere che il namespace di math e il nostro possono coesistere:

    import math
    def sin(x):
        if 2*x == pi:
            return 0.999999
        else:
            return None
    
    pi = 3.14
    print(sin(pi/2))
    print(math.sin(math.pi/2))
    
il risultato sarà:

    0.999999
    1
    
Le entità nostre e del modulo math non si influenzano.

Possiamo invece importare delle singole entità da un modulo, solo quelle indicate, a cui possiamo
accedere senza il qualificatore del modulo

    from math import pi
    
Importiamo solo l'entità pi del modulo math e potremo riferirci ad essa senza usare il qualificatore math.
Se proviamo a far riferimento ad altre entità del modulo math che non abbiamo importato riceveremo un errore.

    from math import sin,pi
    
    print(sin(pi/2))
    
Se successivamente ridefiniamo le due entità sin e pi nel nostro namespace allora esse saranno sovrascritte.

    from math import pi, sin

    print(sin(pi/2))

    pi = 3.14
    def sin(x):
        if 2 * x == pi:
            return 0.999999
        else:
            return None
    
    print(sin(pi / 2))
    
L'output sarà:

    1.0
    0.999999
    
Vediamo quindi che la ridefinizione delle 2 entità nel nostro namespace sovrascrive quelle importate.

Se invece invertiamo le cose, vediamo che la sovrascrittura funziona nel modo inverso, quindi viene sovrascritto il precedente 
dalla definizione successiva.

    pi = 3.14
    def sin(x):
        if 2 * x == pi:
            return 0.999999
        else:
            return None
    
    print(sin(pi / 2))
    
    from math import pi,sin
    print(sin(pi / 2))
    
Il risultato sarà:

    1.0
    0.999999
    
possiamo inoltre importare tutte le entità di un modulo e usarle senza identificatore, questo però non è sempre utile
perchè se ridefiniamo una entità sovrascriveremo quella del modulo. E' meglio non usare questa modalità

    from module import *
    
Possiamo anche dare un'alias al modulo, mentre verrà importato verrà rinominato in modo che possiamo fare riferimento
ad esso con questo suo nuovo nome.

    import module as newname
    
as è una parola chiave.

Una volta fatto l'alias non possiamo più accedere al nome originale del modulo

    import math as M
    
    print(M.sin(M.pi/2))
    
Possiamo anche rinominare le singole entità importate

    from module import entity as newName
    
    from module import n as a, m as b, o as c
    
Una volta rinominate il nome originale sarà inaccessibile.

## 4.2.1 Lavorare con i moduli standard
Introduciamo la funzione dir(), come parametro si aspetta un modulo che deve essere precedentemente
importato con la import (from module non basta), la funzione dir(module) ci restituirà l'elenco delle entità
presenti all'interno del modulo in ordine alfabetico. Se abbiamo dato un alias al modulo dobbiamo usarlo.

    dir(math)
    
Il risultato dalla console di Python (in un programma non ha senso e non restituisce niente...)

    ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 
    'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 
    'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 
    'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 
    'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 
    'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 
    'tan', 'tanh', 'tau', 'trunc']
    
Da programma possiamo stamparle:
    
    import math
    
    for name in dir(math):
        print(name)

Il modulo random ha varie funzioni per il calcolo di numeri pseudo casuali.
random() chiamata senza argomenti restituisce un float da 0 a 1

    from random import random, seed
    
    seed(0)
    print(random())
    
Numeri interi random randrange(begin, end, step) --> end escluso

randint(begin,end) --> end incluso

Altre 2 funzioni del modulo random:

    from random import choice, sample
    
choice vuole che argomento una sequence, per esempio una lista con degli argomenti al suo interno.
Restituirà un elemento preso a "caso" da questa lista.

sample invece vuole 2 parametri in entrata (il secondo è opzionale e il default vale 1), il primo sarà
una lista il secondo il numero di elementi da scegliere. Restituirà quindi una lista di n elementi (dipende dal secondo parametro)
scelti dalla lista passata come primo parametro. Senza ripetizioni.

Il modulo platform può darci informazioni riguardo il sistema operativo in uso, hardware etc...

    from platform import platform

La funzione platform ci dà indicazioni riguardo al sistema operativo in uso. In base ai parametri
passati ci presenta le informazioni in modo diverso

    from platform import platform

    print(platform())
    print(platform(1))
    print(platform(0,1))

    Windows-10-10.0.18362-SP0
    Windows-10-10.0.18362-SP0
    Windows-10
    
platform(aliased=False, terse=False)
+ aliased: se passato a 1 può presentare nomi di livelli sottostanti alternativi invece dei soliti 
+ terse: se possibile rappresenta il nome in modalità più breve

La funzione machine() del modulo platform restituisce una stringa contenente il nome generico del processore della macchina.

La funzione processor() restituisce il nome effettivo del processore.

La funzione system() ritorna il nome generico del sistema operativo

La funzione version() restituisce la versione del sistema operativo.

Per conoscere invece la versione di Python che stiamo usando, sempre dal modulo platform:

+ python_implementation() restituisce l'implementazione di Python (tipo CPhyton)
+ python_version_tuple(): restituisce una tupla contenente major part della versione,
minor part della versione e la patch.

## 4.3 Creare un modulo
Possiamo creare noi dei moduli, è bene dare un nome intuitivo al modulo e inserire funzioni
che siano dello stesso argomento. Si può poi raggruppare più moduli in package.

Creiamo un modulo chiamato module.py nella stessa cartella creiamo un file main.py nel quale
scriveremo l'istruzione import module.

Nella cartella dove abbiamo creato il modulo è stata creata una cartella __pycache__ dove al
suo interno ci sarà un file chiamato module.cpython-xy.pyc dove xy sono la versione quindi
nel nostro caso il file si chiamerà module.cpython-38.pyc.

Il nome del file ha il nome del modulo, nel nostro caso module.

nel modulo possiamo fare riferimento alla variabile __name__

Se eseguiamo il modulo verrà stampato __main__  (queso perchè la stiamo stampanto dall'interno del modulo)
se eseguiamo il main verrà stampato module

Possiamo quindi usare la variabile "__name__" per distinguere se stiamo eseguendo il modulo oppure se lo abbiamo
importando e stiamo eseguendo le sue funzioni dall'esterno.

Come convenzione una variabile interna al modulo il suo nome è preceduto da 1 o 2 underscore
Questa è solo una convenzione, in questo modo diciamo che la variabile può essere letta ma non scritta.

Nella prima riga di un modulo possiamo indicare una stringa particolare che può sembrare un commento ma che in realtà
è molto utile se l'ambiente è connesso a un server. Si chiama hashbang, per gli ambienti Linux e Unix like indica come eseguire il
contenuto del file, cioè quale file deve essere lanciato per interpretare il testo 

    #!/usr/bin/env python3

Un'altra stringa importante è doc-string che è una descrizione di cosa fa il modulo, può essere multi linea, per la documentazione:

    """ module.py - un esempio di modulo Python """

Nel modulo sys è presente la variabile path che è una lista che contiene l'elenco delle cartelle in cui
viene cercato un modulo quando si chiama la import. Il primo file che troverà con il nome del modulo da importare sarà importato.
Quindi se ce ne fossero altri in altre cartelle con lo stesso nome saranno ignorati.

Python è in grado di cercare anche negli zip, li vede come delle cartelle normali.

possiamo aggiungere il path del nostro modulo 

    from sys import path
    
    path.append("..\\modules")
    
    import modules
    
Il path relativo funziona se il nostro programma main.py si trova nella cartella home e 
la cartella modules è dentro la nostra home, se così non fosse, tipo il programma main.py si trovasse
in una sottocartella dovremmo indicare il path assoluto.

Invece di usare l'append  possiamo usare una path.insert(0,"\\modules")

L'aggiunta del path naturalmente va fatta prima di importare il modulo.

## Package
Per creare un package, visto che non è un file fisico come i moduli, dobbiamo creare un file
\__init.py__

Dove potremmo inserire l'inizializzazione oppure lasciarlo vuoto.

Può essere inserito nella root del progetto oppure anche nelle sottocartelle se 
alcune parti del package hanno bisogno di un trattamento o di una inizializzazione particolare.

## 4.4 Le eccezioni
Ogni volta che il programma farà qualcosa di sbagliato Python fermerà il programma e creerà
un tipo di dato chiamato Eccezione --> __raising and exception__

Quando il programma incontra un errore, in Python possiamo essere in grado di catturare e gestire l'eccezione
in modo che il programma sia ripreso e continui la sua esecuzione.

Questo può essere fatto perchè i nomi delle eccezioni non sono ambigui in modo che possiamo 
categorizzarle e reagire appropriatamente.

Esempio di eccezioni che abbiamo incontrato:

    ValueError
    ZeroDivisionError
    IndexError

Per gestire le eccezioni c'è la parola chiave __try__

    try:
        azione_che_puo_dare_errore
    except:
        azione_da_fare_se_errore
    azione_successiva_al_blocco
    
Appena viene trovata una eccezione nel blocco di codice tra try e except l'esecuzione salta
alla prima riga di codice nel blocco except, quindi alcune istruzioni dentro il try potrebbero
essere omesse.

Possiamo anche intercettare diversi tipi di eccezioni se per esempio nel blocco della try
è possibile che vengano lanciate più tipi di eccezioni

    try:
        :
    except exc1:
        :
    except exc2:
        :
    except:
        :

I rami dell'except vengono ricercati nell'ordine in cui sono stati scritti, non possiamo scrivere più
rami except con lo stesso tipo di eccezione, possiamo mettere quanti except vogliamo, 
l'importante e che ci sia un try seguito da un except (senza o con tipo di eccezione specifico).

Non possiamo usare except senza try, se viene eseguito un ramo except nessun altro ramo except viene 
eseguito. Se nessun except sa gestire l'eccezione, l'eccezione rimane ingestita. Se c'è un ramo con un
except senza tipo di eccezione deve essere messo come ultimo ramo.

L'ordine dei branches è importante, quindi non bisogna mettere prima eccezioni più generali di quelle + concrete, questo farebbe
diventare queste ultime non raggiungibili e inutilizzabili. Il nostro codice sarebbe disordinato e 
inconsistente. Python non genererà nessun errore rispetto a questa problematica.

possiamo gestire diversi tipi di eccezione insieme:

    try:
        :
    exception (exc1, exc2):
        :

In una funzione le eccezioni possono essere gestite al suo interno oppure all'esterno.

L'eccezione se non gestite dalla funzione o dal suo chiamante viene propagata oltre i loro confini
fino a quando qualcuno non sia in grado di gestirla, Nel caso non venga gestita da nessuno il programma sarà
terminato.

la parola chiave raise lancia l'eccezione come se fosse provocata naturalmente, può servire
per testare il codice e vedere come è stata gestita.

    def prova(x):
        raise ZeroDivisionException
    
    try:
        prova(0)
    except ArithmeticError:
        print("Eccezione")

L'output sarà:
    
    Eccezione

Possiamo anche utilizzare raise da sola ma solo all'interno di un except così verrà lanciata
l'eccezione che è stata catturata precedentemente

    def prova(x):
        try:
            return x/0
        except:
            print("Lancio l'eccezione")
            raise
            
    try:
        prova(5)
    except ArithmeticError:
        print("Catturo l'eccezione")

L'output sarà:

    Lancio l'eccezione
    Catturo l'eccezione
    
Un'altra parola chiave importante è assert. Essa viene seguita da un'espressione.

    assert expression

L'espressione viene valutata, se restituisce un valore vero, uno stringa non vuota o un numero
diverso da 0 è valutata come vera, altrimenti lancia una eccezione AssertionError.

Quando può essere usata? Quando vogliamo essere sicuri che i dati immessi siano corretti
e che i dati vengano esaminati prima di essere utilizzati. L'AssertionError assicura che il 
nostro codice non produca dati errati e ci dice chiaramente la natura dell'errore.

Le asserzioni non sostituiscono le eccezioni o la validazione dei dati, sono un qualcosa in più.

### 4.6.2 ArithmeticError
Eccezione concreta che si presente per errori di tipo artimetico, tipo la divisione per zero o 
per il dominio sbagliato di un argomento.

BaseException <-- Exception <-- ArithmeticError

### 4.6.2 AssertionError
Eccezione concreta che si presenta quando l'espressione indicata in un assert risulta False, None, 0 o 
stringa vuota.

BaseException <-- Exception <-- AssertionError

### 4.6.3 BaseException
E' l'eccezione più generale (astratta) di Python, include tutte le altre eccezioni.

except:

except BaseException:

sono equivalenti.

###4.6.4 Exception
Eccezione astratta che include tutte le eccezione causate da errori di codice. 

BaseException <-- Exception

###4.6.5 IndexError
Eccezione concreta che si presenta quando ci sono degli errori di accesso nelle sequenze,
quando si cerca di accedere a un indice che non esiste. A un elemento della sequenza che non
esiste

BaseException <-- Exception <-- LookupError <-- IndexError

###4.6.6 KeyboardInterrupt
Eccezione concreta che si presenta quando il programma viene terminato forzatamante con 
la combinazione di tasti Ctr+C

BaseException <-- KeyboardInterrupt

###4.6.7 LookupError
Eccezione astratta che si presenta quando ci si riferisce in modo erroneo alle collezioni tipo
liste dizionari tuple etc..

BaseException <-- Exception <-- LookupError

### 4.6.8 MemoryError
Eccezione concreta che si presenta quando un'operazione non può essere terminata per mancanza di
memoria libera

BaseException <-- Exception <-- MemoryError 

### 4.6.9 OverflowError
Eccezione concreta che si presenta quando un'espressione produce un valore troppo grande 
per essere memorizzato nella variabile a cui si sta assegnando.

BaseException <-- Exception <-- ArithmeticError <-- OverfolwError

### 4.6.10 ImportError
Eccezione concreta che si presenta quando un'operazione di import fallisce (import di un modulo).

BaseException <-- Exception <-- StandardError <-- ImportError

### 4.6.11 KeyError
Eccezione concreta che si presenta quando proviamo ad accedere a un elemento della 
 collezione che non esiste (per esempio nei dizionari)
 
BaseException <-- Exception <-- LookupError <-- KeyError

### 4.7 Caratteri e stringhe vs. computer
Ogni cattere è codificato con un codice ASCII, numeri, lettere, caratteri speciali,
caratteri non visibili (a capo). Ognuno ha un codice univoco che lo identifica, il codice è un
valore numerico.

Per esempio il codice ascii del carattere spazio è 32, quello della A 65 e quello di a è
97

The world internationalization è abbreviato con I18N.

Un __code point__ è un numero che produce un carattere. Il codice ASCII standard quindi condiste
di 128 checkpoint.

I rimanenti 128 caratteri (questo perchè un carattere viene salvato in 8 bit) possono essere
usati per rappresentare i restanti caratteri di una lingua.

Code page è uno standard che permette di usare i 128 caratteri rimanenti per rappresentare
i caratteri di una specifica lingua. Quindi uno stesso code point può rappresentare caratteri diversi
in diversi code page.

Quindi per conoscere il significato di un code point dobbiamo sapere a che code page si riferisce.
Da questo ne consegue che un code point derivato da un code page è ambiguo.

Entra in giorno lo Unicode che assegna un univoco e non ambiguo carattere a più di un
milione di code points.

UCS-4 usa 32 bit per memorizzare un carattere, e il codice è solo il numero univoco dell'Unidoce code
points.

UCS-4 è più dispendioso (4 volte in più dello standar ASCII) ma fortunatamente ci sono dei metodi
forme più intelligenti per codificare il testo unicode.

UTF-8 usa quanti bit gli servono per rappresentare un code points. Non ha bisogno del BOM come invece ha
bisogno UCS-4.

Python supporta sia unicode che UTF-8. Python è completamente I18Ned

### 4.8 La natura delle stringhe
len() ritorna la lunghezza di una stringa, ossia il suo numero di caratteri. il carattere
"\\" di escape non è incluso nel conteggio della lunghezza.

la funzione ord() ha come parametro un carattere e resttuisce il suo codice ascii code point value.
se non gli passiamo un carattere riceveremo un TypeError

La funzione chr() a fronte di un code point restituisce il carattere che rappresenta. 
Se gli passiamo un argomento non valido potrà restituire un ValueError (se passiamo un numero
che non è un code point valido) oppure un TypeError se non passiamo un numero.

Le stringhe sono delle sequences. Possiamo quindi accedere a un singolo carattere della stringa
con gli indici

    stringa = "stringa di prova"
    for x in len(stringa):
        print(stringa[x])

Gli indici negativi funzionano e non possiamo fare riferimento a indici che non esistono.

Iterare in una stringa è possibile:

    for x in stringa:
        print(x)
        
Anche lo slice funziona:

    print(stringa[3:7])

Anche l'operatore in funziona:

    print('tr' in stringa)
    print('s' in stringa)
    print('S' in stringa)
    
Anche l'operatore not in funziona:

    print('o' not in stringa)
    
Le stringhe sono immutabili.

L'operatore del non può essere utilizzato liberamente nelle stringhe:

    del stringa[3]
    
Ci darà errore. del possiamo usarlo unicamente per cancellare la stringa.

    del stringa
    
Non esiste quindi nemmeno il metodo append, così come non esiste il metodo insert.

funzione min sulle stringhe: passando una stringa come parametro restituisce il carattere con il valore ascii minimo,
restituisce il valore minimo della sequenza:

    print(min("aAzghI"))
    
Stamperà A perchè ha il code point minore (vedi tabella codici ascii)

Min può essere usata anche su liste. si comporterà in modo differente.

max() invece restituirà il valore massimo della sequenza. Per la stringa precedente stamperà z

Metodo index() delle sequence, è un metodo, restituisce l'indice della prima occorrenza dell'elemento
cercato.
L'elemento cercato deve esistere nella sequenza, altrimenti verrà restituito un errore ValueError.

La funzione list() passandogli come parametro una stringa, restituisce una lista contente i caratteri
della stringa, uno per indice.

Il metodo count() prende come parametro un carattere e restituisce il numero di occorrenze di querl
carattere nella stringa. Se il valore passato non è presente nella stringa non restituirà errori ma ritornerà 0.

    print(stringa.count('b'))
    
### 4.9 Metodi delle stringhe

    print('abDc'.capitalize())

Il metodo capitalize ritornerà una stringa (ricorda che la stringa su cui chiamiamo il metodo
non viene modificata perchè le stringhe sono immutabili) il cui primo carattere (se è una lettera)
sarà maiuscolo e tutti gli altri saranno minuscoli. Il metodo può essere chiamato sia da una variabile
che da un literal.

    print('alpha'.center(10))
    
Il metodo center ritorna una stringa centrata all'interno di un campo di un certo numero di
caratteri (passato come parametro).
Quindi aggiungerà a destra e a sinistra della stringa degli spazi in modo da centrarla.
Se il numero che viene passato come parametro è minore della lunghezza della stringa, verrà ritornata la stringa 
stessa.

Il metodo può essere chiamato anche con un secondo parametro, possiamo passargli un carattere, in questo modo riempirà
gli spazi a destra e a sinistra per centrare la stringa con il carattere passato come secondo argomento:

    print('['+'gamma'.center(11,'*')+']')
    
Stamperà:

    [***gamma***]
    
Senza il secondo parametro:

    [   gamma   ]

Il metodo endswith restituisce True o False rispettivamente se la stringa su cui lo si richiama
termina con la sottostringa passata come parametro;

    if 'provafine'.endswith('ine'):
        print('yes')
    else:
        print('no')
Il metodo find cerca una sottostringa all'interno di una stringa, se non la trova ritorna -1 (non va in errore
come l'index), se lo trova invece ritorna l'indice di inizio della sua prima occorrenza

    print('Eta'.find('ta'))

Ritornerà 1 che è l'indice di inizio dove si trova la sottostringa ricercata.
Se dobbiamo ricercare solo un carattere conviene usare la in. find funziona solo con le stringhe
non va utilizzata con le altre sequences.

Il metodo find può essere anche chiamato con un secondo parametro, che indica l'indice di partenza da cui cercare la sottostringa.

    print('kappa'.find('a',2))
    
Ci restituirà l'indice della prima occorrenza della lettera a a partire dall'indice 2 della stringa kappa.

Possiamo anche chiamare la find con un terzo parametro, che indica il primo indice che non deve essere preso
in considerazione per la ricerca

    print('kappa'.find('a',2,4))
    
restituirà -1 perchè la a si trova all'indice 4 che però non viene preso in considerazione.

Il metodo isalnum() verifica che la stringa sia composta solo di numeri o lettere (alfanumerici),
se contiene altri caratteri (anche lo spazio) restituisce False, altrimenti True

    print('lambda30'.isalnum())
    
restituirà True

Il metodo isalpha() invece è molto più restringente, restituisce True solo se la stringa è
composta da sole lettere

    print('Prova3'.isalpha())
    
Restituirà False perchè contiene un numero.

Il metodo isdigit() restituisce True se contiene solo numeri.

Il metodo islower() restituisce True solo se la stringa contiene solo lettere e sono tutte minuscole.

Il metodo isspace() restituisce True solo se la stringa è composta solo da spazi vuoti (può
contenere solo spazi e al massimo tab o a capo)

Il metodo isupper() ritorna True solo se la stringa contiene solo lettere maiuscole.

Il metodo join prevede come argomento una lista che contenga solo elementi di tipo string,
altrimenti dà TypeError. Restiuirà una stringa contenente la concatenazione delle stringhe
contenute nella lista utilizzando come separatore la stringa che richiama il metodo.

In questo esempio il separatore è la virgola:

    print(','.join(['prima','seconda','terza']))
    
Il metodo lower() ritorna una nuova stringa mettendo minuscole tutte le lettere maiuscole 
della stringa che lo invoca

    print('SigMA==60'.lower())
    
L'output sarà:

    sigma==60
    
Il metodo lstrip() restituisce una stringa togliendo gli spazi a sinistra della stringa che la richiama

    print('['+ ' tau '.lstrip()+']')

Ritornerà

    [tau ]
    
Il metodo lstrip con un parametro rimuoverà dall'inizio della stringa i caratteri indicati come parametro:

    print('www.cisco.com'.lstrip('w.'))
    
Ritornerà:

    cisco.com
    
Il metodo replace prevede 2 parametri, sostituirà tutte le occorrenze della sottostringa indicata nel primo parametro 
con quella indicata nel secondo (che può essere stringa vuota quindi rimuoverà la prima, ma il primo parametro
non può essere una stringa vuota)

    print('this is it'.replace('is','are'))
    
Stamperà:

    thare are it

Il terzo parametro della replace indicherà il limite dei rimpiazzamenti, quindi sarà un numero:
    
    print('this is it'.replace('is','are',1))
    
Stamperà:

    thare is it
    
Il metodo rfind() si comporta in modo simile al find, ma inizia a cercare dalla fine della stringa

    print('tau tau tau'.rfind('ta'))
    print('tau tau tau'.rfind('ta',9))
    print('tau tau tau'.rfind('ta',3,9))

Stamperà:

    8
    -1
    4
L'ultimo restituisce 4 perchè l'indice 9 è escluso (la terza a quindi è come se cercasse nella porzione di stringa:
 " tau t")
 
Il metodo rstrip() toglie gli spazi a destra, con un parametro toglie quei caratteri da destra, fa come
lstrip ma dalla parte opposta

Il metodo split() splitta la stringa e restituisce una lista contente le sottostringhe che ha ottenuto.
Splitta la stringa quando trova spazi vuoti (o a capo o tab). E' l'opposto della join.

Il metodo startswith() ci dice se la stringa inizia con una determinata sottostringa:

    print('omega'.stratswith('om'))
    
Il metodo strip() combina gli effetti di lstrip e lrtrip, toglie gli spazi sia a inizio che a fine stringa.

Il metodo swapcase() inverte maiuscolo con minuscolo e viceversa.

Il metodo title() mette maiuscola l'iniziale di ogni parola e il resto minuscolo.

Il metodo upper() fa diventare maiuscole tutte le lettere minuscole contenute nella stringa.

### 4.10 Confrontare stringhe
Possiamo confrontare le stringhe con gli operatori == != > >= < <=

Due stringhe sono uguali quando contengono gli stessi caratteri nello stesso ordine

    'alpha' == 'alpha'
    'alpha' != 'Alpha'
    
entrambi i confronti restituiranno True

    'alpha' < 'alphabet'
    
Restituirà True, questo perchè la seconda è più lunga della prima e la parte iniziale
della seconda coincide con l'intera prima stringa.

    'beta' > 'Beta'
    
Minuscolo è considerato maggiore del maiuscolo per via del suo code point (codice ascii) che è maggiore

Anche se nelle stringhe ci sono numeri, questi vanno considerati come stringhe

    "010" == "10"   #False
    '10' > '010'    #True
    '10' > '8'      #False
    '20' < '8'      #True
    '20' < '80'     #True
    
Non è una buona idea confrontare una stringa con un numero, ma se vogliamo farlo possiamo
usare solo == e != il primo ritornerà sempre False, il secondo sempre True. Gli altri operatori
daranno TypeError

La funzione sorted() riceve come parametro una lista di stringhe e restituisce una nuova lista
contenente gli elementi della prima ordinati.

Il metodo sort() invece ordina gli elementi della lista che lo richiama.

Convertire numeri in stringhe con la funzione str(), ciò è sempre possibile.

Per convertire una stringa in un numero è necessario che la stringa rappresenti un numero,
altrimenti le nostre funzione int() e float() restituiranno un ValueError.

