def solution(n):
    answer = 0
    new_word = str(n)
    
    answer = sorted(new_word, reverse= True)
    # '구분자'.join(리스트)
    alist = int(''.join(answer))
    
    return alist
