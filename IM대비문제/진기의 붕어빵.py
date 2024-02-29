for tc in range(1, int(input()) + 1):
    # N = 사람수 , M= 붕어빵 굽는 시간 ,K=구워서 나온 붕어빵 갯수
    N, M, K = list(map(int, input().split()))
    times = list(map(int, input().split()))
    times.sort()

    for i in range(N):
        bread_cnt = (times[i]//M)*K
        if bread_cnt < i + 1:
            result= 'Impossible'
            print(f"#{tc} {result}")
            break
    else:
        result = "Possible"
        print(f'#{tc} {result}')