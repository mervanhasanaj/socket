import time
import logging
from threading import Thread


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

#creiamo la funzione test e passiamo i come parametro
def test(i):
  #informa che il thread è iniziato
  logging.info(f"{i} thread: iniziato")
  #ferma la funzione su 3 secondi
  time.sleep(3)
  #informa che il thread è finito
  logging.info(f"{i} thread: finito")


#ciclo for per creare 5 thread
for i in range(5):
  #vreazione del tread
  t = Thread(target=test, args=(i,))
  #inizio
  t.start()
  t.join()