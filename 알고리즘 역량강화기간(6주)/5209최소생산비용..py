def solve(start,new_sum):
    global max_sum
    if max_sum <= new_sum:
        return
    if start==N:
        if max_sum >= new_sum:
            max_sum = new_sum
        return

    for i in range(N):
        if visited[i] ==0:
            visited[i]=1
            solve(start+1,new_sum+arr[start][i])
            visited[i]=0


for tc in range(1,int(input())+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    visited=[0]*N
    max_sum=100*N
    solve(0,0)
    print(f'#{tc} {max_sum}')

