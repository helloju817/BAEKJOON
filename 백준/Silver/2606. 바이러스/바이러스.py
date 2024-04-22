n = int(input())  
v = int(input())  
graph = [[] for _ in range(n + 1)] 
visited = [False] * (n + 1) 

def dfs(v):
    visited[v] = True
    count = 1  
    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += dfs(neighbor)
    return count

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(1) - 1)
