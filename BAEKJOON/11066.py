import sys
from typing import List, Dict


class Link:
    def __init__(self, value: int, right: int):
        self.value = value
        self.right = right


def min_sum(book: List[int]) -> int:
    book = [Link(v, i + 1) for i, v in enumerate(book)]
    total = 0
    for _ in range(len(book) - 1):
        box,c = [float('inf'), None], 0
        while c != len(book):
            if book[c].right < len(book) and book[c].value + book[book[c].right].value < box[0]:
                box = [book[c].value + book[book[c].right].value, c]
            c = book[c].right
        book[box[1]].value = box[0]
        total += box[0]
        book[box[1]].right = book[book[box[1]].right].right
    return total
input = sys.stdin.readline
for _ in range(int(input())):
    _, book = int(input()), list(map (int,(input().split())))
    print(min_sum(book))



