from threading import Thread
import queue
from time import sleep

# q 代表任务队列
# NUM是并发线程总数
# JOBS 是有多少任务


q=queue.Queue()
NUM =2
JOBS = 10

# 具体的处理函数，负责处理单个任务
def do_sth (args):
    print(args)

# 这个是工作进度，负责不断从队列取数据并处理
def worker(agrs):
    while True:
        args=q.get()
        do_sth(agrs)
        sleep(1)
        q.task_done()

# fork NUM个线程等待队列
for i in range(NUM):
    t = Thread(target=worker())
    t.setDaemon(True)
    t.start()

# 把JOB排入队列
for i in range(JOBS):
    q.put(i)

# 等待所有JOBS完成
q.join()


# if __name__ == '__main__':
#     t=Thread(target=sayhi,args=('hh',))
#     t.start()
#     print('主线程')