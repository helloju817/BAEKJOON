import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()
oper = deque()

def push(stack, item):
    stack.append(int(item))

def pop(stack):
    if stack:
        return stack.pop()
    else:
        return -1

def size(stack):
    return len(stack)

def is_empty(stack):
    if stack:  
        return 0
    else:          
        return 1

def top(stack):
    if stack:
        return stack[-1]
    else:
        return -1

for _ in range(N):
    oper.append(sys.stdin.readline().strip().split())

for x in oper:
    if x[0] == 'push':
        push(stack, x[1])
    elif x[0] == 'pop':
        print(pop(stack))
    elif x[0] == 'size':
        print(size(stack))
    elif x[0] == 'empty':
        print(is_empty(stack))
    elif x[0] == 'top':
        print(top(stack))
