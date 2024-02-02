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
            if arr[r][c] != 0:
                r = r - dr[move_p]
                c = c - dc[move_p]
                move_p += 1
                move_p= move_p% 4              
                r = r + dr[move_p]
                c = c + dc[move_p]     
            cnt += 1
            arr[r][c] = cnt
            r = r + dr[move_p]
            c = c + dc[move_p]
        except IndexError:
            r = r - dr[move_p]
            c = c - dc[move_p]
            move_p +=1
            move_p = move_p % 4
            r = r + dr[move_p]
            c = c + dc[move_p]            

    
    return arr
        
    
    




T = int(input())
for i in range(1, T + 1):
    N = int(input())
    result = solve()
    print(f'#{i}')
    # 각 행을 문자열로 변환하여 출력
    for row in result:
        print(" ".join(map(str, row)))