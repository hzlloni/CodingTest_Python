"""
def solution(priorities, location):
    answer = 0
    queue = []
    
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    
    while queue:
        cur = queue.pop(0)
        
        if cur[0] < max(x[0] for x in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer
"""
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()

    for i in range(len(priorities)):
        queue.append((priorities[i], i))

    while queue:
        cur = queue.popleft()

        if queue and cur[0] < max(x[0] for x in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer
