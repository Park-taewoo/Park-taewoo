def solve():
    global cnt
    for i in range(1,A,2):
        if i+1 < A:
            if arr[i] >= arr[i+1]:
                cnt += 1

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(N):
        s,e = map(int,input().split())
        arr.append(s)
        arr.append(e)
    A=len(arr)
    print(arr)
    cnt=1
    solve()
    print(f'#{tc} {cnt}')
