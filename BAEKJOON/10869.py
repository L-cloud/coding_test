n,m = map(int,input().split())
print("\n".join(list(map(str,[n+m,n-m,n*m,int(n/m),n%m]))))
