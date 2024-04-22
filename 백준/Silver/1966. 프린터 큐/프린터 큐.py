T = int(input())

for x in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    if N == 1:
        print(1)
        continue

    queue = [(item, index) for index, item in enumerate(priorities)]
    order = 0

    while queue:
        current = queue.pop(0)
        has_higher_priority = False

        # 현재 문서보다 중요도가 높은 문서가 있는지 직접 검사합니다.
        for other in queue:
            if current[0] < other[0]:
                has_higher_priority = True
                break

        if has_higher_priority:
            # 중요도가 높은 문서가 있으면 현재 문서를 큐의 끝으로 보냅니다.
            queue.append(current)
        else:
            # 그렇지 않다면 현재 문서를 인쇄합니다.
            order += 1
            if current[1] == M:
                # 만약 인쇄된 문서가 우리가 알고 싶은 문서의 위치에 해당한다면
                print(order)
                break
