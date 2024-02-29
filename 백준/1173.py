N,m,M,T,R = map(int,input().split())
cnt = 0
cnt1 = 0
k=m
if k+T > M:
    cnt = -1
while True:
    if cnt == -1 or cnt == N:
        break
    if k+T<=M:
        k += T
        cnt +=1
    else:
        k -= R
        if k < m:
            k = m
        cnt1 +=1


print(cnt+cnt1)

