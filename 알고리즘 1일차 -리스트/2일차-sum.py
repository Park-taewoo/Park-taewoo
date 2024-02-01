for test_case in range(1, 10 + 1):
    num = int(input())
    lst = []
    rng = 100
    for i in range(rng):
        lst.append(list(map(int,input().split())))
 
 
    # 행 합구하기
    mx_row = 0
    for j in lst:
        tot_row = 0
        for rw in j:
            tot_row += rw
        if tot_row > mx_row:
            mx_row = tot_row
    # mx_row = 행 최대합
    # 열 합구하기
    mx_col = 0
    for k in range(rng):
        tot_col = 0
        for l in range(rng):
            tot_col += lst[l][k]
        if tot_col > mx_col:
            mx_col = tot_col
 
    # 대각선 합구하기
    mx_diagnol = 0
    tot_diagnol_r = 0
    tot_diagnol_l = 0
    for a in range(rng):
        tot_diagnol_l += lst[a][a]
        tot_diagnol_r += lst[a][rng-1-a]
 
    #print(mx_row,mx_col,tot_diagnol_r,tot_diagnol_l)
    tot_mx = 0
    for i in [mx_row,mx_col,tot_diagnol_r,tot_diagnol_l]:
        if tot_mx < i:
            tot_mx = i
    print(f"#{test_case} {tot_mx}")