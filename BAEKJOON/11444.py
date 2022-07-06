def multiply(A,B):
    tempt = [0,0,0,0]
    tempt[0] = (A[0] * B[0] + A[1]*B[2]) % 1000000007
    tempt[1] = (A[0] * B[1] + A[1]*B[3]) % 1000000007
    tempt[2] = (A[2] * B[0] + A[3]*B[2]) % 1000000007
    tempt[3] = (A[2] * B[1] + A[3]*B[3]) % 1000000007
    return tempt



def fibo(N:int):
    if N == 1:
        return [1,1,1,0]
    if N % 2 == 0:# 짝수
        a = fibo(N // 2)
        return multiply(a,a)
    else:
        a = fibo(N // 2)
        multi = multiply(a,a)
        return multiply([1,1,1,0],multi)
        
N = int(input())
print(fibo(N)[1])