def solve():
    A=len(arr)
    B=A//2
    new_lst=[0]*A
    for i in range(B):


    return new_lst


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(str,input().split()))
    reult =solve()
    print(f'#{tc} {reult}')