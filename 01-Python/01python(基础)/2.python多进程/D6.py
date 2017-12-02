#-*-coding:utf-8
import multiprocessing

#Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递

def writer_proc(q):
    try:
        q.put(1, block=False)   #put方法用以插入数据到队列中
    except:
        pass


def reader_proc(q):
    try:
        print (q.get(block=False))  #get方法可以从队列读取并且删除一个元素
    except:
        pass


if __name__ == "__main__":
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=writer_proc, args=(q,))
    writer.start()

    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()

    reader.join()
    writer.join()