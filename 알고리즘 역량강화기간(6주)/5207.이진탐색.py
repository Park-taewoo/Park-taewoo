def solve(target):
    low=0
    high=len(A)-1
    global cnt
    c=0
    # if target == low or target == high:
        # return
    while low<=high:
        mid=(low+high)//2
        if A[mid]==target:
            cnt+=1
            return 
        elif A[mid] > target and c!=1:
            high = mid -1
            c=1
        elif A[mid]<target and c!=2:
            low = mid +1
            c=2
        else:
            return


T=int(input())

for tc in range(1,T+1):
    N,M= list(map(int,input().split()))
    A =list(map(int,input().split()))
    B =list(map(int,input().split()))
    cnt=0
    A.sort()
    # c=[0]*500000
    for i in B:
        # if c[B[i]]==0:
        solve(i)
            # c[B[i]]=1
    print(f'#{tc} {cnt}')