# bisect쓰는게 훨씬 더 효율적
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
numbers = []
while True:
    try:
        numbers.append(int(input()))
    except:
        break

def postorder(left, right):
    if right <= left:
        return
    right_index = left + 1
    for i in range(right_index, right):
        if numbers[left] < numbers[i]:
            right_index = i
            break
    postorder(left + 1,right_index)
    postorder(right_index,right)
    print(numbers[left])
postorder(0,len(numbers))
