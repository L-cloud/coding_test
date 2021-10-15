import collections
import heapq
def solution(jobs):
    jobs = collections.deque(sorted(jobs,key=lambda x:x[0]))
    time, answer, jobs_len = 0, 0, len(jobs)
    hq = []
    while jobs or hq != []:
        while jobs and jobs[0][0] <= time:
            job = jobs.popleft()
            heapq.heappush(hq,(job[1],job))# shortest length get upside ex (3,[0,3])
        if hq == []:
            time += jobs[0][0] - time # plus waiting time
            continue
        next_job = heapq.heappop(hq)[1] # [0,3]
        answer += time - next_job[0] + next_job[1]
        time += next_job[1]
    return int(answer / jobs_len)