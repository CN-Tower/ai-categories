#-*-coding:utf-8
import multiprocessing
import time

#创建函数并将其作为单个进程
def worker(interval): #interval间歇，间隔
    n = 5  #进程数
    while n > 0:
        print("The time is {0}".format(time.ctime()))  #初始化时间
        time.sleep(interval)  #睡眠时间
        n -= 1  #递减


if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(3,)) #创建进程，target：调用对象，args：传参数到对象，此处表示睡眠值
    p.start()  #开启进程
    print("p.pid:", p.pid)  #进程号
    print("p.name:", p.name)  #别名
    print("p.is_alive:", p.is_alive())  #进程是否存活