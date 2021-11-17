import collections
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_table, edge,h,visited = [float('inf') for _ in range(n)], collections.defaultdict(list),[],{k : 1}
        for time in times:
            edge[time[0]].append([time[1], time[2]]) # key = start_node, value = [source_node, weight]
        for node in edge[k]:
            heapq.heappush(h,(node[1],(node[0],node[1])))
            time_table[node[0] - 1] = node[1]
        time_table[k- 1] = 0
        while h and len(visited) != n:
            current_node = heapq.heappop(h)[1]
            while h and current_node[0] in visited:
                current_node = heapq.heappop(h)[1]
            visited[current_node[0]] = 1
            time_table[current_node[0] - 1] = current_node[1]
            for node in edge[current_node[0]]:
                heapq.heappush(h, (node[1] + current_node[1],(node[0],node[1] + current_node[1])))
        if len(visited.keys()) == n :
            return max(time_table)
        return -1