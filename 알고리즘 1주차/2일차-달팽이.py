def solve():
    r,c = 0,0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    arr = [[0]*N for _ in range(N)]
    cnt = 0
    move_p = 0
    while 1:
        if cnt == N**2:
            break
        try:
            cnt += 1
            arr[r][c] = cnt
            r = r + dr[move_p]
            c = c + dc[move_p]
            # elif move_p ==1:
            #     arr[r][c] = cnt
            #     r = r + dr[1]
            #     c = c + dc[1]
            # elif move_p == 2:
            #     arr[r][c] = cnt
            #     r = r + dr[2]
            #     c = c + dc[2]
            # else:
            #     arr[r][c] = cnt
            #     r = r + dr[3]
            #     c = c + dc[3]
        except IndexError:
            move_p +=1
            move_p = move_p%4

    return arr







T=int(input())
for i in range(1,T+1):
    N=int(input())
    result=solve()
    print(f'#{i} {result}')
