#-*-coding:utf-8
import multiprocessing
import time

#将进程定义为类

class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):     #进程p调用start()时，自动调用run()
        n = 5
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
