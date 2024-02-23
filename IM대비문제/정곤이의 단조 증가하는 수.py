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
    if N == 1:
        nono = 0

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
                        if cnt ==len(A) and sum < c:
                            sum = c
                D=0
    else:
        sum = -1
    # else:
    #     A=str(arr[0])
    #     b=0
    #     for i in A:
    #         if b <= int(i):
    #             b = int(i)
    #             sum = A
    #         if b> int(i):
    #             sum = -1
    print(f'#{tc} {sum}')

