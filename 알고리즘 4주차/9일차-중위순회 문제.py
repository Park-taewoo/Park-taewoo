# v번 노드에 있는 알파벳을 출력 >>> 중위순회 순서로 출력
def solve(v):
    if v > N :  # v가 N보다 크면 해당 정점은 없음
        return
    # 왼쪽 서브트리 먼저 탐색
    solve(v*2)
    print(tree[v],end='')
    solve(v*2+1)
    # 오른쪽 서브트리 나중에 탐색

T = 10
for tc in range(1,T+1):
    N = int(input())    # 정점의 개수,
    # 완전이진트리, 노드번호가 연속되도록 주어지니까..
    # 배열에 트리 저장할 수 있다.
    # 노드번호로 부모노드와 자식노드를 알 수있다.
    tree = [None] * (N+1)
    for _ in range(N):
        #노드번호, 알파벳, 왼쪽자식, 오른쪽자식
        data = input().split()
        tree[int(data[0])] = data[1]
    print(f'#{tc}',end=' ')
    solve(1)
    print()
'''
8                
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''
