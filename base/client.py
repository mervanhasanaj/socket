from base64 import decode
import socket
import json

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    #af inet indica il tipo di protocollo che viene usato
    #socket stream indica che tipo di socket è
    #whith as tiene aperto i socket dandogli come nome s,
    #dopo che il codice è finito chiuderà la connessione con il server
    s.connect((HOST,PORT))
    while True:
        primoNumero=input("inserisci il primo numero numero. exit() per uscire")
        if primoNumero=="exit()":
            break
        primoNumero=float(primoNumero)
        operazione=input("inserisci l'operazione(+,-,*,/,%)")
        secondoNumero=float(input("inserisci il secondo numero"))
        messaggio={'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero}

        messaggio=json.dumps(messaggio)# trasformiamo l'oggetto in una stringa
        s.sendall(messaggio.encode("UTF-8"))# invia il vettore di byte

        data=s.recv(1024)# aspettiamo che il server ci rimandi in dietro i dati 
        print("Risultato: ",data.decode())# trasforma il vettore di byte in stringa
        

