for tc in range(1,int(input())+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    vistied =[999999999]*(V+1)
    vistied[0]=0
    for a,b,c in arr:
        if vistied[b]>vistied[a]+c:
            vistied[b]=vistied[a]+c
    print(f'#{tc} {vistied[-1]}')



