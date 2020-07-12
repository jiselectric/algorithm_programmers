def solution(phone_book):
    answer = True
    table = {}

    for num in phone_book:
        table[num] = 1

    for num in phone_book:
        combination = ''
        for i in num:
            combination = combination + i
            
            if combination in table and combination != num:
                return False

    return answer