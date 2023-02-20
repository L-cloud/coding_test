def solution(n:int) -> int:
    k, f0,f1 = 1, 0, 1
    while k != n:
        answer = (f0 + f1) % 1234567
        f0, f1 = f1, answer
        k += 1
    return answer % 1234567
