# idx 행에서 하나 선택하기
# tmp : 중간합
def solve(idx, tmp, check):
    global min_v
    if tmp >= min_v:
        return
    if idx == N:
        print(tmp)
        if min_v > tmp:
            min_v = tmp
        return
    # 하나 선택하고
    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            solve(idx + 1, tmp + arr[idx][i], check)
            check[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 3≤N≤10
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 100
    solve(0, 0, [0] * N)
    print(f'#{tc} {min_v}')