for tc in range(1,int(input())+1):
    V,E = map(int,input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b, w = map(int, input().split())
        adj[a][b] = w
        adj[b][a] = w

   
