def solve():
    lst = []
    final_lst = []
    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                lst.append(arr[j][i])
            if arr[j][i] == 2:
                if lst:
                    final_lst.append(arr[j][i])
                    lst.clear()
        lst.clear()
    return len(final_lst)

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')