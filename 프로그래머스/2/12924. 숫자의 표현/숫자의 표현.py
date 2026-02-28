# n을 나누어 떨어지게 하는 약수들 중 홀수인 것과 같음


def solution(n):
    answer = 0
    rest = []
    idx = 1
    
    while idx <= n:
        if n % idx == 0:
            rest.append(idx)
        idx += 1
    for i in range(len(rest)):
        if rest[i] % 2 != 0:
            answer += 1 
    
    return answer