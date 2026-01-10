def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    
    for i in s:
        if i.count("p") or i.count("P"):
            p_count +=1
        elif i.count("y") or i.count("Y"):
            y_count +=1
    
    if p_count == y_count:
        return True
    else:
        return False
