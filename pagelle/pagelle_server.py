from operator import truediv
import socket
import json

HOST='127.0.0.1'
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[*] In ascolto su %s:%d "%(HOST, PORT))
    clientsocket, address=s.accept()#accetta la conversione
    students = { 
                'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
                'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
                'Nicola Spina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]
                }
    with clientsocket as cs:
        print("Connessione da ", address)
        while True:
            data=cs.recv(1024)
            if not data:
                break
            data=data.decode()
            data=data.strip()
            data=json.loads(data)
            comando=data['operazione']
            print ("[*] Recived: %s" % comando)
            if comando == '#list':
                serialized_stud = json.dumps(students)
                cs.sendall(serialized_stud.encode("UTF-8"))
            elif comando.find('#set') != -1:
                inserimento=comando.split('/')
                controllo_pres=inserimento[1]
                if(controllo_pres in students):
                    cs.sendall("Studente già presente".encode("UTF-8"))
                else:
                    students[inserimento[1]]=[]
                    cs.sendall("Studente inserito".encode("UTF-8"))
            elif comando.find('#get') != -1:
                inserimento=comando.split('/')
                controllo_pres=inserimento[1]
                if(controllo_pres in students):
                    serialized_stud = json.dumps(students[controllo_pres])
                    cs.sendall(serialized_stud.encode("UTF-8"))
                else:
                    cs.sendall("Studente non presente".encode("UTF-8"))
            elif comando.find('#put') != -1:
                boole=True
                inserimento=comando.split('/')
                controllo_pres=inserimento[1]
                controllo_materia=inserimento[2]
                if(controllo_pres in students):
                    for alunno,materie in students.items():
                        if(alunno==controllo_pres):
                            for i in materie:
                                if(controllo_materia == i[0]):
                                    cs.sendall("Materia già presente".encode("UTF-8"))
                                    boole=False
                            if(boole==True):    
                                students[inserimento[1]].append((inserimento[2],inserimento[3],inserimento[4]))
                                cs.sendall("Inserimento avvenuto".encode("UTF-8"))
                else:
                    cs.sendall("Studente non trovato".encode("UTF-8"))
            elif comando.find('#close') != -1:
                break
            print(cs.getpeername())