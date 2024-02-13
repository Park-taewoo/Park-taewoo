#0에서 99로 가는 경로가 있는지 없는지 1,0으로 표시
def solve():
    stack = [0]
    visited = [0] * (100)
    visited[0] = 1

    while stack:
        current = stack[-1]
        if current == 99:
            return 1
        #현재 노드에서 할 수 있는 모든 경로 탐색
        for i in range(2):
            # print(current)
            if adj[i][current] != -1 and not visited[adj[i][current]]:
                stack.append(adj[i][current])
                visited[adj[i][current]] = 1
                break
        else:
            stack.pop()
    return 0



T = 10
for _ in range(T):
    tc, E = map(int,input().split())
    adj = [[-1] * 100 for _ in range(2)]
    # adj[0] >>각 인덱스에 첫번째 연결된 정점 정보
    # adj[1] >>각 인덱스에 두번째 연결된 정점 정보
    data = list(map(int,input().split()))
    for i in range(0,E*2,2):
        a, b = data[i],data[i+1]
        # 이미 0번에 다른 노드로 가는 정보가 저장되어있으면 1번에 저장
        if adj[0][a] == -1:
            adj[0][a] = b
        else:
            adj[1][a] = b
    #0에서 99로 가는 경로가 있는지 없는지 1,0으로 표시
    result = solve()
    print(f'#{tc} {result}')
