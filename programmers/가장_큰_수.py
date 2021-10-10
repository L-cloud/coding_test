import collections
def solution(numbers):
    dic,numbers = collections.defaultdict(list), list(map(str,numbers))
    answer = ""
    for num in numbers:
        dic[num[0]].append(num)
    for key in sorted(dic.keys(),reverse = True):
        num = sorted(dic[key], key = func, reverse = True)
        for n in num:
            answer += n    
    return answer

def func(x):
    while len(x) < 4:
        x = x + x[0]
    return x # 0 <= number <= 1000
