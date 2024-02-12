def solve(start):
    stack = [start] #경로저장을 위해서 stack이 필요
    visited = [0]*(V+1) #방문 표시 배열,중복방분을 방지
    visited[start] = 1 #방문했다 표시
    while stack: #스택이 있으면 무한반복
        current = stack[-1] 
        for i in range(V+1):
            if adj[current][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
    return visited

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    
    lst = [list(map(int, input().split())) for _ in range(E)]
    data = []
    adj = [[0]*(V+1) for _ in range(V+1)]
    for a in lst:
        data.append(a[0])
        data.append(a[1])
        
    S, G = map(int, input().split())

    for i in range(0,E*2,2):
        adj[data[i]][data[i+1]] = 1

    
    result = solve(S)
    if result[G] == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')