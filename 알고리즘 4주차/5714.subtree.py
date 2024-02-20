def solve(N):
    global cnt
    if g[N][0] != None:
        cnt +=1
        solve(g[N][0])
    if g[N][1] !=None:
        cnt +=1
        solve(g[N][1])


T=int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split())
    g =[[None]*(2) for _ in range(E+2)]
    arr = list(map(int,input().split()))
    for i in range(0,E*2,2):
        if not g[arr[i]][0]:  # 왼쪽 자식에 대한 정보를 가지고 있지 않음
            g[arr[i]][0] = arr[i + 1]
        else:  # 왼쪽 자식에 대한 정보를 이미 가지고 있음
            g[arr[i]][1] = arr[i + 1]
    cnt = 1
    solve(N)
    print(f'#{tc} {cnt}')