from collections import deque
import sys

N = int(sys.stdin.readline())
queue=deque()
oper=[]

def push_back(item):
    queue.append(int(item))
    
def push_front(item):
    queue.appendleft(int(item))
    
def pop_front():
    if queue:
        return queue.popleft()
    else:
        return -1
def pop_back():
    if queue:
        return queue.pop()
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
    if x[0] == 'push_front':
        push_front(x[1])
    elif x[0] == 'push_back':
        push_back(x[1])
    elif x[0] == 'pop_front':
        print(pop_front())
    elif x[0] == 'pop_back':
        print(pop_back())
    elif x[0] == 'size':
        print(size())
    elif x[0] == 'empty':
        print(is_empty())
    elif x[0] == 'front':
        print(front())
    elif x[0] == 'back':
        print(back())
