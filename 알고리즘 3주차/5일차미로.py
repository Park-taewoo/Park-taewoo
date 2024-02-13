def dfs():
    # 시작점 먼저 찾고
    # 시작점에서 dfs 탐색 수행
    r, c = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 시작점 찾기
                r, c = i, j
    # 시작점 찾았으니 dfs 수행
    # 각 노드는 (r,c) 형태로 표현, 인접한 노드는 상화자우 네 개
    stack = [(r, c)]
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]  # 상하좌우
    while stack:
        cr, cc = stack[-1]  # 현재위치 stack이 [(r,c)]이므로 따로 받음
        if arr[cr][cc] ==3:
            return 1
        # 현재 위치에서 갈 수 있는 곳 다 찾아보기
        for d in range(4):  # 네 방향 탐색
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 정상범위에 있으면서 통로(또는 목적지)라면
            # 그리고 방문하지 않았으면 방문
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 \
                    and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break
        else: #갈 수 있는곳이 없으면
            stack.pop()
    return 0


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    result = dfs()
    print(f'#{tc} {result}')
