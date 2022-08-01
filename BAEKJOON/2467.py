import sys,bisect
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
min_value = [float('inf'), float('inf')]
# bisect로 풀면됨
for num in nums:
    tempt = -num
    index = bisect.bisect_left(nums,tempt)
    sample = [index -1, index]
    for s in sample:
        if 0 <= s < N and nums[s] != num:
            if abs(nums[s] + num) < abs(sum(min_value)):
                min_value = [nums[s], num]
print(*sorted(min_value)) 

