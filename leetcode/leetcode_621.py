import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        count = collections.Counter(tasks)
        for_erase = collections.Counter()
        time = 0
        while True:
            task_key = count.most_common(n + 1)
            task = 0
            for i in range(n + 1):
                if task_key:
                    count[task_key.pop(0)[0]] -= 1
                    task += 1
                time += 1
            count += for_erase
            if not count:
                return time - (n + 1 - task)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        time = 0
        while count:
            pass_num = 0
            for key,value in count.most_common(n + 1):
                count[key] -= 1
                time += 1
                pass_num += 1
            count += collections.Counter()
            if count:
                time += n + 1 - pass_num
        return time
