from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        pop = prices.popleft()
        time = 0 

        for i in prices:
            if pop <= i: # 1 -> 2 // 2 -> 3
                time = time + 1
            else:
                time = time + 1
                break
        answer.append(time)
        
    return answer