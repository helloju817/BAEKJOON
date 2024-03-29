def solution(t, p):
    answer=0
    for x in range(len(t)-len(p)+1):
        sub=t[x:x+len(p)]
        if(int(p) >= int(sub)):
            answer+=1
    return answer