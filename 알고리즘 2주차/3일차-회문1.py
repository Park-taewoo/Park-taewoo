def solve():
    cnt = 0
    #행검사
    for i in range(N): # i번쨰 행에서 길이 M인 회문찾기
        for j in range(N-M+1): # j번 열에서 시작하는 길이 M인 회문찾기
            for k in range(M//2):
                if data[i][j+k] != data[i][j+M-1-k]:
                    break #회문아님
            else: #for k 반복문에서 break에 안걸렸음 회문이다.
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


