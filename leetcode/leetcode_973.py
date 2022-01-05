class Solution:
    def distance(self, x, y):
        return x**2 + y **2
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key = lambda x: self.distance(x[0],x[1]))[:k]
