import sys,collections

N = int(sys.stdin.readline())

alpha = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
cnt = collections.Counter()
for al in alpha:
    for i,v in enumerate(al[::-1]):
        cnt[v] += 10**i
num = sorted(list(cnt.keys()),key = lambda x: cnt[x],reverse= True)
score, m, output = {}, 9, 0
for i in num:
    score[i] = m
    m -= 1
for al in alpha:
    output += int("".join([str(score[a]) for a in al]))

print(output)
# max_ = [0]
# # 중복을 어떻게 제거할 것인가.. # 우선순위를 주면됨!!
# def dfs(dict, num, visited):
#     if not visited: # 다 찼음
#         tempt = 0
#         for al in alpha:
#             tempt += int(''.join([str(dict[a]) for a in al]))
#         max_[0] = max(max_[0], tempt)
#         return
#     for i,v in enumerate(visited):
#         dict[v] = num
#         dfs(dict, num-1, visited[:i] + visited[i+1:])
#         del dict[v]
# dfs({},9,list(s))