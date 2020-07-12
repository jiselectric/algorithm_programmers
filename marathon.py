def solution(participant, completion):
    answer = ''
    table = {}
    num = 0 

    for part in participant:
        table[hash(part)] = part
        num = num + hash(part)

    for comp in completion:
        num = num - hash(comp)

    answer = table[num]
    return answer
