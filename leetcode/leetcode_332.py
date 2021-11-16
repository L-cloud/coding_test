class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key = lambda x : (x[0], x[1]))
        dic,visited,flights = collections.defaultdict(list),collections.defaultdict(list) ,[]
        for ticket in tickets:
            dic[ticket[0]].append(ticket[1])
            visited[ticket[0]].append(False)
        def dfs(start:str):
            flights.append(start)
            if len(tickets) + 1 == len(flights):
                return True
            for index,flight in enumerate(dic[start]):
                if visited[start][index]: # to check visited
                    continue
                else:
                    visited[start][index] = True
                if dfs(flight):
                    return True
                flights.pop()
                visited[start][index] = False
            return False
        dfs("JFK")
        return flights
