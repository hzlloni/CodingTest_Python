def solution(s):
    answer = ''
    
    part = s.split()
    num = list(map(int, part))
    
    max_num = max(num)
    min_num = min(num)
    
    answer = f"{min_num} {max_num}"
    
    return answer