def solve():
    d1 = [-1,1,0,0] #상하좌우
    d2 = [0,0,-1,1]
    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            cnt += arr[i][j]
            for k in range(1,arr[i][j]+1):
                for q in range(4):
                    r = i+d1[q]*k
                    c = j+d2[q]*k
                    if 0<=r<N and 0<=c<M:
                        cnt+= arr[r][c]
                        if max_v < cnt :
                            max_v = cnt  
    return max_v


T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=solve()
    print(f'#{tc} {result}')