def solution(n, times):
    times.sort()
    low = 0
    high = sum(times) * n // len(times) + len(times)
    while low != high:
        mid = low +(high - low) // 2
        people = 0
        for i in times:
            people += mid // i
            if n <= people:
                high = mid
                break
        if people < n:
            low = mid +1
    return low
