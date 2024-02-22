# 정점 v에서 연산을 수행하는 함수
# 연산 수행을 위해서는 왼쪽 서브트리 , 오른쪽 서브트리를 순회 후
# 그 결과를 이용해서 연산 > 후위순회
# 만약에 value가 숫자라면 연산하지 않고 반환
def solve(v):
    if tree[v][2] not in '+-*/':  # tree[v][2] 가 숫자라면?그냥반환
        return int(tree[v][2])
    else:  # 숫자가 아니라면??? 연산해야 합니다.
        # 왼쪽 서브트리 순회
        # tree[v][0] #왼쪽서브트리 루트
        # tree[v][1] #오른쪽서브트리 루트
        left_result = solve(tree[v][0])
        right_result = solve(tree[v][1])
        #이제 사칙연산: 현재 노드의 value에 따라 다르게 연산
        if tree[v][2] == '+':
            return left_result + right_result
        elif tree[v][2] == '-':
            return left_result - right_result
        elif tree[v][2] == '*':
            return left_result * right_result
        elif tree[v][2] == '/':
            return left_result / right_result

for tc in range(1, 11):
    N = int(input())
    # 노드의 정보를 저장 할 배열을 선언
    tree = [[0] * 3 for _ in range(N + 1)]
    for _ in range(N):
        data = input().split()
        # 길이가 2개라면 단말, 4라면 자식정보 포함
        # 0 : 노드 번호, 1 : 노드의 value , 2: 왼쪽자식번호,3:오른쪽 자식번호
        if len(data) == 4:
            node = int(data[0])
            left = int(data[2])
            right = int(data[3])
            value = data[1]
            tree[node][0] = left
            tree[node][1] = right
            tree[node][2] = value
        else:
            node = int(data[0])
            value = data[1]
            tree[node][2] = value
    result= int(solve(1))
    print(f'#{tc} {result}')
