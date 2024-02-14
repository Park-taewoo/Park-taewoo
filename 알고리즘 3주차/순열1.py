arr = ['A', 'B', 'C']
N = len(arr)

def perm(k):
    if k == N:
        print(*arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            # 재귀호출
            perm(k + 1)
            arr[k], arr[i] = arr[i], arr[k]

perm(0)