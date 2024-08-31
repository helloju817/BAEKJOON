def solution(s):
    answer = ''
    num = list(map(int, s.split()))
    min_num=min(num)
    max_num=max(num)
    answer=str(min_num)+" "+str(max_num)
    return answer