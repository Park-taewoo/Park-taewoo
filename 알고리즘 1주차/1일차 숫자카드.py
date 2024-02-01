T=int(input())

for i in range(1,T+1):
    N=int(input())
    ai=list(map(int,input()))
    cnt_lst=[0]*10

    for j in ai:
        cnt_lst[j] += 1

    cnt=cnt_lst[0]
    for index,big_num in enumerate(cnt_lst):
        if big_num >= cnt:
            cnt = big_num
            cnt_n = index
    print(f'#{i} {cnt_n} {cnt}')



