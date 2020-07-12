import heapq

def solution(scoville, K):
    time = 0 
    minimum = 0 
    heapq.heapify(scoville)

    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        except IndexError:
            return -1
        time = time + 1  

    return time

