import heapq

def solution(stock, dates, supplies, K):
    times = 0 
    start = 0 
    heap = []

    while stock < K:
        for i in range(start, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(heap, -supplies[i])
                start = i + 1
            else:
                break
        stock = stock + -heapq.heappop(heap)
        times = times + 1

    return times