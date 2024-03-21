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

# 1. 간선의 가중치 순서대로 정렬
# 2. 순서대로 선택하면서 노드들을 하나의 집합에 넣어주기
# 3. 만약에 간선을 이루는 노드들이 이미 같은 집합이면 선택하지 않음
#   (cycle이 생기기 때문에)
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
p = [x for x in range(V)]  # 각 노드의 부모정보를 포함하는 배열

def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])


def union(x, y):
    r1 = find_set(x)
    r2 = find_set(y)
    p[r2] = r1

def kruskal():
    edges.sort(key=lambda x: x[2])
    selected = []
    # a,b: 노드 번호 , w: 간선 가중치
    for a, b, w in edges:
        # a와 b가 같은 그룹에 있지 않으면 선택하면 됩니다.
        ra = find_set(a)
        rb = find_set(b)
        if ra != rb: #같은 그룹에 있지 않으면 선택하고 같은 그룹으로 만들어주면 됨
            union(a,b)
            selected.append([a, b, w])
    for row in selected:
        print(row)

kruskal()