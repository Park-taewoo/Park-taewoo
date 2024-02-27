def solve():
    d1 =[1,-1,0,0,-1,-1,1,1]#상하좌우 상왼쪽대각오른쪽대각 하왼쪽대각오른쪽대각
    d2 =[0,0,-1,1,-1,1,-1,1]
    cnt1=0
    for i in range(N):
        for j in range(M):
            cnt=0
            for q in range(8):
                r = i+d1[q]
                c = j+d2[q]
                if 0<=r<N and 0<=c<M and arr[i][j]>arr[r][c]:
                    cnt+=1
            if cnt >=4:
                cnt1 +=1 
                
    return cnt1

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=solve()
    print(f'#{tc} {result}')