import math
def solution(progresses, speeds):
    left=[math.ceil((100-a)/b)for a,b in zip(progresses,speeds)]
    answer=[]
    front=0
    for i in range(len(speeds)):
        if left[front]<left[i]:
            answer.append(i-front)
            front=i
    answer.append(len(speeds)-front)


    return answer
