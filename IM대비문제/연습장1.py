def solve():
    d1=[-1,1,0,0]
    d2=[0,0,-1,1] #상하좌우
    d3=[-1,-1,1,1]
    d4=[-1,1,-1,1]
    max_num=0
    max_num1 =0
    god = 0
    for i in range(N):
        for j in range(N):
            cnt =arr[i][j]
            for k in range(1,M):
                for q in range(4):
                    r= i +d1[q]*k
                    c= j +d2[q]*k
                    if 0<=r<N and 0<=c<N:
                        cnt+=arr[r][c]
                if max_num < cnt:
                    max_num = cnt   
                                         
    for i in range(N):
        for j in range(N):
            cnt =arr[i][j]
            for k in range(1,M):
                for q in range(4):
                    r= i +d3[q]*k
                    c= j +d4[q]*k
                    if 0<=r<N and 0<=c<N:
                        cnt+=arr[r][c]
                if max_num1< cnt:
                    max_num1 = cnt
    
    if max_num1 < max_num:
        god = max_num
    else:
        god = max_num1         
    return god

T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=solve()
    print(f'#{tc} {result}')
    
    