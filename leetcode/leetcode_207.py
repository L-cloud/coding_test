class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        dic, visited = collections.defaultdict(list),[]
        for num in prerequisites:
            if num[0] == num[1]:
                return False
            dic[num[0]].append(num[1])
        
        def dfs(num):
            while dic[num]:
                next_num = dic[num].pop()
                if next_num in visited:
                    return False
                visited.append(next_num)
                if not dfs(next_num):
                    return False
                visited.pop()
            return True
        
        for key in list(dic.keys()):
            visited.append(key)
            if not dfs(key):
                return False
            visited.pop()
        return True
