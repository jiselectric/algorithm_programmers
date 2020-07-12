from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque((p, i) for i,p in enumerate(priorities))

    while len(dq):
        val = dq.popleft()
        if dq and max(dq)[0] > val[0]:
            dq.append(val)
        else:
            answer = answer + 1
            if val[1] == location:
                break
    return answer
