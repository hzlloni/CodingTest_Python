import numpy as np 

def solution(a, b):
    
    a = np.array(a)
    b = np.array(b)
    
    answer = sum((a*b))
    
    return int(answer)