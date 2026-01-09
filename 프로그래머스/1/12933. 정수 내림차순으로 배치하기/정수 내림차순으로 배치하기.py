def solution(n):
    answer = 0
    new_word = str(n)
    
    answer = sorted(new_word, reverse= True)
    alist = int(''.join(answer))
    
    return alist
