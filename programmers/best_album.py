import collections
def solution(genres, plays):
    cnt,dic,answer = collections.Counter(),collections.defaultdict(list), []
    for i in range(len(genres)):
        cnt[genres[i]] += plays[i]
        dic[genres[i]].append([i, plays[i]])
    for key, value in cnt.most_common():
        for index, play in sorted(dic[key], key = lambda  x: (-x[1] , x[0]))[:2]:
            answer.append(index)
    return answer