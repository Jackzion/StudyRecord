import random , time , queue
from multiprocessing.managers import BaseManager

# 创建类似的 queueManager
class QueueManager(BaseManager):
    pass
# 获取
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接服务器
server_add = '127.0.0.1'
print('Connect to server %s...' % server_add)
# 端口和验证码
m = QueueManager(address=(server_add,5000),authkey=b'abc')
# 连接
m.connect()
# 获取 queue
task = m.get_task_queue()
result = m.get_result_queue()
# 从 task 获取 ， 放到 result
for i in range(10):
    try:
        n = task.get(timeout = 1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')
# 处理结束
print('work out')