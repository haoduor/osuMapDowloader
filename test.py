import sys
import time
import threading
import Queue

lock = threading.Lock()


def pp(a):
    for i in range(3):
        lock.acquire()
        print a, threading.activeCount()
        lock.release()
        time.sleep(1)


if __name__ == '__main__':
    t = range(1, 100)
    q = Queue.Queue()
    for i in t:
        q.put(i)

    while not q.empty():
        if threading.active_count() != 5:
            t = threading.Thread(target=pp, args=(q.get(), ))
            t.start()
        else:
            pass

    print 'end'