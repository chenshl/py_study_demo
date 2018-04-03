#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
multiprocessing模块提供了一个process子类代表一个进程对象，来实现多进程
@author:chensl
"""

import os, time, random

from multiprocessing import Process, Pool


#  子进程要执行的代码(process)
def run_proc(name):
    print("Run child process %s" % os.getpid())


# 通过Pool启动大量子进程
def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds" % (name, (end - start)))



# if __name__ == "__main__":
#     print("Parent process %s" % os.getpid())
#     p = Process(target=run_proc, args=("test",))
#     print("Child process will start...")
#     p.start()
#     p.join()
#     print("Child process end.")

if __name__ == "__main__":
    print(("Parent process %s" % os.getpid()))
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print("Waiting for all subprocesses done...")
    p.close()
    p.join()
    print("All subprocesses done.")
