def solve():
    for i in range(0,12,3):
        

T=int(input())
for tc in range(1,T+1):
    arr=list(input())
    result=solve()
    print(f'#{tc} {result}')