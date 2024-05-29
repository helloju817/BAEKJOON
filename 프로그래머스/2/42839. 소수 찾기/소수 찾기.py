from itertools import permutations

# 소수 판별 함수
def is_prime_number(x):
    if x < 2:  # 2보다 작은 수는 소수가 아님
        return False
    
    for i in range(2, x):  # 2부터 x-1까지 나누어 떨어지면 소수가 아님
        if x % i == 0:
            return False
            
    return True  # 위 조건에 해당하지 않으면 소수

def solution(numbers):
    answer = 0  # 소수의 개수를 저장할 변수
    nums = []  # 순열을 저장할 리스트
    
    # 주어진 숫자로 만들 수 있는 모든 순열 생성
    for i in range(1, len(numbers) + 1):
        # 순열 모듈을 사용해서 나올 수 있는 모든 수 조합 생성
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    
    # 중첩 리스트를 하나의 리스트로 변환하고 중복 제거
    per = list(set(map(int, set(sum(nums, [])))))
    
    # 생성된 수들 중 소수인지 판별
    for p in per:
        if is_prime_number(p):
            answer += 1  # 소수인 경우 카운트 증가

    return answer  # 최종 소수의 개수 반환
