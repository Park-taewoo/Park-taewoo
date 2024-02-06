def solve():
    cnt = 0
    #행검사
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if data[i][j+k] != data[i][j+M-1-k]:
                    break
            else:
                cnt +=1
    #열 검사
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M // 2):
                if data[j + k][i] != data[j + M - 1 - k][i]:
                    break
            else:
                cnt +=1
    return cnt

for tc in range(1,11):
    N = 8
    M = int(input())
    data=[input() for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')