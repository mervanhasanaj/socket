from http import client
import socket
import json

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    progressivo=1
    s.bind((HOST,PORT))
    s.listen()
    print("[*] In ascolto su %s:%d"%(HOST,PORT))
    clientsocket, address=s.accept()

with clientsocket as cs:
    print("Conessione da ",address)
    while True:
        data=cs.recv(1024)
        if not data:
            break
        data=data.decode()
        data=json.loads(data)
        frase=data['frase']
        ris=""
        if type(frase)==str:
            ris=str(progressivo) + ') '+ frase
            progressivo+=1
        else:
            ris="Operazione non riconosciuta"
        '''
        elif operazione=="*":
            ris=primoNumero*secondoNumero
        elif operazione=="/":
            if secondoNumero==0:
                ris="non puoi dividere per 0"
            else:
                ris=primoNumero/secondoNumero
        elif operazione=="%":
            ris=primoNumero%secondoNumero
        else:
            ris="Operazione non riconosciuta"
        '''
        ris=str(ris)#casting
        print('Ricevuto: ' + ris)
        cs.sendall(ris.encode("UTF-()"))
