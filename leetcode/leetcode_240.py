class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row < len(matrix):
            if matrix[row][0] <= target and target <= matrix[row][-1]:
                index = bisect.bisect_left(matrix[row], target)
                if matrix[row][index] == target: # dont'worry about large index because of target <= matrix[row][-1]
                    return True
            row += 1
        return False
