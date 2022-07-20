import sys,bisect
input = sys.stdin.readline
N,max_len = int(input()), 0 
numbers = list(map(int, input().split()))
for i in range(N):
    left,right = [],[]
    for l in numbers[:i]: #
        if  l < numbers[i]:
            l_idx = bisect.bisect_left(left, l)
            if not left or l_idx == len(left):
                left.append(l)
            else:
                left[l_idx] = l 
    for r in numbers[:i:-1]:
        if r < numbers[i]:
            r_idx = bisect.bisect_left(right, r)
            if not right or r_idx == len(right):
                right.append(r)
            else:
                right[r_idx] = r
    max_len = max(max_len,len(right) + len(left) + 1)
print(max_len)
