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


