N, K = map(int, input().split())  # 7, 3
arr = list(range(1, N+1))  # [1, 2, 3, 4, 5, 6, 7]

res = []
index = 0  # 시작 인덱스

while arr:
    index = (index + K - 1) % len(arr)  # K번째 사람의 인덱스
    res.append(str(arr.pop(index)))  # 해당 인덱스의 사람을 제거하고 결과에 추가

print("<" + ", ".join(res) + ">")
