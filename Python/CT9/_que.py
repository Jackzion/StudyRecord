from multiprocessing import Process,Queue
import os , time , random

#写数据
def write(q):
    print('process to write : %s' , os.getpid)
    for value in ['a','b','c']:
        print('put %s in queue ..' % value)
        q.put(value)
        time.sleep(random.random())

#读数据
def read(q):
    print('process to write : %s' , os.getpid)
    while True:
        valeue = q.get(True)
        print('get %s from queue..' % valeue)

if __name__ == '__main__':
    #父进程创建 queue 传给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()