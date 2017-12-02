import time
import threading

# 打开线程锁
lock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        #self.counter = counter

    def run(self):
        # 某某线程要开始了
        print(self.name + "开始了##################")

        if self.name == "听歌线程":
            matter1(music)
        elif self.name == "打码线程":
            matter2(number)
        elif self.name == "零食线程":
            matter3(snacks)
        print(self.name + "结束了##################")

def matter1(music):
    for i in range(0,len(music)):
        print("第" + str(i + 1) + "首歌是：" + str(music[i]))
        # 假设每一首歌曲的时间是2秒
        time.sleep(2)
        print("切换下一首歌...")

def matter2(number):
    lock.acquire()
    j = 0
    while j <= number:
        print("我准备写入第" + str(j + 1) +"行代码")
        j = j + 1
        # 假设每写一行代码的时间为1秒
        time.sleep(1)
        print("写下一行代码...")
    lock.release()

def matter3(snacks):
    #lock.acquire()
    for k in range(0,len(snacks)):
        print("我正在听着歌吃" + str(snacks[k]) + "零食")
        #每吃一袋零食间隔5秒
        time.sleep(5)
        print("吃完了一包零食")
    #lock.release()

if __name__ == '__main__':
    # 设定我要听的歌为
    music = ["music1","music2","music3"]

    # 设定我要打码的行数
    number =2

    # 设定我想吃的零食
    snacks = ["咪咪","辣条"]

    # 开始时间
    start = time.time()

    thing1 = MyThread(matter1, music,"听歌线程")
    thing2 = MyThread(matter2, number, "打码线程")
    thing3 = MyThread(matter3, snacks, "零食线程")
    thing1.start()
    thing2.start()
    thing3.start()
    thing1.join()
    thing2.join()
    thing3.join()

    # 结束时间
    end = time.time()
    print("完成的时间为：" + str(end - start))