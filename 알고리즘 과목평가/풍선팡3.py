def solve():
    d1=[-1,1,0,0]
    d2=[0,0,-1,1] # 상하좌우
    r,c= 0,0
    max_sum=0
    min_sum=999
    for i in range(N):
        for j in range(N):
            b=arr[i][j]
            d = 0
            e = 0
            d += arr[i][j]
            e += arr[i][j]
            for k in range(1,b+1):
                for q in range(4):
                    r = d1[q]*k
                    c = d2[q]*k
                    if 0<= i+r < N and 0<= j+c < N:
                        d += arr[i+r][j+c]
                        e += arr[i+r][j+c]                    
            if  max_sum <= d:
                max_sum = d
            if min_sum >= e:
                min_sum = e
    return ((max_sum)-(min_sum))                


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')