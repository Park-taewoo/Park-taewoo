def solve(x,y,sum_num):
    global max_sum
    if max_sum < sum_num:
        return
    if x >= N or y >= N:
        return

    sum_num +=arr[x][y]

    if x==N-1 and y==N-1:
        if max_sum > sum_num:
            max_sum = sum_num
        return
    solve(x + 1, y, sum_num)
    solve(x,y+1,sum_num)


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_sum = 10*N
    result = solve(0,0,0)
    print(f'#{tc} {max_sum}')

