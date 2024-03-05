# 순열 : permutation
# idx 번째 요소에 모든 요소 한번씩 넣어보기
arr = [1, 2, 3]
N = len(arr)
perm_arr = [0] * N


# idx 번쨰에 모든 요소 넣어보기
# used: 요소가 사용되었는지 표시하는배열

def perm(idx,used):
    if idx == N:
        print(perm_arr)
        return

    for i in range(N):
        if not used[i]: #사용안한 요소라면 쓰겠다
            perm_arr[idx] = arr[i]
            used[i] = 1 #사용표시
            perm(idx + 1,used)
            used[i] = 0 #다썻으니 표시 없애기


perm(0,[0]*N)
print('--------------')


def perm2(idx):
    if idx ==N:
        print(arr)

    for i in range(idx,N):
        arr[idx],arr[i] = arr[i],arr[idx]
        perm2(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]
perm2(0)