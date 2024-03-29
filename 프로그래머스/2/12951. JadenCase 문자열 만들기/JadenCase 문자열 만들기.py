def solution(s):
    answer=''
    for word in s.split(' '):
        answer+=word.capitalize()+' '
    return answer[:-1]
