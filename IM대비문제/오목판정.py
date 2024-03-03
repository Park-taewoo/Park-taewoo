def solve():
    d1=[0,1,1,1]  #오른쪽,아래,오른쪽아래 대각 왼쪽아래 대각
    d2=[1,0,1,-1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for q in range(4):
                    cnt=0
                    r = i
                    c = j
                    while 0<=r<N and 0<=c<N and arr[r][c]=='o': 
                        cnt+=1
                        r= r+d1[q]
                        c= c+d2[q]
                    if cnt ==5:
                        return 'YES'

    return 'NO'          
    
    
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(str,input())) for _ in range(N)]
    result=solve()
    print(f'#{tc} {result}')