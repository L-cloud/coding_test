import collections
from typing import List


class Solution:
    def __init__(self):
        self.travel = collections.defaultdict(list)
        self.min_value = -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        for start, to, price in flights:
            self.travel[start].append([to, price])

        def dfs(pass_num: int, start: int, current_price: int, visited: List[int]) -> bool:
            if pass_num > k:
                return False
            for to, price in sorted(self.travel[start], key=lambda x: x[1]):
                if to == dst:
                    self.min_value = price + current_price
                    print(pass_num)
                    return True
                if to in visited:
                    continue
                visited.append(to)
                if dfs(pass_num + 1, to, current_price + price, visited):
                    return True
                visited.pop()
            return False

        dfs(0, src, 0, [src])

        return self.min_value
