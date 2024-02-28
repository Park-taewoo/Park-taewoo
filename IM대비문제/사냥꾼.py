def solve():
    d1=[-1,1,0,0,-1,-1,1,1] #상하좌우대각
    d2=[0,0,-1,-1,-1,1,-1,1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                for w in range(8):
                    for q in range(1,N):
                        r=i+d1[w]*q
                        c=j+d2[w]*q
                        if 0<=r<N and 0<=c<N and arr[r][c]==3:
                            break
                        if 0<=r<N and 0<=c<N and arr[r][c]==1:
                            break
                        elif 0<=r<N and 0<=c<N and arr[r][c] == 2:
                            cnt+=1

    return cnt

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=solve()
    print(f'#{tc} {result}')