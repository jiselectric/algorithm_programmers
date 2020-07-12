def solution(heights):
    stack = []
    answer = []
    #stack.append(0)
    #maxNum = heights[0]

    while heights:
        valPop = heights.pop()

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > valPop:
                stack.append(i + 1)
                break
        else:
            stack.append(0)
    
    for i in stack[::-1]:
        answer.append(i)

    return answer