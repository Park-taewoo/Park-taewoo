def solve(num,a,b):
    if num == N :
        return
    for k in range(N):
        if 0<=a-1<N and <=b-1<N:
        
    
    for i in range(N):
        if vistied[i] == 0:
            vistied[i] =1
            N_queen[num][i]=0
            solve(num+1,num,i)
            vistied[i]=0
            N_queen[num][i]=-1
for tc in range(1,int(input())+1):
    N=int(input())
    N_queen=[[-1]*N for _ in range(N)]
    vistied=[0]*N
    result=solve(0,0,0)
    print(f'#{tc} {result}')    