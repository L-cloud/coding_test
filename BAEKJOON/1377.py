# memory O(2N), time O(NlogN)
N = int(input())
A = [int(input()) for _ in range(N)]
A_dic, answer = {}, 0
for i,v in enumerate(A):
    if v in A_dic:
        A_dic[v].append(i)
    else:
        A_dic[v] = [i]
for key in A_dic: # 결국 O(N)
    A_dic[key] = A_dic[key][::-1]
for i,v in enumerate(sorted(A)):
    answer = max(answer, A_dic[v][-1] - i)
    A_dic[v].pop()
print(answer + 1)