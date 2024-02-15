def isFull():
    if rear == N-1:
        return True
    else:
        return False

def isEmpty():
    if front == rear:
        return True
    else:
        return False

def Qpeek():
    if isEmpty():
        print('No item')
    else:
        return q[front+1]

def enQ(item):
    global rear
    if isFull():
        print('Full')
    else:
        rear += 1
        q[rear] = item

def deQ():
    global front
    if isEmpty():
        print('No item')

    else:
        front += 1
        temp = q[front]
        return temp


N = 10

q = [0] * N
front = rear = -1

for i in range(1, 4):
    enQ(i)

for j in range(2):
    deQ()

print(isEmpty())




