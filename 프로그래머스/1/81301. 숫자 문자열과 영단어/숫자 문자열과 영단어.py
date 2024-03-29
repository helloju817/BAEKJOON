def solution(s):
    answer = s
    a=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in a:
        answer=answer.replace(i,str(a.index(i)))
    return int(answer)