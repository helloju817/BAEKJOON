#heappop : 힙에서 가장 작은 요소를 제거하고 반환
import heapq
import sys
arr=[]
N = int(sys.stdin.readline())
for x in range(N):
    x = int(sys.stdin.readline())
    if x==0:
        if len(arr)>0:
            k =  heapq.heappop(arr)
            print(-k)
        else:
            print(0)
            
    else:
        heapq.heappush(arr,-x)