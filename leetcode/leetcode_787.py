import collections
import heapq
from typing import List


class Solution: # Wrong code
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


class Solution: #Right code...
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        heap = [(0, src, K + 1)]
        visits = [0] * n

        for start, end, cost in flights:
            graph[start][end] = cost

        while heap:
            cost, start, end = heapq.heappop(heap)

            if start == dst:
                return cost
            if visits[start] >= end:
                continue

            visits[start] = end

            for new_end, new_cost in graph[start].items():
                heapq.heappush(heap, (cost + new_cost, new_end, end - 1))

        return -1



class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight, h = collections.defaultdict(list), [(0, src, -1)]
        for src_, dst_, price in flights:
            flight[src_].append((price, dst_))  # key = src, value = [price,dst]
        visited = {}
        while h:
            price, node, via = heapq.heappop(h)
            if node == dst:
                return price
            if via < k:
                for price_, dst_ in flight[node]:
                    price_ += price
                    if dst_ not in visited:
                        visited[dst_] = [price_, via + 1]
                        heapq.heappush(h, (price_, dst_, via + 1))
                    elif price_ < visited[dst_][0] or via + 1 < visited[dst_][1]:
                        if price_ < visited[dst_][0] and via + 1 < visited[dst_][1]:
                            visited[dst_] = [price_, via + 1]
                        heapq.heappush(h, (price_, dst_, via + 1))

        return -1