import heapq

def prim_optimized(graph, start_node, V):
    visited = [False] * (V + 1)  # 방문한 노드를 추적
    edges = [(0, start_node)]  # 시작 노드로부터의 가중치와 노드 번호
    total_weight = 0  # 최소 신장 트리의 총 가중치
    count = 0  # 연결된 노드 수

    while edges:
        weight, node = heapq.heappop(edges)
        if not visited[node]:
            visited[node] = True
            total_weight += weight
            count += 1
            if count == V:  # 모든 노드가 연결되면 종료
                break
            for adj_node, adj_weight in graph[node]:
                if not visited[adj_node]:
                    heapq.heappush(edges, (adj_weight, adj_node))

    return total_weight

V, E = map(int, input().split()) # V는 정점의 개수, E는 간선의 개수

# 그래프를 초기화하는 과정
graph = {} # 빈 딕셔너리로 시작합니다.
for i in range(1, V+1): # 각 정점에 대해 반복합니다.
    graph[i] = [] # 각 정점(i)을 키로 하고, 빈 리스트를 값으로 하는 항목을 추가합니다.

# 간선 정보를 입력받아 그래프를 구성하는 과정
for _ in range(E):
    A, B, C = map(int, input().split()) # A와 B는 간선의 양 끝 정점, C는 가중치
    graph[A].append((B, C)) # 정점 A의 리스트에 (B, C) 쌍을 추가합니다.
    graph[B].append((A, C)) # 무방향 그래프이므로, B에서 A로 가는 간선도 동일한 가중치로 추가합니다.


# 최적화된 프림 알고리즘을 사용하여 최소 스패닝 트리의 가중치를 계산
min_cost = prim_optimized(graph, 1, V)
print(min_cost)
