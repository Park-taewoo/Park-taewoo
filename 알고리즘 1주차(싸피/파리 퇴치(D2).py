def solve():
    arr_N = []
    max_catch = 0  # 파리를 잡은 최댓값 변수 설정
    for i in range(N): # N x N 파리 영역 생성
        A = list(map(int, input().split()))
        arr_N.append(A)
    for i in range(N - M + 1):  #파리채가 갈 수 있는 만큼 영역 제한
        for j in range(N - M + 1):
            catchparis = 0
            for k in range(M):
                for a in range(M):  #파리채의 크기만큼 순회하면서 파리 잡기
                    catchparis += arr_N[i+k][j+a]
            if catchparis > max_catch:
                max_catch = catchparis
    return max_catch


T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    result = solve()
    print(f'#{tc} {result}')
