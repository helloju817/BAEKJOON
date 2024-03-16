cnt = 0 
def solution(numbers, target):
    global cnt
    cnt = 0  
    dfs(numbers, target, 0, 0)
    return cnt

def dfs(numbers, target, idx, values):
    global cnt
    if idx == len(numbers) and values == target:
        cnt += 1
        return
    elif idx == len(numbers):
        return

    dfs(numbers, target, idx+1, values + numbers[idx])
    dfs(numbers, target, idx+1, values - numbers[idx])
