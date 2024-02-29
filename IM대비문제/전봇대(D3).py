T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # for _ in range(N):
    #     for i in range(N - 1):
    #           if arr[i][0] > arr[i + 1][0]:
    #             arr[i], arr[i + 1] = arr[i + 1], arr[i]
    arr.sort(key=lambda x : x[0]) # arr[0]번쨰 기준으로 오름차순으로 정렬

    for i in range(N - 1):
        for j in range(i+1,N):
            if arr[i][1] > arr[j][1]:
                cnt += 1

    print(f'#{tc} {cnt}')