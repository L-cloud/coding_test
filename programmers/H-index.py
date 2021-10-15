def solution(citations):
    ans = 0
    while len(list(filter(lambda x: x >= ans, citations))) >= ans:
        ans += 1
    return ans - 1

def solution(citations): # better version
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0