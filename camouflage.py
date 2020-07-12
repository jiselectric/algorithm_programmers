def solution(clothes):
    answer = 1
    list = {}

    for cloth in clothes:
        if cloth[1] not in list:
            list[cloth[1]] = 2
        else:
            list[cloth[1]] = list[cloth[1]] + 1

    for i in list:
        answer = answer * (list[i])
    
    return answer - 1