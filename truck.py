from collections import deque

def solution(bridge_length, weight, truck_weights):
    dq = deque()
    second = 0
    track = 0
    index = 0

    while True:
        second = second + 1
        if len(dq) == bridge_length:
            track = track - dq.popleft()
        if track + truck_weights[index] <= weight:
            if index == len(truck_weights) - 1:
                second = second + bridge_length
                break
            dq.append(truck_weights[index])
            track = track + truck_weights[index]
            index = index + 1
        else:
            dq.append(0)

    return second