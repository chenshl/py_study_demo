#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/02 21:18
# 多线程处理同一事物时加线程锁
# 使用 Thread 对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，
# 对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间

import threading
import time

class myThead(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)  #调用Thread的构造方法
        self.threadID = threadID
        self.neme = name
        self.counter = counter

    def run(self):
        print("开启线程：%s" % self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s:%s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThead(1, "thread-1", 1)
thread2 = myThead(2, "thread-2", 2)
# 开启新线程
thread1.start()
thread2.start()
# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
# 等待所有线程完成
for i in threads:
    i.join()
print("退出主线程！")
