from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0

        def recursion(row: int, col: int):
            if grid[row][col] == "1":
                grid[row][col] = "0"
                if col < len(grid[0]) - 1:
                    recursion(row, col + 1)
                if row < len(grid) - 1:
                    recursion(row + 1, col)
                if 0 < col <= len(grid[0]) - 1:
                    recursion(row, col - 1)
                if 0 < row <= len(grid) - 1:
                    recursion(row - 1, col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island += 1
                    recursion(i, j)
        return island
