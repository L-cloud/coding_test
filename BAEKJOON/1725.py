import sys
'''
-> 자기 보다 작은거 만나면 pop()해줌 그리고 해당 *인덱스 - 자기 인덱스 + 1) * 자기 높이 해줌
마지막에 인덱스 + 1 0 push 해줘야함
함수화 해서 왼쪽 오른쪽 둘 다 해주자
흐음.. 함수화로 해서 푸는 것을 연습해야하나?
'''

input = sys.stdin.readline
N = int(input())
m = [int(input()) for _ in range(N)]
size = [0] * N
s = []
def pop_stack(index:int, value:int) -> None:
    while s and value < s[-1][1]:
        i,v = s.pop()
        size[i] += (index - i) * v

def pop_stack2(index:int, value:int):
    while s and value < s[-1][1]:
        i,v = s.pop()
        size[-i-1] += (index-i) * v
for i,v in enumerate(m):
    if s and v < s[-1][1] :
        pop_stack(i,v)
    s.append((i,v))
pop_stack(N,0)
for i,v in enumerate(m[::-1]):
    if s and v < s[-1][1] :
        pop_stack2(i-1,v)
    s.append((i,v))
pop_stack2(N-1,0)
print(max(size))








