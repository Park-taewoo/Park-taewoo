def solve():
    
    new_list=[]
    for _ in range(100) :
        new_list.append(list(map(int,input().split())))  # 배열값 받기
        
         
    max_c = 0 #열 최대값 구하기
    for h in range(100):
        sum_c=0
        for k in range(100):
            sum_c+=new_list[k][h]
            if sum_c > max_c :
                max_c = sum_c
    max_r = 0 #행 최대값 구하기
    for k in new_list:
        sum_r = 0
        for g in k:
            sum_r += g
        if sum_r > max_r:
            max_r = sum_r
    
    tot_diagnol_r = 0 #대각선 최대값 구하기
    tot_diagnol_l = 0
    for a in range(100):
        tot_diagnol_l += new_list[a][a]
        tot_diagnol_r += new_list[a][100-1-a]
    
    #대각 , 행 ,열 중에서 가장 큰 값 선정
    tot_max = 0
    for i in [max_r,max_c,tot_diagnol_r,tot_diagnol_l]:
        if tot_max < i:
            tot_max = i 
    return tot_max
    


for i in range(10):
    M = int(input())
    result=solve()
    print(f'#{M} {result}')