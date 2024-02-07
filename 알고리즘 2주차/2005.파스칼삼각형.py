def solve():
    cnt=0
    for i in range(N):
        cnt+=1
        return cnt



T=int(input())
for tc in range(1,T+1):
    N = int(input())
    result =solve()
    print(f'#{tc} {result}')