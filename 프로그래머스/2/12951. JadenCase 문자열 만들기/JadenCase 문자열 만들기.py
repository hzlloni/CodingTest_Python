def solution(s):
    answer = s.split(' ')
    
    for i in range(len(answer)):
        answer[i] = answer[i].capitalize()
        result = ' '.join(answer)
    
    return result