# 정점(노드), 정점들을 잇는 간선(엣지,Edge)
# (노드 최대 번호, 간선개수)
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
V, E = map(int,input().split())
data = list(map(int,input().split()))
# 1. 인접 리스트에 저장하기
g = [[] for _ in range(V+1)]

for i in range(0,E*2,2):
    g[data[i]].append(data[i+1])
    g[data[i+1]].append(data[i])

def bfs(start):
    # 먼저 발견한 경로를 먼저 탐색 >> 큐를 활용 FIFO
    # 재방문 방지를 위한 방문 표시 배열
    visited = [0] * (V+1)
    queue = [start]
    visited[start] = 1
    # 경로 탐색 수행 : 발견한 경로가 더 이상 없을 때 까지..반복
    while queue:
        current = queue.pop(0)
        print(current,end=' ')
        for i in range(V+1):
            # current랑 i랑 인접하면서, i를 방문하지 않았으면
            if i in g[current] and not visited[i]:
                queue.append(i)
                visited[i] = 1
    print()
bfs(1)
# 선형큐를 이용해서 bfs 구현
# enQueue = rear + 1
# deQueue = front + 1
# isEmpty
def bfs2(start):
    queue = [None] * 1000000
    front, rear = -1, -1
    visited = [0] * (V+1)
    #enQueue
    rear += 1
    queue[rear] = start
    visited[start] = 1
    while front != rear:    # 큐가 비어있지 않음
        front += 1
        current = queue[front]
        print(current,end=' ')

        for i in range(V+1):
            if i in g[current] and not visited[i]:
                rear += 1
                queue[rear] = i
                visited[i] = 1
    print()
bfs2(1)
# 정점 A에서 B정점 까지 가기 위한 최소거리?

# 시작점에서 목적지 까지 걸리는 거리를 반환하는 함수
# 시작점에서 각 노드까지의 거리를 같이 알고 있으면 됩니다.
def bfs_length(start,goal):
    visited = [0] * (V+1)
    #노드 번호와 시작점에서 거리를 (번호, 거리) 형태로 저장
    queue = [(start,0)]
    visited[start] = 1
    while queue:
        #(번호,거리)
        current, distance = queue.pop(0)
        print(current, end=' ')
        if current == goal:
            return distance
        for i in range(V+1):
            if i in g[current] and not visited[i]:
                queue.append((i, distance + 1))
                visited[i] = 1
    print()
    return -1   # 목적지에 도달하지 못하는 경우...임의로 -1반환

def bfs_length2(start,goal):
    visited = [0] * (V+1)
    queue = [start]
    visited[start] = 1  # visited에 시작점에서 거리를 저장, 시작점 거리가 1
    while queue:
        #(번호,거리)
        current = queue.pop(0)
        print(current, end=' ')
        if current == goal:
            return visited[goal] - 1    # 시작점을 1로 시작했으니까 1빼주기
        for i in range(V+1):
            if i in g[current] and not visited[i]:
                queue.append(i)
                visited[i] = visited[current] + 1
    print()
    return -1   # 목적지에 도달하지 못하는 경우...임의로 -1반환


result1 = bfs_length(4,3)
result2 = bfs_length2(4,3)
print(f'거리 :{result1}, {result2}')
