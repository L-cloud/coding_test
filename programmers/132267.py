def solution(a : int, b : int, n : int) -> int:
    answer = 0
    while n:
        remain = n % a
        n //= a
        answer += n * b
        n = n * b + remain if n * b > 0 else 0
    return answer
