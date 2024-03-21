from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [0] *1000001

    q = deque()
    q.append((N, 0))

    visited[N] = 1

    while 1:
        node, cnt = q.popleft()

        if node == M:
            break

        for i in range(4):
            if i == 0:
                if 1000001 > node + 1:
                    if not visited[node + 1]:
                        visited[node + 1] = 1
                        q.append((node + 1, cnt + 1))
            elif i == 1:
                if 1000001 > node - 1:
                    if not visited[node - 1]:
                        visited[node - 1] = 1
                        q.append((node - 1, cnt + 1))
            elif i == 2:
                if 1000001 > node * 2:
                    if not visited[node * 2]:
                        visited[node * 2] = 1
                        q.append((node * 2, cnt + 1))
            else:
                if 1000001 > node - 10:
                    if not visited[node - 10]:
                        visited[node - 10] = 1
                        q.append((node - 10, cnt + 1))

    print(f'#{tc} {cnt}')