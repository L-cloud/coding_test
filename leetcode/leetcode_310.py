from typing import List
import collections
class Solution:
    def findMinHeightTrees(self, num: int, edges: List[List[int]]) -> List[int]:  # using que
        if num <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = []
        for i in range(num):
            if len(graph[i]) == 1:
                leaves.append(i)

        while num > 2:
            num -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
