T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    memo = [[0] * N for _ in range(N)]
 
    for n in range(N):
        for r in range(0, n + 1):
            if r == 0 or n == r:
                memo[n][r] = 1
            else:
                memo[n][r] = memo[n-1][r-1] + memo[n-1][r]
 
    print(f'#{tc}')
    for n in range(N):
        print(*memo[n][:n+1])