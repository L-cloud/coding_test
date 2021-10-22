from typing import List
def solution(people : List, limit : int) -> int:
    answer = 0
    people.sort()
    while people:
        boat = list(filter(lambda x : limit - x - people[0] >= 0, people[:-1]))
        if boat:
            people.remove(boat[-1])
        people.pop()
        answer += 1
    return answer
