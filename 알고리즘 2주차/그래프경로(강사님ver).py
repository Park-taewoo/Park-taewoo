# 주어진 시작점에서 목적지로 갈 수 있으면 1, 아니면 0을 반환
def solve(S, G, adj):
    # 경로를 저장할 수 있는 stack
    # 현재위치에서 방문할 수 있는 경로가 있다면 방문
    # 경로가 ㅇ벗다면 되돌아가서 경로찾기 수행
    stack = [S]
    visited = [0] * (V + 1)  # 방문 여부 표시
    visited[S] = 1  # 시작점 방문
    while stack:  # 경로상에 노드가 있으면 계속 탐색
        top = stack[-1]  # 현재위치
        if top == G:
            return 1
        # 현재위치에서 갈 수 있는 모든 경로 탐색
        for i in range(1, V + 1):
            # 갈 수 있는 경로, 나랑 연결되어있고, 방문하지 않은곳
            if adj[top][i] and not visited[i]:  # adj[top][i] == 1 and visited[i] ==0
                stack.append(i)
                visited[i] = 1
                break  # 경로 찾았으니 top에서 갈 수 있는 경로탐색 종료
        else:  # break가 한번도 실행안됨>>길없음 for-else문
            stack.pop()
    return 0  # 반복문을 다 돌았는데도 목적지에 도달못함


# 노드를 이동하는 재귀함수
# 현재노드 v가 목적지라면 1반환, 아니면 다음 경로 탐색
def solve2(v, G, adj, visited):
    visited[v] = 1

    if v == G:
        return 1

    for i in range(1, V + 1):
        if adj[v][i] and not visited[i]:
            result = solve2(i, G, adj, visited)
            if result == 1:
                return 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # 인접행렬 생성, 1번부터 V번 노드까지 있음
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        # a노드에서 b노드로 가는 경로가 존재한다
        adj[a][b] = 1
    S, G = map(int, input().split())
    result = solve(S, G, adj)
    result1 = solve2(S,G,adj,[0]*(V+1))
    print(f'#{tc} {result}')
    print(result1)
