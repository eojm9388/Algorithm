class Queue:
    def __init__(self, maxsize):
        self.size = maxsize
        self.item = [None] * maxsize
        self.rear = -1
        self.front = -1


    def enQueue(self, item):
        self.rear += 1
        self.item[self.rear] = item


    def deQueue(self):
        self.front += 1

        return self.item[self.front]


q = Queue(3)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
print(q.item)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.item)

