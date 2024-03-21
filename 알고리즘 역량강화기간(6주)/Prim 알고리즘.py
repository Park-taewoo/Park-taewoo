import heapq
#MST
# 7 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51
V, E = map(int,input().split())
INF = 0xffffffff
#노드간 연결정보:가중치 포함
adj = [[0]*V for _ in range(V)]
for _ in range(E):
    a,b,w = map(int,input().split())
    adj[a][b] = w
    adj[b][a] = w
# MST 를 만들어갈건데..만들고 있는 MST에서
# 인접한 노드로 갈수 있는 가장 적은 비용의 간선을 선택하기
def prim(start):
    MST = {start}
    # 현재 선택한 노드들에서 다른 노드로 갈 수 있는 비용을 저장하는 배열
    # 노드로 갈 수 있는 경로가 여러개라면 최소 비용만 저장
    weight = [INF]*V
    weight[start] = 0   #시작정점을 연결하는 비용은 0

    # weight에 시작 노드에서 다른 노르로 갈수 있는 비용 넣어주기
    for i in range(V):
        if adj[start][i]:
            weight[i] = adj[start][i]

    while len(MST) < V: # 모든 노드를 선택할 때 까지 반복
        #비용중에 제일 작은거 선택 (이미 선택된 노드는 빼고)
        min_idx = -1
        min_val = INF
        for i in range(V):
            if weight[i] < min_val and i not in MST:
                min_val = weight[i]
                min_idx = i
        #제일 작은 비용과 그 비용으로 갈 수 있는 노드가 선택됨
        MST.add(min_idx)
        # MST에 새로운 노드가 추가 되면서 각 노드로 갈 수 있는 비용바뀜
        # 만약에 더 싼 비용으로 갈 수 있는 노드가 있으면 바꿔주기
        # min_idx와 연결된 노드를 살펴보면됩니다.
        for i in range(V):
            # adj[min_idx][i] # min_idx에서 i번 노드 가는 비용
            if adj[min_idx][i] > 0 and weight[i] > adj[min_idx][i] and i not in MST:
                weight[i] = adj[min_idx][i]

    print(weight)
    #prim end


def prim2(start):
    MST = {start}
    # 현재 선택한 노드들에서 다른 노드로 갈 수 있는 비용을 저장하는 배열
    # 노드로 갈 수 있는 경로가 여러개라면 최소 비용만 저장
    weight_heap = []    # 확정되지 않은 가중치를 넣어주는 배열
    weight = [0]*V # 확정된 가중치를 넣어주는 배열
    for i in range(V):
        if adj[start][i]:
            #(가중치, 노드번호)
            heapq.heappush(weight_heap,(adj[start][i],i))

    while len(MST) < V:
        # weight_heap에서 가중치가 제일 작은애 뽑아오기
        w, v = heapq.heappop(weight_heap)
        if v in MST: continue

        weight[v] = w
        MST.add(v)
        for i in range(V):
            if adj[v][i] and i not in MST:
                heapq.heappush(weight_heap,(adj[v][i],i))

    print(weight)



prim(0)
prim2(0)
# heap = []
# #heappush
# heapq.heappush(heap,(5,'A'))
# heapq.heappush(heap,(4,'B'))
# heapq.heappush(heap,(6,'C'))
# heapq.heappush(heap,(1,'D'))
# heapq.heappush(heap,(2,'E'))
#
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
