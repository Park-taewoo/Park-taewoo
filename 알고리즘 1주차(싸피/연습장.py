# T=int(input())
# for tc in range(1,T+1):
#     N=list(map(int,input()))
#     cnt=0
#     cnt_2=0
#     arr=[0]*10
#     sum=0
#     for i in N:
#         arr[i]+=1
#     print(arr)
#     for j in range(10):
#         while arr[j]>=3:
#             cnt+=1
#             arr[j]-=3
#             print('a')
#         while j<=7 and arr[j]>0 and arr[j+1]>0 and arr[j+2]>0:
#             cnt_2 += 1
#             arr[j]-=1
#             arr[j+1]-=1
#             arr[j+2]-=1
#             print('b')
#     if cnt+cnt_2==2:
#         sum=True
#         print(f'{tc} {sum}')
#     else:
#         print(f'{tc} false')   

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    cut=0
    li=[]
    print(arr)
    for i in range(N):
        for j in range(N):
            cut=0
            if j-1>=0:
                cut += arr[i][j-1]
            if j+1<N:
                cut += arr[i][j+1]          
            if i-1>=0:
               cut += arr[i-1][j]
            if i+1<N:
                cut += arr[i+1][j]
           
            cut = cut-arr[i][j]
            if cut%2==0:
                cut=cut*2
            if cut <0:
                cut = 0
            if i==0 or i ==N-1 or j == 0 or j ==N-1:
                cut = 0
            li.append(cut)
            print(li)
    print(f'{tc} {max(li)}')
                