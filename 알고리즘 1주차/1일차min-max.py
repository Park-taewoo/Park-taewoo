T=int(input())

for i in range(T):
    N=int(input())   
    ai=list(map(int,input().split()))
    max_num = ai[0]
    min_num = ai[0]
    for j in range(N):
        if ai[j] > max_num:
            max_num = ai[j]
           
        elif ai[j] < min_num:
            min_num = ai[j]

    print(f'#{i+1} {max_num-min_num}')   