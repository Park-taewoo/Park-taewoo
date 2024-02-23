T=int(input())
for tc in range(1,T+1):
    N= int(input())
    arr=list(map(int,input().split()))
    cnt = 1
    max_cnt =1
    for i in range(N-1):
        if arr[i] < arr[i+1]:
            cnt+=1
        else:
            cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')