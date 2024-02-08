def solve():
    arr=[list(map(int,input().split())) for _ in range(N)]
    r1 = [-1,1,0,0] #상하좌우
    c1 = [0,0,-1,1]
    cnt = 0
    max_num=0
    r,c = 0,0
    for i in range(N):
        for j in range(M):
            cnt = 0
            cnt += arr[i][j]
            for k in range(1,arr[i][j]+1):
                for a in range(4):
                    dr = i+r1[a]*k
                    dc = j+c1[a]*k
                    if 0<= dr < N and 0<= dc < M:
                        cnt += arr[dr][dc]
            if cnt>max_num:
                max_num = cnt
    return max_num



T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    reult=solve()
    print(f'#{tc} {reult}')