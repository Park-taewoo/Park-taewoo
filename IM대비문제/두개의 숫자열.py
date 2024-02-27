T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(2)]
    long_arr=[]
    short_arr=[]
    if N>M:
        long_arr = (arr[0])
        short_arr = (arr[1])
    else:
        long_arr = (arr[1])
        short_arr = (arr[0])
    A = len(long_arr) - len(short_arr)
    
    max_v  = 0   
    for i in range(A+1):
        max_num=0
        for j in range(len(short_arr)):
            max_num += long_arr[j+i]*short_arr[j]
        if max_v<max_num:
            max_v = max_num
    print(f'#{tc} {max_v}')   