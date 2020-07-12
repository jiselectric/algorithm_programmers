def solution(numbers):
    numbers = list(map(str, numbers))
    order = sorted(numbers, key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(order)))

    return answer
