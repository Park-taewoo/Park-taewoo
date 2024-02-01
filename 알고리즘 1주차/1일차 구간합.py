def solve():
    max_v = 0
    min_v = 1000000
    #시작점 반복
    for i in range(0, N-M+1):
        # i :구간의 시작점
        #M길이의 구간합 구하기
        sum_v = 0
        for j in range(i,i+M):
            sum_v += data[j]
        if sum_v > max_v:
            max_v = sum_v
        if sum_v < min_v:
            min_v = sum_v
    return  max_v - min_v

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    result = solve()
    print(f'#{tc} {result}')