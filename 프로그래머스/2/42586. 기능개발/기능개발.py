import math

def solution(progresses, speeds):
    answer = []
    count_answer = []
    count = 1
    index = 0
    
    for i in range(len(speeds)):
        progress = math.ceil((100 - progresses[i]) / speeds[i])   
        answer.append(progress)            
    
    for j in range(1, len(speeds)):
        if answer[index] >= answer[j]:
            count += 1
        else: 
            count_answer.append(count)
            count = 1
            index = j
    count_answer.append(count)

    return count_answer