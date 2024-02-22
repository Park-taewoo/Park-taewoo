T = int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    c=0
    nono=1
    # for i in arr: #단조 증가인지 확인
    #     if c<=i:
    #         c=i
    #     else:
    #         nono=0
    sum=-1
    D=0

    if nono==1: #단조 증가하는 수이면
        for i in range(len(arr)-1):
            c=arr[i]*arr[i+1]
            A=str(c) #단조증가 곱을 받음
            cnt=0
            if sum<c:
                for j in A: #곱이 단조 인지 확인
                    if D <= int(j) :
                        cnt +=1
                        D=int(j)
                        d = arr[i]*arr[i+1]
                        if cnt ==len(A) and sum < d:
                            sum = d
                D=0
    print(f'#{tc} {sum}')

