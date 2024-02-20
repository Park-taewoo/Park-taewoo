# 13 #정점의 갯수
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
V = int(input())  # 정점의 개수
data = list(map(int, input().split()))
g = [[None] * 2 for _ in range(V + 1)]
for i in range(0, (V - 1) * 2, 2):
    # 부모노드 번호 :data[i], 자식노드 번호: data[i+1]
    # g[data[i]][0]: data[i]의 왼쪽 자식
    # g[data[i]][1]: data[i]의 오른쪽 자식
    if not g[data[i]][0]:  # 왼쪽 자식에 대한 정보를 가지고 있지 않음
        g[data[i]][0] = data[i + 1]
    else:  # 왼쪽 자식에 대한 정보를 이미 가지고 있음
        g[data[i]][1] = data[i + 1]
for row in g:
    print(row)

# 순회방법 : 전위 순회, 중위 순회, 후위 순회
#v:순회하는 노드 번호
#전위 순회
def pre_order(v):
    if v == None:
        return
    print(v,end=' ')
    pre_order(g[v][0]) #왼쪽 자식 방문
    pre_order(g[v][1]) #오른쪽 자식 방문

pre_order(1)