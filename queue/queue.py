class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

myQueue = Queue()
myQueue.enqueue(3)
myQueue.enqueue(5)
myQueue.dequeue()
myQueue.display()

from collections import deque
q= deque()
q.append(5)
q.append(3)
q.popleft()
print(q)


from queue import Queue
myq = Queue(maxsize=5)
myq.put(0)
myq.put(4)
myq.get()
print(myq)