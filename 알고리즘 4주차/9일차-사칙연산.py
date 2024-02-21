T=10
for tc in range(1,T+1):
    N = int(input())
    A = list(input().split() for _ in range(N))
    tree = [None] * (N+1)
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][1] in '-*/+':
                tree[i+1] = A[i][1]
            elif A[i][1] not in '-*/+':
                tree[i+1] = int(A[i][1])
    B = len(tree)
    for k in range(B-1,-1,-1):
        if tree[k] == '-':
            tree[k] = tree[int(A[k-1][2])] - tree[int(A[k-1][3])]
        elif tree[k] == '+':
            tree[k] = tree[int(A[k-1][2])] + tree[int(A[k-1][3])]
        elif tree[k] == '/':
            tree[k] = tree[int(A[k-1][2])] / tree[int(A[k-1][3])]
        elif tree[k] == '*':
            tree[k] = tree[int(A[k-1][2])] * tree[int(A[k-1][3])]
    print(f'#{tc} {int(tree[1])}')

