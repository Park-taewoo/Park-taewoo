T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    A = len(arr)
    # 행 열 검사
    result = 1
    for i in range(A):
        r_sum = 0
        c_sum = 0
        for j in range(A):
            r_sum += arr[i][j]  # 열검사
            c_sum += arr[j][i]  # 행검사
        if r_sum != 45 or c_sum != 45:
            result = 0

    # 3x3 검사
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            total = 0
            for k in range(j, j + 3):
                sum = arr[i][k] + arr[i + 1][k] + arr[i + 2][k]
                total += sum

            if total != 45:
                result = 0

    print(f'#{tc} {result}')
