from collections import deque


def solve():
    d1 = [1, 0, 0, -1]  # 하 좌 우 상
    d2 = [0, -1, 1, 0]
    visited[0][0] = 0
    q = deque()
    q.append((0,0))


    while q:
        r, c = q.popleft()
        for i in range(4):
            r1 = r + d1[i]
            c1 = c + d2[i]
            if 0 <= r1 < N and 0 <= c1 < N:
                if arr[r][c] >= arr[r1][c1]:  # 이동한 높이가 전 높이보다 크지 않을때
                    if visited[r][c] + 1 < visited[r1][c1]:
                        visited[r1][c1] = visited[r][c] + 1
                        q.append((r1, c1))
                else:   #이동한 높이가 전보다 높을때
                    if visited[r][c] + (arr[r1][c1] - arr[r][c] + 1) < visited[r1][c1]:
                        visited[r1][c1] = visited[r][c] + (arr[r1][c1] - arr[r][c] + 1)
                        q.append((r1, c1))
    return visited[-1][-1]


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[999999] * N for _ in range(N)]

    result = solve()
    print(f'#{tc} {result}')
