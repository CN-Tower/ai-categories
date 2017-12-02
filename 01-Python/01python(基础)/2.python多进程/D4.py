#-*-coding:utf-8
# import multiprocessing
# import time
#
#daemon程序对比结果
#
# def worker(interval):
#     print("work start:{0}".format(time.ctime()));
#     time.sleep(interval)
#     print("work end:{0}".format(time.ctime()));
#
#
# if __name__ == "__main__":
#     p = multiprocessing.Process(target=worker, args=(3,))
#     #p.daemon = True
#     p.start()
#     print ("end!")      #因子进程设置了daemon属性，主进程结束，它们就随着结束了。

import multiprocessing   #设置daemon执行完结束的方法
import time              #daemon是父进程终止后自动终止，且自己不能产生新进程，必须在start()之前设置。


def worker(interval):
    print("work start:{0}".format(time.ctime()));
    time.sleep(interval)
    print("work end:{0}".format(time.ctime()));


if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(3,))
    p.daemon = True
    p.start()
    p.join()
    print ("end!")