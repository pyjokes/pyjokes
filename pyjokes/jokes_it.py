# -*- coding: utf-8 -*-

"""
Jokes from stackoverflow - provided under CC BY-SA 3.0
http://stackoverflow.com/questions/234075/what-is-your-best-programmer-joke?page=4&tab=votes#tab-top
"""

neutral = [
    "Trionfalmente, Beth ha rimosso Python 2.7 dal server nel 2020.'Finalmente!' ha detto con gioia, solo per vedere l'annuncio di Python 4.4.",
    "Una query SQL entra in un bar, cammina verso a due table e chiede: 'Posso unirvi ?'",
    "Quando il tuo martello e' C ++, tutto inizia a sembrare un pollice.",
    "Se metti un milione di scimmie su un milione di tastiere, uno di loro alla fine scrivera' un programma Java, il resto scrivera' Perl.",
    "Per comprendere la ricorsione devi prima capire la ricorsione.",
    "Gli amici non permettono agli amici di usare Python 2.7.",
    "Ho suggerito di tenere un 'Python Object Oriented Programming Seminar', ma l'acronimo era impopolare.",
    "'toc, toc'. 'Chi e' la'?' ... molto lunga pausa ... 'Java.' ",
    "Quanti programmatori ci vogliono per cambiare una lampadina? Nessuno, e' un problema hardware.",
    "Qual e' il modo orientato agli oggetti per diventare ricchi? Ereditarieta'.",
    "Quanti programmatori ci vogliono per cambiare una lampadina? Nessuno, possono rendere l'oscurita' uno standard.",
    "I vecchi programmatori C non muoiono, sono solo gettati nel void.",
    "Gli sviluppatori di software amano risolvere i problemi: se non ci sono problemi facilmente disponibili li creeranno.",
    ".NET e' stato chiamato .NET in modo che non si visualizzasse in un elenco di directory Unix.",
    "Hardware: la parte di un computer che puoi calciare.",
    "Un programmatore e' stato trovato morto nella doccia, accanto al corpo c'era uno shampoo con le istruzioni:Insapona, risciacqua e ripeti",
    "Ottimista: il bicchiere e' mezzo pieno Pessimista: il bicchiere e' mezzo vuoto Programmatore: il bicchiere e' il doppio del necessario.",
    "In C abbiamo dovuto codificare i nostri bug. In C ++ possiamo ereditarli.",
    "Come mai non c'e' una gara Perl offuscato? Perche' tutti vincerebbero",
    "Se riproduci un CD di Windows all'indietro, ascolterai il canto satanico ... peggio ancora, se lo riproduci in avanti, installa Windows.",
    "Quanti programmatori ci vogliono per uccidere uno scarafaggio? Due: uno tiene, l'altro installa Windows su di esso.",
    "Come si chiama un programmatore finlandese? Nerdic.",
    "Cosa ha detto il codice Java al codice C? : Non hai classe.",
    "Perche' Microsoft ha chiamato il proprio motore di ricerca BING? Because It's Not Google.",
    "I venditori di software e i venditori di auto usate si differenziano perche' questi ultimi sanno quando mentono.",
    "Bambino: 'papa', perche' il sole sorge ad est e tramonta ad ovest?' Papa': 'figlio, sta funzionando, non toccarlo.'",
    "Quanti programmatori Prolog ci vogliono per cambiare una lampadina? Falso.",
    "I veri programmatori possono scrivere codice assembly in qualsiasi lingua.",
    "Cameriere: 'le piacerebbe un caffe' o un te'?' Programmatore: 'Si'.",
    "Un programmatore entra in un foo ...",
    "Qual e' il secondo nome di Benoit B. Mandelbrot? Benoit B. Mandelbrot.",
    "Perche' sorridi sempre? Questa e' solo la mia ... espressione regolare.",
    "Domanda stupida ASCII, ottiene uno stupido ANSI.",
    "Un programmatore aveva un problema: penso' a se stesso: 'lo risolvo con i threads!', ora ha due problemi",
    "Java: scrivi una volta e scappa.",
    "Ti direi una battuta su UDP, ma non lo capiresti mai.",
    "Un ingegnere di QA entra in un bar, si imbatte in un bar, striscia in un bar, balla in un bar, punta i piedi in un bar...",
    "Ho avuto un problema quindi ho pensato di utilizzare Java. Ora ho una ProblemFactory.",
    "L'ingegnere del QA entra in un bar, ordina una birra, ordina 0 birre,  99999 birre, una lucertola, -1 birre, uno sfdeljknesv.",
    "Un responsabile di prodotto entra in un bar, chiede un drink, il barista dice NO, ma prendera' in considerazione l'aggiunta successiva.",
    "Come si genera una stringa casuale? Metti uno studente di Informatica del primo anno davanti a Vim e gli chiedi di salvare ed uscire.",
    "Uso Vim da molto tempo ormai, principalmente perche' non riesco a capire come uscire.",
    "Come fai a sapere se una persona e' un utente Vim? Non ti preoccupare, te lo diranno.",
    "un cameriere urla: 'sta soffocando! Qualcuno e' un dottore?' Programmatore: 'sono un utente Vim.'",
    "3 Database Admins sono entrati in un bar NoSQL e poco dopo sono usciti perche' non sono riusciti a trovare un table.",
    "Come spiegare il film Inception a un programmatore? Quando esegui una VM dentro una VM dentro un' altra VM tutto procede molto lentamente",
    "Come si chiama un pappagallo che dice 'Squawk! Pezzi di nove! Pezzi di nove!' Un errore a pappagallo.",
    "Ci sono solo due problemi difficili in Informatica: invalidazione della cache, denominazione delle cose e errori di off-by-one",
    "Ci sono 10 tipi di persone: quelli che comprendono il binario e quelli che non lo sanno.",
    "Ci sono 2 tipi di persone: quelli che possono estrapolare dati da insiemi incompleti ...",
    "Esistono II tipi di persone: quelli che comprendono i numeri romani e quelli che non li conoscono.",
    "Ci sono 10 tipi di persone: quelli che comprendono l'esadecimale e altri 15.",
    "Ci sono 10 tipi di persone: quelli che capiscono il trinario, quelli che non lo fanno e quelli che non ne hanno mai sentito parlare.",
    "Come chiami otto hobbit? Un hob byte.",
    "La cosa migliore di un booleano e' che anche se ti sbagli, sei solo fuori di un bit.",
    "Un buon programmatore e' qualcuno che guarda sempre in entrambe le direzioni prima di attraversare una strada a senso unico.",
    "Esistono due modi per scrivere programmi privi di errori: solo il terzo funziona.",
    "I controlli di qualita' consistono nel 55% di acqua, 30% di sangue e 15% di ticket in Jira.",
    "Quanti QA servono per cambiare una lampadina? Hanno notato che la stanza era buia,: non risolvono i problemi, li trovano.",
    "Un programmatore si schianta contro un'auto , l'uomo chiede 'cosa e' successo', l'altro risponde'Non so. Facciamo il backup e riprova'.",
    "Scrivere PHP e' come fare pipi' in piscina, tutti lo hanno fatto, ma non hanno bisogno di renderlo pubblico.",
    "Numero di giorni da quando ho riscontrato un errore di indice di array: -1.",
    "gli appuntamenti veloci sono inutili, 5 minuti non sono sufficienti per spiegare correttamente i benefici della filosofia Unix.",
    "Microsoft ha ogni quindici giorni una 'settimana produttiva' dove usa Google invece di Bing. ",
    "Trovare un buon sviluppatore PHP e' come cercare un ago in un pagliaio o e' un hackstack in un ago?",
    "Unix e' user friendly, e' solo molto particolare nella scelta di chi siano i suoi amici.",
    "Un programmatore COBOL guadagna milioni con la riparazione Y2K e decide di congelarsi criogenicamente. L'anno e' 9999. ",
    "Il linguaggio C combina tutta la potenza del linguaggio assembly con tutta la facilita' d'uso del linguaggio assembly.",
    "Un esperto SEO entra in un bar, pub, pub irlandese, taverna, barista, birra, liquore, vino, alcolici, liquori ...",
    "Che cosa significa Emacs ? Utilizzato esclusivamente dagli scienziati informatici di mezza eta'.",
    "Che cosa hanno in comune le battute di PyJokes con Adobe Flash? Si aggiornano sempre, ma non migliorano.",
    "Quanti demosceners sono necessari per cambiare una lampadina? Meta'. Con uno intero non ci sono sfide.",

]


