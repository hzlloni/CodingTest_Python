def solution(s):
    answer = ''
    
    mod = len(s) % 2
    index = int(len(s) / 2)
    

    if mod == 1:
       answer += s[index]
    else:
        answer += s[index-1:index+1]
        
        
    return answer