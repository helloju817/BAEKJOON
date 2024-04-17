import sys

A = int(input())

for x in range(A):
    arr = input().strip() #공백제거
    if arr[0] == ')' or arr[-1] == '(':
        print('NO')
        continue
    stack = []
    pair = True
    for y in arr:
        if y == '(':
            stack.append(y)
        elif y == ')':
            if stack:
                stack.pop()
            else:
                pair = False
                break

    if pair and not stack:
        print('YES')
    else:
        print('NO')
