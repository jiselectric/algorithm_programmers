def solution(arrangement):
    stack = []
    answer = 0
    arrangement = arrangement.replace('()', '0')

    for i in arrangement:
        if i == '(':
            stack.append(0)
        elif i == ')':
            stack.pop()
            answer = answer + 1
        else:
            answer = answer + len(stack)
    
    return answer