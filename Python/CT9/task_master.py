import random , time , queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 把两个 Queue 注册到网络上
def get_task_queue():
    return task_queue

def get_result_queue():
    return result_queue

# 从 baseManager 继承的 queueManager
class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    # 把两个queue 注册到网络上
    QueueManager.register('get_task_queue',callable=get_task_queue)
    QueueManager.register('get_result_queue',callable=get_result_queue)
    # port 5000  , 设置验证码 ‘abc’
    manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    # 启动 queue
    manager.start()
    #通过QueueManager获取任务队列，避免绕过封装
    task = manager.get_task_queue()   
    result = manager.get_result_queue() 
    # 放几个任务进去
    for i in range(10):
        n = random.randint(0,10000)
        print('put task %d' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10000)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')
