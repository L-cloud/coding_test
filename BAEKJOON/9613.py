import sys

def get_GDC(a:int, b:int):
    if b == 0:
        return a
    gdc = get_GDC(b, a % b)
    return gdc


for _ in range(int(sys.stdin.readline())):
    GCD_sum = 0
    num, *test_case = list(map(int, sys.stdin.readline().split()))
    test_case.sort(reverse=True)
    for i in range(len(test_case)):
        for j in range(i+1, len(test_case)):
            GCD_sum += get_GDC(test_case[i], test_case[j])
    
    print(GCD_sum)
