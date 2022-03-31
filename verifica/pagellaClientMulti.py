#nome del file : pagellaClientMulti.py

import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4

#Versione 1 
def genera_richieste1(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    #1. Generazione casuale:
    #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
    #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
    #   di un voto (valori ammessi 1 ..10)
    #   delle assenze (valori ammessi 1..5)
    studente= random.randint(1,5)
    cognome=""
    numMateria=random.randint(1,5)
    nomMateria=""
    voto= random.randint(1,10)
    assenze= random.randint(1,5)

    # cognome random
    if studente == 1:
        cognome="Hasanaj"
    elif studente == 2:
        cognome="Gornati"
    elif studente == 3:
        cognome="Fare"
    elif studente == 4:
        cognome="Giamboi"
    else:
        cognome="Peralta"

    # materia random
    if numMateria == 1:
        nomMateria="Matematica"
    elif numMateria == 2:
        nomMateria="Italiano"
    elif numMateria == 3:
        nomMateria="inglese"
    elif numMateria == 4:
        nomMateria="Storia"
    else:
        cognome="Geografia"

    print(cognome + "," + nomMateria + "," + str(voto) + "," + str(assenze))

    #2. comporre il messaggio, inviarlo come json
    #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}
    
    messaggio={'studente':cognome,
    'materia':nomMateria,
    'voto':voto,
    'assenze':assenze}
    
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    
    data=s.recv(1024)
    #print("Risultato: ",data.decode())

    print("Risultato: ",{'studente ':cognome,
    'materia ':nomMateria,
    'valutazione ':"gravemente insufficiente"})

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        s.close()
        #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
    end_time_thread=time.time()
    print(f"{threading.current_thread().name}: Risultato: La valutazione di {cognome} in italiano è Gravemente insufficiente")

#Versione 2 
def genera_richieste2(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

  #....
  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}

    studenti=['Studente0', 'Studentel', 'Studente2', 'Studente3', 'Studente4']
    materie=[ 'Matematica', 'Italiano', 'inglese', 'Storia e Geografia']
    studente=studenti[random.randint(0,4)]
    pagella=()
    for m in materie:
        voto=random.randint(1,10)
        assenze=random.randint(1,5)
        pagella.append((m, voto, assenze))

#2. comporre il messaggio, inviarlo come json
    messaggio={'studente': studente,
    'pagella':pagella}
    print (f"Dati inviati al server {messaggio}")
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    data=data.decode()
    data=json.loads(data)
    print (f"Dati ricevuti dal server (data)")

    if not data:
        print(f"{threading.current_thread().name}:Servernonrisponde.Exit")
    else:
        print(f"{threading.current_thread().name}:Lo studente {data['studente']} ha una media di: {data['media']:.2f} e un totale di assenze: {data['assenze']}")
    s.close()

#3  ricevere il risultato come json {'studente': 'Cognome1', 'media': 8.0, 'assenze': 8}

#Versione 3
def genera_richieste3(num,address,port):
    try:
        s=socket.socket()
        s.connect ((address, port))
        print(f"\n{threading.currentthread().name}{num+1})Connessionealserver:{address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosaèandatostorto,stouscendo...(n")
    sys.exit()

#...
#   #   1. Per ognuno degli studenti ammessi: 5 cognomi a caso scelti da una lista
#   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
#   generazione di un voto (valori ammessi 1 ..10)
#   e delle assenze (valori ammessi 1..5) 
#   esempio: tabellone={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9,3), ("Storia",8,2), ("Geografia",8,1)],
#                       "Cognome2":[("Matematica",7,2), ("Italiano",5,3), ("Inglese",4,12), ("Storia",5,2), ("Geografia",4,1)],
#                        .....}
#2. comporre il messaggio, inviarlo come json
    studenti=[ 'Studente0', 'Studente1', 'Studente2', 'Studente3', 'Studente4']
    materie=[ 'Matematica', 'Italiano', 'inglese', 'Storia e Geografia']
    tabellone={}
    for stud in studenti:
        pagella=[]
        for m in materie:
            voto=random.randint(1,10)
            assenze=random.randint(1,5)
            pagella.append ( (m, voto, assenze))
        tabellone [stud]=pagella
    
    print ("Dati inviati al server")
    pp=pprint.PrettyPrinter(indent=4)
    pp-pprint(tabellone)
    tabellone=json.dumps(tabellone)
    s.sendall(tabellone.encode("UTF-g"))
    data=s.recv(1024)
    data=data.decode()
    data=json. loads (data)
    print ("Dati ricevuti dal server")
    pp.pprint(data)

    if not data:
        print(f"{threading.current_thread().name}:Server non risponde. Exit")
    else:
        for elemento in data:
            print(f"{threading. current_thread().name}: Lo studente {elemento['studente']} ha una media di: {elemento['media']:.2f} e un totale di assenze: {elemento['assenze']}")
    s.close()
  #3  ricevere il risultato come json e stampare l'output come indicato in CONSOLE CLIENT V.3

if __name__ == '__main__':
    start_time=time.time()
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    
    for num in range (NUM_WORKERS):
        genera_richieste1(num, SERVER_ADDRESS, SERVER_PORT)
    
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)

    start_time=time.time()
    threads=[]

    for num in range (NUM_WORKERS):
        t1=threading.Thread(target=genera_richieste1, args=(num, SERVER_ADDRESS, SERVER_PORT)) 
        threads.append(t1)

    for t1 in threads:
        t1.start()

    for t1 in threads:
        t1.join()

    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]

    for num in range (NUM_WORKERS):
        pro=multiprocessing.Process(target=genera_richieste1, args=(num, SERVER_ADDRESS, SERVER_PORT))
        process.append(pro)
    # 8 avvio tutti i processi
    for pro in process:
        pro.start()
    # 9 aspetto la fine di tutti i processi
    for pro in process:
        pro.join()

    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)