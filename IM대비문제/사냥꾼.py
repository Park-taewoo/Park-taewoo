def solve():
    d1=[-1,1,0,0,-1,-1,1,1] #상하좌우대각
    d2=[0,0,-1,1,-1,1,-1,1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:  # 사냥꾼 위치 찾아서 반복문 
                for w in range(8):
                    for q in range(1,N+1):
                        r=i+d1[w]*q
                        c=j+d2[w]*q
                        if 0<=r<N and 0<=c<N and arr[r][c]==3: #만약 돌을 만나면 for문 종료
                            break
                        elif 0<=r<N and 0<=c<N and arr[r][c] == 2: #토끼 잡았으면 횟수증가
                            cnt+=1

    return cnt

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=solve()
    print(f'#{tc} {result}')