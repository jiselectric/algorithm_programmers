import heapq

def solution(operations):
    answer = []
    queue = []
    #print(operations)
    
    for op in operations:
        command, number = op.split()
        
        if command == 'I':
            heapq.heappush(queue, int(number))
        elif queue and command == 'D':
            if number == "-1":
                heapq.heappop(queue)
            elif number == "1":
                maxNum = max(queue)
                queue.pop(queue.index(maxNum))
        
    if queue:
        # max number
        answer.append(max(queue))
        # min number
        answer.append(heapq.heappop(queue))
    else:
        return [0, 0]
        

    return answer