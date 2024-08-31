def solution(s):
    max_len = 0  
    for i in range(len(s)):
        # 첫 번째 경우: 중심이 하나인 홀수 길이 팰린드롬
        left = i
        right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
            left -= 1
            right += 1

        # 두 번째 경우: 중심이 두 개인 짝수 길이 팰린드롬
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
            left -= 1
            right += 1

    return max_len  # 가장 긴 팰린드롬의 길이를 반환