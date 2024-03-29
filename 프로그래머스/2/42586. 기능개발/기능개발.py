import math

def solution(progresses, speeds):
    days = []  # 각 기능이 완성되는 데 필요한 일수를 저장할 리스트
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))  # 직접 인덱스를 사용하여 계산

    answer = []
    while days:
        release_day = days.pop(0)  # 첫 번째 기능의 완성일
        features = 1  # 첫 번째 기능은 항상 현재 배포에 포함됨

        # 현재 배포일보다 작거나 같은 완성일을 가진 기능들을 카운트
        while days and days[0] <= release_day:
            days.pop(0)  # 다음 기능도 현재 배포에 포함되므로 리스트에서 제거
            features += 1  # 배포될 기능의 수 증가
        
        answer.append(features)  # 현재 배포될 기능의 수를 결과 리스트에 추가

    return answer
