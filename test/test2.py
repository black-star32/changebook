import threading
import time


def worker():
    print('i am thread')
    t = threading.current_thread()
    time.sleep(10)
    print(t.getName())

new_t = threading.Thread(target=worker, name='thread-1')
new_t.start()

# worker()

t = threading.current_thread()
print(t.getName())


# 主线程
