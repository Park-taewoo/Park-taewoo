def solve(z):
    if z==M:
        print(' '.join(map(str,data)))
        return
    for i in range(N):
        data.append(arr[i])
        solve(z+1)
        data.pop()


N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
data=[]
solve(0)
