# HASANAJ
# calcolatrice client per calcoServer.py versione multithread
from ast import operator
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
NUM_WORKERS=2

def genera_richieste(num,address,port):
    start_time_thread= time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except Exception as e:
        print(e)
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
    #1. rimpiazzare questa parte con la generazione di operazioni e numeri random, non vogliamo inviare sempre 3+5
    # numeri da 1 a 100
    #primoNumero=3
    #operazione="+"
    #secondoNumero=5
    primoNumero= random.randint(1,100)
    operazione=""
    secondoNumero= random.randint(1,100)
    op=random.randint(0,3)
    if op == 0:
        operazione="+"
    elif op == 1:
        operazione="-"
    elif op == 2:
        operazione="*"
    else:
        operazione="/"

    print(str(primoNumero) + "," + str(op) + "," + str(secondoNumero))

    #2. comporre il messaggio, inviarlo come json e ricevere il risultato
    messaggio={'primoNumero':primoNumero,
    'operazione':operazione,
    'secondoNumero':secondoNumero}
    sock_service=socket.socket()
    sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
    messaggio=json.dumps(messaggio)# trasformiamo l'oggetto in una stringa
    sock_service.sendall(messaggio.encode("UTF-8"))# invia il vettore di byte

    data=sock_service.recv(1024)# aspettiamo che il server ci rimandi in dietro i dati 
    print("Risultato: ",data.decode())# trasforma il vettore di byte in stringa


    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name}: Risultato: {data.decode()}") # trasforma il vettore di byte in stringa
    s.close()
    end_time_thread=time.time()
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)

if __name__ == '__main__':
    start_time=time.time()

    # 3 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    for num in range (NUM_WORKERS):
        genera_richieste(num, SERVER_ADDRESS, SERVER_PORT)

    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)

    start_time=time.time()
    threads=[]

    # 4 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # ad ogni iterazione appendo il thread creato alla lista threads
    for num in range (NUM_WORKERS):
        t1=threading.Thread(target=genera_richieste, args=(num, SERVER_ADDRESS, SERVER_PORT)) 
        threads.append(t1)

    # 5 avvio tutti i thread
    for t1 in threads:
        t1.start()

    # 6 aspetto la fine di tutti i thread
    for t1 in threads:
        t1.join()

    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # 7 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # ad ogni iterazione appendo il thread creato alla lista threads
    for num in range (NUM_WORKERS):
        pro=multiprocessing.Process(target=genera_richieste, args=(num, SERVER_ADDRESS, SERVER_PORT))
        process.append(pro)
    # 8 avvio tutti i processi
    for pro in process:
        pro.start()
    # 9 aspetto la fine di tutti i processi
    for pro in process:
        pro.join()

    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)
