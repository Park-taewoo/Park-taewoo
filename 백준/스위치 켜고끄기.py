N=int(input())
arr=list(map(int,input().split()))
M= int(input())
for i in range(M):
    A,B = map(int,input().split())
    if A == 1:
        C=B-1
        while C<N:
            arr[C] = 1-arr[C]
            C =C+B
    elif A == 2:
        C = B-1
        q = 1
        arr[C]=1-arr[C]
        while 0<=C+q<N and 0<=C-q<N :   
            if arr[C-q] == arr[C+q]:
                arr[C-q] = 1-arr[C-q]
                arr[C+q] = 1-arr[C+q]
                q += 1     
            else:
                break              
              
for k in range(1,N+1):
    print(arr[k-1], end=" ")
    if k % 20 == 0:
        print()
