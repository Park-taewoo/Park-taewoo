def solve():
    for i in range(M):
        value=arr.pop(0)
        arr.append(value)
    return arr[0]
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr = list(map(int,input().split()))
    result=solve()
    print(f'#{tc} {result}')