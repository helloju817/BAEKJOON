def solution(s):
    answer = True
    count=0
    count1=0
    for i in s:
        if(i=='p' or i=='P'):
            count+=1
        elif (i=='y' or i=='Y'):
            count1+=1
    if count==count1:
        return True
    return False