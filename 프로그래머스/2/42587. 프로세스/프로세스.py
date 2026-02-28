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
    queue = deque((p, i) for i, p in enumerate(priorities))
    order = 0

    while queue:
        cur_p, cur_i = queue.popleft()

        if any(p > cur_p for p, _ in queue):
            queue.append((cur_p, cur_i))
        else:
            order += 1
            if cur_i == location:
                return order
