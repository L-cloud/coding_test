# 내가 생각한 알고리즘
'''
시발 모르겠다
일단 50 30 30 40 뭐 이렇게 있다고 가정해보자 len(pages)가 4 이상인 경우임
그런 경우에 최소 값 부터 하게 되면 50 60 40 이렇게 합쳐지는데 오히려 이럴 경우
60이 합쳐졌을 때의 최소값인 40 보다 크기 때문에 총 합이 커지는 경우가 발생한다.
60 + 100 + 150 // 이럴 경우 50 30 70을 해버린다면 70 + 80 + 150
하는건데.. 이러면 답이 틀림

최소 값을 만들어보고 그 값이 만들어 졌을 때의 리스트에서 최소값보다 큰 경우는 만들지 않는다.

'''
import sys
for _ in range(int(sys.stdin.readline())):
    page_num = int(sys.stdin.readline())
    pages = list(map(int, sys.stdin.readline().split())) # use stack?
    total = 0
    while 4 <= len(pages) : # 여기서 굳이 min_val 이 필요한가 인덱스로 접근하면 되는데?
        tempt = [pages[i] + pages[i + 1] for i in range(len(pages) - 1)] #O(n) # 사실 여기 그냥 for문 하나면 뒤에 꺼 안 해도 되는데 sorted 사용하면 min 안 찾아도 되고..
        h, sorted_tempt = pages[:], sorted(tempt)
        min_index, second_index = tempt.index(sorted_tempt[0]), tempt.index(sorted_tempt[1]) # 이 두개가 같으면?
        h[min_index] = sorted_tempt[1]
        del h[min_index + 1]
        if min(h) < sorted_tempt[0] : # 이러면 그냥 두번 째 꺼로 가야함 40 30 30 50 -> 40 60 50 같은 상황
            pages[second_index] = tempt[second_index]
            del pages[second_index + 1]
            total += pages[second_index]
        else: # 10 2 2 9 -> 10 4 9 같은 상황
            pages[min_index] = tempt[min_index]
            del pages[min_index + 1]
            total += pages[min_index]
    while 2 < len(pages) :
        tempt, min_val , min_index= [0,0], 20000, 0
        for i in range(2):
            tempt[i] = pages[i] + pages[i + 1]
            if tempt[i] < min_val:
                min_index = i
                min_val = tempt[i]
        pages[min_index] = min_val
        total += min_val
        del pages[min_index + 1]
    
    print(total + sum(pages))
                
                
        
    



            
            # 여기서 두  번 째  녀석 넣어야 하는데...

        