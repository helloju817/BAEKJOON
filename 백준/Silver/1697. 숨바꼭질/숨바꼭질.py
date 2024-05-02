import sys

MAX = 100001  # curr의 값이 17 이상으로 증가할 수 있음. 만약 curr가 17인 상태에서 2 * curr 연산을 수행하면 그 결과는 34
n, k = map(int, input().split())  # 5,17

distance = [0] * MAX# 각 위치까지의 최소 이동 횟수를 저장할 배열, 초기값은 모두 0
queue = [n]  # 탐색을 시작할 위치 n을 큐에 추가

# 큐에 아직 처리할 위치가 남아 있는 동안 계속 실행
while queue:
    curr = queue.pop(0)  # 5
    
    # 현재 위치가 동생의 위치와 같다면
    if curr == k:
        print(distance[curr])  # 현재 위치까지의 이동 횟수 출력
        break  # 루프 종료
    
    # 현재 위치에서 갈 수 있는 세 가지 다음 위치를 검사
    for next_pos in (curr - 1, curr + 1, 2 * curr):
        # 다음 위치가 유효한 범위 내에 있고 아직 방문하지 않은 위치인 경우
        if 0 <= next_pos < MAX and not distance[next_pos]:
            distance[next_pos] = distance[curr] + 1  # 이동 횟수 갱신 (현재 위치의 이동 횟수 + 1)
            queue.append(next_pos)  # 다음 위치를 큐에 추가하여 나중에 탐색하도록 함