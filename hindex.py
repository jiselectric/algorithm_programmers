def solution(citations):
    h = 0
    index = 0 
    list = []

    while index <= len(citations):
        if len(citations) == 1:
            return 1

        above = sum(i >= h for i in citations)
        below = len(citations) - above

        if above >= h and below <= h:
            list.append(h)

        h = h + 1
        index = index + 1 

    return max(list)
