# https://gaussian37.github.io/math-algorithm-ccw/
# https://gaussian37.github.io/math-algorithm-line_intersection/
import sys
input = sys.stdin.readline
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
def line(x1:int,y1:int,x2:int,y2:int, x3:int,y3:int) -> bool:  # 직선 위에 점이 있는지 확인
    try: # 여기가 문제인건데
        graph = ((y2-y1)/(x2-x1))*(x3-x1) + y1
        if y3 -0.1<=graph <=y3 + 0.1 and min(x1,x2)<= x3 <=max(x1,x2):
            return True
        return False
    except ZeroDivisionError as e:
        return min(y1,y2) <= y3 <= max(y2,y1) and x3 == x1
def ccw(x1:int,y1:int,x2:int,y2:int) -> int: #2차원을 3차원처럼 외적
    cross_product = x1*y2 - x2*y1
    if cross_product > 0: # 반시계방향
        return 1
    elif cross_product < 0: # 시계방향
        return -1 
    else: # 일직선
        return 0
l1 = ccw(x2-x1,y2-y1,x3-x1,y3-y1) * ccw(x2-x1,y2-y1,x4-x1,y4-y1) # 한 직선에서 다른 직선까지 외적 방향
l2 = ccw(x4-x3,y4-y3,x4-x1,y4-y1) * ccw(x4-x3,y4 -y3, x4 -x2, y4 -y2)
if l1 <0 and l2 <0 : # 교차
    print(1)
elif (l1 == 0 and l2 !=0) or (l1 != 0 and l2 == 0): # 한 직선 상에 있음! 접하는지 아닌지 모름
    if line(x1,y1,x2,y2,x3,y3) or line(x1,y1,x2,y2,x4,y4) or  line(x3,y3,x4,y4,x1,y1) or  line(x3,y3,x4,y4,x2,y2):
        print(1)
    else:
        print(0)
elif l1 == 0 and l2 == 0: # 두 선이 모두 한 직선에 있음
    if x1 == x3: # 수평
        p1,p2,p3,p4 = min(y1,y2), max(y1,y2), min(y3,y4),max(y3,y4)
    else :    
        p1,p2,p3,p4 = min(x1,x2), max(x1,x2), min(x3,x4),max(x3,x4)
    if p3 <= p2 and p1 <= p4:
            print(1)
    else:
        print(0) 
else:
    print(0)


