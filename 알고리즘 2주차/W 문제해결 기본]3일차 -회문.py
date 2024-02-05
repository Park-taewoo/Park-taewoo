T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr = [list(map(str,input())) for _ in range(N)]
    arr_2 = [item[::-1] for item in arr]

    for i in range(len(arr)):
        if arr[i] == arr_2[i]:
            print(f'#{tc} {"".join(arr[i])}')