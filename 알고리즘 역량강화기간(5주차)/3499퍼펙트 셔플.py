# 투포인트 알고리즘
# a = 맨처음
# b = 중간 +1


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr = list(map(int,input().split()))
    a = 0
    b =(len(arr)+1)//2
    result = solve()
    print(f'#{tc} {result}')

