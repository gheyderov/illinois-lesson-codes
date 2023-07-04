import time
import threading

def do_something():
    print('Process started...')
    time.sleep(1)
    print('Process ended!')


t1 = time.time()

threads = []

for i in range(1000):
    th1 = threading.Thread(target=do_something)
    th1.start()
    threads.append(th1)


for i in threads:
    i.join()


t2 = time.time()

print(t2 - t1)