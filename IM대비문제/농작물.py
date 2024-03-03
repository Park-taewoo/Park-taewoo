def solve():
    c = N//2
    cnt = 0
    for i in range(N):
        if i <= N//2:
            for j in range(0,i+1):
                if j !=0:
                    cnt += arr[i][c+j]
                    cnt += arr[i][c-j]
                else:
                    cnt+=arr[i][c]
        else:
            for j in range(N-i-1,-1,-1):
                if j != 0:
                    cnt += arr[i][c + j]
                    cnt += arr[i][c - j]
                else:
                    cnt += arr[i][c]
    return cnt




T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    result= solve()
    print(f'#{tc} {result}')