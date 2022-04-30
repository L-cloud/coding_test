import collections
def solution(id_list, report, k):
    cnt = collections.Counter(id_list)
    dic = collections.defaultdict(list)
    answer = []
    for r in set(report):
        i, d = r.split()
        dic[i].append(d)
        cnt[d] += 1
    for id_ in id_list:
        num = 0
        for r in dic[id_]:
            if  k < cnt[r]:
                num += 1
        answer.append(num)
    return answer
