import heapq
import sys

arr = []
result = []

N = int(sys.stdin.readline().strip()) 

for x in range(N):
    x = int(sys.stdin.readline().strip()) 
    if x == 0:
        if arr:
            abs_val, real_val = heapq.heappop(arr) 
            result.append(real_val)  
        else:
            result.append(0)
    else:
        heapq.heappush(arr, (abs(x), x)) 

for res in result:
    print(res) 
