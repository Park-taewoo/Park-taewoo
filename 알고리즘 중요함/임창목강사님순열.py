#순열 만들기
arr = [1,2,3]
N = len(arr)
perm = [0] * N
#perm[idx] 요소에 arr의 모든 요소 넣어보기
#요소를 중복으로 사용할 수 있는 순열
#중복순열
def permutation(idx):
    if idx == N: #인덱스를 벗어나면 요소넣기 중단
        print(perm)
        return
    for i in range(N):
        perm[idx] = arr[i]
        permutation(idx+1)

permutation(0)
print('---------------------------')
# 중복 없애기: 앞 인덱스에서 사용한 요소는 사용안하기
# 사용한 요소 체크하기
check = [0] * N #각 요소에 대해서 사용했으면 1, 안했으면 0
def permutation1(idx):
    if idx == N: #인덱스를 벗어나면 요소넣기 중단
        print(perm)
        return
    for i in range(N):
        #표시 되어 있는거 안쓰기
        if not check[i]:
            perm[idx] = arr[i]
            check[i] = 1  #썻다 표시
            permutation1(idx+1)
            check[i] = 0 #썻다는 표시제거
permutation1(0)