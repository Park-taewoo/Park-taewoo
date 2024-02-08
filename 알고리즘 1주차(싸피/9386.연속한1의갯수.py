T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers=list(map(int,input()))
    cnt=0
    max_num=0
    for i in numbers:
        if i == 1:
            cnt +=1
            if max_num < cnt:
                max_num = cnt
        elif i == 0:
            cnt = 0
    print(f'#{tc} {max_num}')


