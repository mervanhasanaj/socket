import json
import socket

SERVER_ADDRESS='127.0.0.1' # indirizzo server
SERVER_PORT=22224  # porta del server 

def invia_comandi(sock_service):
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
        sock_service.sendall(messaggio.encode("UTF-8"))# invia il vettore di byte

        data=sock_service.recv(1024)# aspettiamo che il server ci rimandi in dietro i dati 
        print("Risultato: ",data.decode())# trasforma il vettore di byte in stringa

def  connessione_server(address, port):
    sock_service=socket.socket()
    sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
    print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
    invia_comandi(sock_service)

if __name__=='__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT)