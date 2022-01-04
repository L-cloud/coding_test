from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))  # start 범위 작고 범위가 좁은 순서대로
        output = []
        overlap = range(intervals[0][0], intervals[0][1] + 1)

        for index, interval in enumerate(intervals):
            if range(max(overlap[0], interval[0]), min(overlap[-1], interval[-1]) + 1):  # overlap 있는 구간 check
                overlap = range(min(overlap[0], interval[0]),
                                max(overlap[-1], interval[-1]) + 1)  # 문제는 마지막에 overlap이 추가가 안 될 수 있음
            else:
                output.append([overlap[0], overlap[-1]])
                overlap = range(interval[0], interval[-1] + 1)
            if index == len(intervals) - 1:
                output.append([overlap[0], overlap[-1]])
        return output