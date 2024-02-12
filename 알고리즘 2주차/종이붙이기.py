def solve(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return solve(N-10) + solve(N-20)*2
 
T = int(input())
for tc in range(1,T+1):
     result = solve(int(input()))
     print(f'#{tc} {result}')