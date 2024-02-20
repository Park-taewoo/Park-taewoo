def in_order(v):
    global cnt
    if v > N:
        return

    in_order(v * 2)  # 왼쪽
    tree[v] = cnt
    cnt += 1
    in_order(v * 2 + 1)  #


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [None] * (N + 1)
    cnt = 1
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')