adult = [
    "La programmazione e' come il sesso: un solo errore e devi supportarlo per il resto della tua vita.",
    "Il software e' come il sesso: E' meglio quando e' gratis'.",
    "Il software e' come il sesso: Non e' mai VERAMENTE libero.",
    "Ci sono 10 tipi di persone: quelle che comprendono il binario e quelle che si fanno scopare.",
    "Perche' ai programmatori piace UNIX: unzip, strip, touch, finger, grep, mount, fsck, more, yes, fsck, fsck, fsck, umount, sleep",
    "Tua mamma e' cosi' grassa che nemmeno Dijkstra e' in grado di trovare un percorso piu' breve intorno a lei.",
    "L'unica interfaccia utente intuitiva e' il capezzolo. Dopo hai dovuto imparare tutto.",
    "Qual e' la differenza tra lo sviluppo del software e il sesso? Nel sesso, non si ottiene un bonus per il rilascio anticipato.",
    "Tua mamma e' cosi' grassa che la funzione ricorsiva che calcola la sua massa causa un overflow dello stack.",
]

"""
Jokes from The Internet Chuck Norris DB (ICNDB) (http://www.icndb.com/) - provided under CC BY-SA 3.0
http://api.icndb.com/jokes/
"""

chuck = [
    "Tutti gli array che Chuck Norris dichiara sono di dimensioni infinite, perche' Chuck Norris non conosce limiti.",
    "Chuck Norris non ha la latenza del disco perche' il disco rigido sa sbrigarsi, altrimenti sono guai.",
    "Chuck Norris scrive codice che si ottimizza da solo.",
    "Chuck Norris non puo' testare l'uguaglianza perche' non ha eguali.",
    "Chuck Norris non ha bisogno di garbage collection perche' non chiama .Dispose (), chiama .DropKick ().",
    "Il primo programma di Chuck Norris e' stato kill -9.",
    "Chuck Norris ha scoppiato la bolla delle dot com.",
    "Tutti i browser supportano le definizioni esadecimali #chuck e #norris per i colori nero e blu.",
    "MySpace non e' proprio il tuo spazio, e' di Chuck (te lo lascia solo usare).",
    "Chuck Norris puo' scrivere funzioni infinitamente ricorsive e farle tornare.",
    "Chuck Norris puo' risolvere le Torri di Hanoi in una mossa.",
    "L'unico modello di design che Chuck Norris conosce e' il God Object Pattern.",
    "Chuck Norris ha terminato World of Warcraft.",
    "I project manager non chiedono mai a Chuck Norris le stime.",
    "Chuck Norris non usa gli standard web in quanto il web si conformera' a lui.",
    "'Funziona sulla mia macchina' e' sempre vero per Chuck Norris.",
    "Chuck Norris non fa i grafici di Burn Down, fa i grafici di Smack Down.",
    "Chuck Norris puo' cancellare il cestino.",
    "La barba di Chuck Norris puo' scrivere 140 parole al minuto.",
    "Chuck Norris puo' testare tutte le applicazioni con un'unica affermazione, 'funziona'.",
    "La tastiera di Chuck Norris non ha un tasto Ctrl perche' niente controlla Chuck Norris.",
    "Chuck Norris puo' far traboccare il tuo stack solo guardandolo.",
    "Per Chuck Norris, tutto contiene una vulnerabilita'.",
    "Chuck Norris non usa sudo, la shell sa solo che e' lui e fa quello che gli viene detto.",
    "Chuck Norris non ha bisogno di un debugger, si limita a fissare il codice finché non confessa.",
    "Chuck Norris puo' accedere a metodi privati.",
    "Chuck Norris puo' istanziare una classe astratta.",
    "L'oggetto classe eredita da Chuck Norris.",
    "Per Chuck Norris, NP-Hard = O (1).",
    "Chuck Norris conosce l'ultima cifra del Pi greco.",
    "La connessione di Chuck Norris e' più veloce in up che in down perche' i dati sono più incentivati a correre via da lui.",
    "Nessuna affermazione puo' prendere la ChuckNorrisException.",
    "Chuck Norris puo' scrivere applicazioni multi-thread con un singolo thread.",
    "Chuck Norris non ha bisogno di usare AJAX perche' le pagine hanno troppa paura di postback comunque.",
    "Chuck Norris non usa la riflessione, la riflessione chiede educatamente il suo aiuto.",
    "Non c'e' alcun tasto Esc sulla tastiera di Chuck Norris, perche' nessuno sfugge a Chuck Norris.",
    "Chuck Norris puo' eseguire la ricerca binaria di dati non ordinati.",
    "Chuck Norris non ha bisogno di tentativi di cattura, le eccezioni sono troppo spaventate da sollevarsi.",
    "Chuck Norris e' uscito da un ciclo infinito.",
    "Se Chuck Norris scrive codice con bug, gli errori si risolvono da soli.",
    "L'hosting di Chuck Norris e' garantito al 101% di uptime.",
    "La tastiera di Chuck Norris ha il tasto Any.",
    "Chuck Norris puo' accedere al database dall'interfaccia utente.",
    "I programmi di Chuck Norris non escono mai, sono terminati.",
    "I programmi di Chuck Norris occupano il 150% della CPU, anche quando non sono in esecuzione.",
    "Chuck Norris puo' generare thread che si completano prima di essere avviati.",
    "I programmi di Chuck Norris non accettano input.",
    "Chuck Norris puo' installare iTunes senza installare Quicktime.",
    "Chuck Norris non ha bisogno di un sistema operativo.",
    "Il modello di rete OSI di Chuck Norris ha un solo livello: fisico.",
    "Chuck Norris puo' compilare errori di sintassi.",
    "Chuck Norris non ha bisogno di digitare cast. Il Chuck-Norris Compiler (CNC) vede attraverso le cose, fino in fondo sempre.",
    "Chuck Norris comprime i suoi file c on un calciom rotante sul disco rigido.",
    "Con Chuck Norris P = NP. Non c'e' alcun nondeterminismo con le decisioni di Chuck Norris.",
    "Chuck Norris puo' recuperare qualsiasi cosa da / dev / null.",
    "Nessuno ha mai programmato in coppia con Chuck Norris e ha vissuto per raccontare la storia.",
    "Nessuno ha mai parlato durante la revisione del codice di Chuck Norris e vissuto per raccontare la storia.",
    "Chuck Norris non usa una GUI, preferisce la linea di comando.",
    "Chuck Norris non usa Oracle, lui e' l'Oracle.",
    "Chuck Norris puo' dereferenziare NULL.",
    "Una differenza tra il tuo codice e quello di Chuck Norris e' infinita.",
    "Il plugin Chuck Norris Eclipse e' diventato un contatto alieno.",
    "Chuck Norris e' l'ultimo mutex, tutti i thread lo temono.",
    "Non preoccuparti dei test, i test case di Chuck Norris coprono anche il tuo codice.",
    "Le dichiarazioni del registro di Chuck Norris sono sempre al livello FATAL.",
    "Chuck Norris ha completato World of Warcraft.",
    "Quando Chuck Norris rompe la build, non e' possibile risolverla, perche' non c'e' una sola riga di codice.",
    "Chuck Norris scrive con un dito, lo punta alla tastiera e la tastiera fa il resto.",
    "I programmi di Chuck Norris possono superare il test di Turing fissando l'interrogatore.",
    "Se provi kill -9 con i programmi di Chuck Norris, si ritorce contro",
    "Chuck Norris esegue loop infiniti in meno di 4 secondi.",
    "Chuck Norris puo' sovrascrivere una variabile bloccata.",
    "Chuck Norris conosce il valore di NULL",
    "Chuck Norris puo' installare un sistema operativo a 64 bit su macchine a 32 bit.",
    "Chuck Norris puo' scrivere su un flusso di output.",
    "Chuck Norris puo' leggere da un flusso di input.",
    "Chuck Norris non ha mai scritto il suo programma in codice macchina. Le macchine hanno imparato a interpretare il codice di Chuck Norris.",
    "I test unitari di Chuck Norris non girano, muoiono.",
    "Chuck Norris causa la schermata blu della morte.",
    "Chuck Norris puo' fare una classe che e' sia astratta che finale.",
    "Chuck Norris potrebbe usare qualsiasi cosa in java.util.* per ucciderti, inclusi i javadoc.",
    "Il codice gira piu' velocemente quando Chuck Norris lo guarda.",
    "Chuck Norris non usa REST, lui aspetta.",
    "Su Facebook a tutti piace Chuck Norris, che lo scelgano o no.",
    "Non puoi seguire Chuck Norris su Twitter, perche' lui ti segue.",
    "La calcolatrice di Chuck Norris ha solo 3 tasti: 0, 1 e NAND.",
    "Chuck Norris utilizza solo variabili globali. Non ha nulla da nascondere.",
    "Chuck Norris scrive direttamente in binario. Quindi scrive il codice sorgente come documentazione per altri programmatori.",
]

jokes_it = {
    'neutral': neutral,
    'adult': adult,
    'chuck': chuck,
    'all': neutral + adult + chuck,
}