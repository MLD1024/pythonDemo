# coding:utf-8
from  multiprocessing import Pool
import time

i =100
def Foo():
    global i
    i = i+1
    print i

def Bar(arg):
    print arg

if __name__ == '__main__':
    t_start=time.time()
    pool = Pool(5)

    for i in range(10):
        pool.apply_async(func=Foo, args=(), callback=Bar)#维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    pool.terminate()
    t_end=time.time()
    t=t_end-t_start
    print 'the program time is :%s' %t

