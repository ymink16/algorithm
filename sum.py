# 프로그래머스 문제 : 두 정수 사이의 모든 값의 합 구하기
def solution(a, b):
    answer = 0
    if (a == b):
        answer = a
    elif (a < b):
        for i in range(a, b+1):
            answer = answer + i
    else:
        for i in range(b, a+1):
            answer = answer + i    
    return answer
