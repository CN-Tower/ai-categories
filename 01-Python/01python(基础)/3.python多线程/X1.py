#-*-coding:utf-8
from threading import Thread
import time

#多线程实现

def loop(name, seconds):
    print ('start loop', name, ' at:', time.ctime())
    time.sleep(1)
    print ('end loop', name, ' at:', time.ctime())


if __name__ == '__main__':
    loops = [2, 4]
    nloops = range(len(loops))
    threads = []
    print ('starting at :', time.ctime())
    for i in nloops:
        t = Thread(target=loop, args=(i, loops[i],))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    print ('all DONE at :', time.ctime())