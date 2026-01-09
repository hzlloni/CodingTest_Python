import math

def solution(n):
    answer = int(math.sqrt(n))
    
    if answer * answer == n:
        return (answer+1) ** 2
    else:
        return -1