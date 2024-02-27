T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v = 0
    min_v = 10000000
    for i in range(N-M+1):
        sum_v = 0
        for j in range(M):
            sum_v += arr[i+j]
        if min_v > sum_v:
            min_v = sum_v
        if max_v < sum_v:
            max_v = sum_v
    print(f'#{tc} {max_v - min_v}')