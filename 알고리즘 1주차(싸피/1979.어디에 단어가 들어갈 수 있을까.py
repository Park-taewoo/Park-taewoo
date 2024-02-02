T= int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr=[list(map(int,input().split())) ]
    N +=1
    ans = 0
    for i in range(N):
        for j in range(N):
            