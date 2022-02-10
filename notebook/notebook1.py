from threading import Thread
import time, datetime

#creazione funzione thread1
def threadl():
    #avviso che è iniziato il primo thread
    print ("Thread 1 iniziato")
    #fermiamo il thread per 10 secondi
    time.sleep(10)
    #diciamo che il thread è finito
    print ("Thread 1 finito")

#creazione funzione thread2
def thread2():
    #avviso che è iniziato il secondo thread
    print ("Thread 2 iniziato")
    #fermiamo il thread per 4 secondi
    time.sleep(4)
    #diciamo che il thread è finito
    print ("Thread 2 finito")

#avviso di inizio codice
print ("Main iniziato")

#il tempo di inizio è = all'ora corrente
start_time = time.time()
#creazione thread
t1 = Thread(target=threadl)
#creazione thread
t2 = Thread(target=thread2)
#thread 1 parte
t1.start()
#thread 2 parte
t2. start()
#fermiamo il tempo per 2 secondi
time.sleep(2)
#tempo di fine è = al tempo corrente
end_time = time.time()

#mostraiamo il il tempo di fine e di inizio
print (f"Main finito in {end_time-start_time}")