import heapq
import math

def solution(jobs):
    last, now, answer, count = -1, 0, 0, 0
    size = len(jobs)
    wait = []

    while count < size:
        for job in jobs:
            if last < job[0] <= now:
                answer = answer + (now - job[0])
                heapq.heappush(wait, job[1])
        
        if len(wait) > 0:
            answer = answer + len(wait) * wait[0]
            last = now
            now = now +  heapq.heappop(wait)
            count = count + 1
        else:
            now = now + 1
    
    return answer // size