def solve(N):
    crr=[]
    crr.append(brr[N])
    visited[N]=1
    c=[]
    if len(brr[N]) == 1:
        if brr[brr[N][0]] ==[]:
            return brr[N][0]
    while crr!=[[]]:
        a=crr.pop(0)
        c.clear()
        temp_list = []
        for i in a:
            if visited[i]==0:
                visited[i]=1
                if brr[i]:
                    for b in brr[i]:
                        if visited[b]==0:
                            temp_list.append(b)
                            c.append(b)
                # else:
                #     return i
        crr.append(temp_list)
        if crr ==[[]]:
            return d

        if c:
            d=max(c)
        else:
            return
    return d



for tc in range(1,11):
    A,B=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=[[] for i in range(101)]
    for i in range(0,A,2):
        brr[arr[i]].append(arr[i+1])

    visited=[0]*101

    a=solve(B)
    print(f'#{tc} {a}')