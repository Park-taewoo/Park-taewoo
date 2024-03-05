#정점(노드),정점들을 잇는 간선(엣지,Edge)
# 7 8 (노드 최대번호,간선개수)
# 1 3 1 2 2 4 2 5 4 6 5 6 6 7 3 7
#1. 인접 리스트에 저장하기
V, E =map(int,input().split())
data=list(map(int,input().split()))

g = [[] for _ in range(V+1)]
for i in range(0,E*2,2):
    g[data[i]].append(data[i+1])
    g[data[i+1]].append(data[i])
for row in g:
    print(row)
#2. 인접 행렬에 저장하기
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(0,E*2,2):
    # data[i], data[i+1]
    adj[data[i]][data[i+1]] = 1
    adj[data[i+1]][data[i]] = 1
for row in adj:
    print(row)

def dfs(start):
    #경로저장을 위해서 stack이 필요
    stack =[start]
    visited = [0]*(V+1) #방문 표시 배열,중복방문을 방지한다.
    visited[start] = 1 #방문했다 표시
    print(start,end=' ')
    while stack : #스택의 길이가 0보다크면 = 스택이 있으면
        #현재 위치(경로상 마지막,stack의 top)에서 갈 수 있는 모든 노드를 탐색
        current= stack[-1]
        # 만약에 현재위치랑 인접하면서 방문하지 않았으면 해당노드를 방문
        # 현재노드와 인접한 노드 정보 adj[current]
        for i in range(V+1): # i : 노드번호
            #current 노드가 i번 노드와 연결되어 있는지 확인
            if adj[current][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i]=1
                print(i,end=' ')
                #길찾기 중단
                break
        else: #현재 위치에서 갈 수 있는 길 없음
            stack.pop()
dfs(1)
print()
#재귀
#현재 노드, 방문표시
def dfs2(v,visited):
    print(v,end=' ')
    visited[v] = 1
    #경로 탐색
    for i in range(V+1):
        if adj[v][i]  and not visited[i]:
            dfs2(i,visited)
dfs2(1,[0]*(V+1))
print()

# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7