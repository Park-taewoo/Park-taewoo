for tc in range(1, int(input()) + 1):
    cnt = 0
    N = int(input())
    for i in range(-N, N + 1):
        for j in range(-N, N + 1):
            if i ** 2 + j ** 2 <= N ** 2:
                cnt += 1

    print(f"#{tc} {cnt}")