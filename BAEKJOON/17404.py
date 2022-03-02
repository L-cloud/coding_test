import sys
from typing import List
class Price:
    def __init__(self):
        self.min_price = float('inf')
def dfs(start_color : int, color : int, price : int, price_class :Price ,house: List[int]) -> None:
    if len(house) == 1:
        if start_color == color:
            return
        price += house[0][color]
        price_class.min_price = min(price, price_class.min_price)
        return
    if color == 0:
        dfs(start_color,1,price + house[0][0], price_class, house[1:])
        dfs(start_color, 2, price + house[0][0], price_class, house[1:])
    if color == 1:
        dfs(start_color, 0, price + house[0][1], price_class, house[1:])
        dfs(start_color, 2, price + house[0][1], price_class, house[1:])
    if color == 2:
        dfs(start_color, 1, price + house[0][2], price_class, house[1:])
        dfs(start_color, 0, price + house[0][2], price_class, house[1:])

houses = []

for _ in range(int(sys.stdin.readline())):
    houses.append(list(map(int, sys.stdin.readline().split())))

price_class = Price()
dfs(0, 0, 0, price_class,houses)
dfs(1, 1, 0, price_class,houses)
dfs(2, 2, 0, price_class,houses)

print(price_class.min_price)