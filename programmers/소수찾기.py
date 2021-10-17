import itertools
import math
from typing import List
def solution(numbers : str) -> List[str]:
    answer = []
    for i in range(1,len(numbers) + 1):
        permutation = list(set(itertools.permutations(numbers,i)))
        for char in permutation:
            candi = int(''.join(char))
            if is_prime(candi):
                answer.append(candi)
    return len(set(answer)) # To erase overlap

def is_prime(x:int) -> bool:
    if x <= 1:
        return False
    if x < 3:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True
