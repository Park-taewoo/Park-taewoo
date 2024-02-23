def solve(N):
    i = 1/2
    cnt = 0
    st=''
    while True:
        if N >= i:
            st += '1'
            N = N-i
            cnt+=1
            i = i*(1/2)
        else:
            st += '0'
            cnt += 1
            i = i * (1 / 2)
        if N <=0:
            break
        if cnt >=13 :
            return 'overflow'
    return st

T=int(input())
for tc in range(1,T+1):
    N=float(input())
    result = solve(N)
    print(f'#{tc} {result}')