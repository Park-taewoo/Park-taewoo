T=int(input())
for tc in range(1,T+1):
    N=str(input())
    revers_N=''
    for i in N:
        revers_N = i + revers_N
    if N==revers_N:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')