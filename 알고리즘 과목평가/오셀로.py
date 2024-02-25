T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        i, j, k = map(int, input().split())
        if k == 1:
            # 1번 작업: i번째부터 j개 돌 뒤집기
            for x in range(j):
                if i-1+x < N:
                    arr[i-1+x] = 1 - arr[i-1+x]
        elif k == 2:
            # 2번 작업: i번째부터 j개 돌을 i번째 돌 색으로 변경
            for x in range(j):
                if i-1+x < N:
                    arr[i-1+x] = arr[i-1]
        elif k == 3:
            # 3번 작업: i번째 돌을 중심으로 양쪽 j개 돌을 검사하고 같은 색이면 뒤집기
            for x in range(1, j+1):
                if i-1-x >= 0 and i-1+x < N and arr[i-1-x] == arr[i-1+x]:
                    arr[i-1-x] = 1 - arr[i-1-x]
                    arr[i-1+x] = 1 - arr[i-1+x]
    print(f'#{t}', *arr)


# 3
# 5 1
# 0 0 0 0 0
# 2 2 1
# 5 1
# 0 1 0 0 0
# 2 3 2
# 10 4
# 0 1 1 0 0 1 0 1 0 1
# 3 2 1
# 5 3 2
# 4 4 3
# 8 4 1
