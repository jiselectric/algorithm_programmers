def solution(array, commands):
    answer = []
    start, end, select = 0, 0, 0 

    for command in commands:
        start = command[0] - 1
        end = command[1]
        select = command[2] - 1
        
        cut = array[start:end]
        sortArr = sorted(cut)

        target = sortArr[select]
        answer.append(target)

    return answer