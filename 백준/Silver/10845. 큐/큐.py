import sys

N = int(sys.stdin.readline())
queue = []
oper=[]
def push(item):
    queue.append(int(item))

def pop():
    if queue:
        return queue.pop(0)
    else:
        return -1

def size():
    return len(queue)

def is_empty():
    if queue:  
        return 0
    else:          
        return 1

def front():
    if queue:
        return queue[0]
    else:
        return -1
def back():
    if queue:
        return queue[-1]
    else:
        return -1
for _ in range(N):
    oper.append(sys.stdin.readline().strip().split())

for x in oper:
    if x[0] == 'push':
        push(x[1])
    elif x[0] == 'pop':
        print(pop())
    elif x[0] == 'size':
        print(size())
    elif x[0] == 'empty':
        print(is_empty())
    elif x[0] == 'front':
        print(front())
    elif x[0] == 'back':
        print(back())
