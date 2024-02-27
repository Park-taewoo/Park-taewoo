def solve():
    d1=[-1,1,0,0,-1,-1,1,1] #상하좌우대각
    d2=[0,0,-1,-1,-1,1,-1,1]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                for q in range(1,N):
                    for w in range(8):
                        r=i+d1[w]*q
                        c=j+d2[w]*q
                        if arr[r][c]==3:
                            break
    pass

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=solve()
    print(f'#{tc} {result}')