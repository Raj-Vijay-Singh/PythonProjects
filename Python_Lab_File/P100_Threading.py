import threading
import time

def printlist1():
    for i in [100, 200, 300, 400, 500]:
        print(i)
        time.sleep(1)

def printlist2():
    for i in ["Mayank", "Shanti", "Om", "Puja", "Chirag"]:
        print(i)
        time.sleep(1)

t1 = threading.Thread(target = printlist1)
t2 = threading.Thread(target = printlist2)

t1.start()
t2.start()

t1.join()
t2.join()
