import re
import collections

import collections
from typing import List
def solution(numbers:List[int]) -> str:
    numbers = list(map(str,numbers))
    numbers = division(numbers)
    answer = "".join(numbers)
    if answer[0] == '0':
        return '0'
    return answer

def division(numbers:List[int]) -> str:
    if len(numbers) < 2:
        return numbers
    left_num = division(numbers[:len(numbers) // 2])
    right_num = division(numbers[len(numbers) // 2 :])
    output,i, j = [],0, 0 
    while i < len(left_num) and j < len(right_num):
        if left_num[i] + right_num[j] < right_num[j] + left_num[i] :
            output.append(right_num[j])
            j += 1
        else: # left is bigger
            output.append(left_num[i])
            i += 1
    while i < len(left_num):
        output.append(left_num[i])
        i += 1
    while j < len(right_num):
        output.append(right_num[j])
        j += 1
    return output



def solution(numbers):
    dic, numbers = collections.defaultdict(list), list(map(str, numbers))
    answer = ""
    for num in numbers:
        dic[num[0]].append(num)
    for key in sorted(dic.keys(), reverse=True):
        if dic[key] != []:
            num = sorted(dic[key], key=lambda x: (func(x), x[-1]), reverse=True)
            for n in num:
                answer += n

    if re.sub('0', '', answer) == '':
        return '0'

    return answer


def func(x):
    while len(x) < 4:
        x = x + x[0]
    return x  # 0 <= number <= 1000
