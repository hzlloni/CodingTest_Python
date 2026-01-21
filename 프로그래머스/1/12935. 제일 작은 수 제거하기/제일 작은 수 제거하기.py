def solution(arr):
    answer = []
    small = [min(arr)]
    
    answer = [x for x in arr if x not in small]
    if not answer:
        return [-1]
    
    return answer