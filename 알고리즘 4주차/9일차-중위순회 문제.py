T=10
for tc in range(1,T+1):
    N=int(input())
    arr=[input().split() for _ in range(N)]
    print(arr)
    arr_2 = []
    for i in range(len(arr)):
        arr_2.append(arr[i][2:])
    print(arr_2)
    g = [[None]*2 for _ in range(N+1)]
