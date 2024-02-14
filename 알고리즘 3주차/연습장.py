def solve(row):
    if out and A_list and sum(A_list) > min(out):
        return
    for i in range(N):
        if not x[i] and not y[i]:
            A_list.append(arr[row][i])

            if len(A_list) == N:
                out.append(sum(A_list))
            x[i] = 1
            y[i] = 1
            solve(row + 1)

            A_list.pop()

            x[i] = 0
            y[i] = 0
    return


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A_list = []
    out = []
    x = [0] * N
    y = [0] * N
    solve(0)
    print(f'#{tc + 1} {min(out)}')