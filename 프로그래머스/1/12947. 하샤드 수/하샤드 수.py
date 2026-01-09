def solution(x):
    sum = 0
    real_x = x
    
    while True:
        head = x // 10  
        rest = x % 10   
        x = head
        sum += rest
        
        if head == 0:
            break
            
    if sum == 0:
        answer = False
    elif sum != 0:
        if real_x % sum == 0:
            answer = True
        else:
            answer = False
    
    return answer
    