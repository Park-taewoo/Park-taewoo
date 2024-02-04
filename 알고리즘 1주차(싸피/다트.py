T=int(input())  
for tc in range(T):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    cnt =0
    li =[]
    for i in range(N):
        for j in range(N):
            cnt=0
            if j-1>=0: #좌
                cnt += arr[i][j-1]
            if j+1<N: #우
                cnt += arr[i][j+1]
            if i-1 >=0: #상
                cnt += arr[i-1][j]
            if i+1 < N: #하 
                cnt += arr[i+1][j]
            cnt = cnt -arr[i][j]
            
            if cnt%2==0: #짝수면 두배이벤트
                cnt = cnt*2
            if cnt < 0:
                cnt = 0 
            if i==0 or i ==N-1 or j == 0 or j ==N-1:
                cnt = 0
            li.append(cnt)
    print(f'#{tc} {max(li)}')
    