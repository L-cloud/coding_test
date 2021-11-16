def solution(numbers):
    candi = [i for i in range(10)]
    return sum(set(candi) - set(numbers))
