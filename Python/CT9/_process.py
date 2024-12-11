from multiprocessing import Process,Pool
import os , time , random

def run_proc(name):
    print('run child' + name)

if __name__ == '__main__':
    print('parent process %s' % os.getpid)
    p = Process(target=run_proc,args=('test',))
    print('child start')
    p.start()
    p.join()
    print('child end')
    
def long_task(name):
    print('run task %s , threadid: %s' % (name,os.getpid))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('%s task run %0.2f seconds' % (name,end - start))
    
if __name__ == '__main__':
    print('parent thread : %s ' % os.getpid)
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_task,args=(i,))
    print('waiting all done')
    p.close()
    p.join()
    print('all done')
    
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('exit code:',r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('exit code:',p.returncode)

