import time
from threading import Thread
def func():
    for n in range(1, 11):
        print(n)
        time.sleep(1)
def func2():
    for k in [chr(i) for i in range(ord('a'), ord('k'))]:
        print(k)
        time.sleep(1)

thr1 = Thread(target=func)
thr2 = Thread(target=func2)

thr1.start()
thr2.start()

thr1.join()
thr2.join()