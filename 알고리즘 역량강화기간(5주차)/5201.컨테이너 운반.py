def solve():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if weight[i]<=truck[j]:
                cnt +=weight[i]
                truck[j] =0
                break
    return cnt




T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    weight = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    weight.sort()
    truck.sort()
    weight.reverse()
    truck.reverse()
    result = solve()
    print(f'#{tc} {result}')
