T=10
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    value=999
    while value != 0:
        for i in range(1,6):
            value = arr.pop(0)-i
            if value <= 0:
                value =0
            arr.append(value)
            if value == 0:
                break
    print(f'#{tc}', *arr)
