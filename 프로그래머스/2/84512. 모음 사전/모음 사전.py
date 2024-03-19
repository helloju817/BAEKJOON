from itertools import product
def solution(word):
    answer = []
    alphabet = ['A','E','I','O','U']
    
    for i in range(len(alphabet)):
        # alphabet의 원소들 중 (i+1)개씩 구성된 중복 순열을 반환
        for j in product(alphabet, repeat = i+1):
            answer.append(''.join(j))
    answer.sort()
    return answer.index(word)+1