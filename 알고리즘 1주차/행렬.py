# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# arr2 = [[0]*N for _ in range(N)]
# print(arr)
# print(arr2)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N=5
arr= [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = i + dj[k]
            if 0<=ni<N and 0<=nj<N:
                print(arr[ni][nj], end = ' ')
        print()


i = 3
j = 4
for k in range(4):
    ni = i + di[k]
    nj = i + dj[k]
    print(ni ,nj)

arr = [[1,2,3],[4,5,6],[7,8,9]] #3*3행렬

#전치 행렬
for i in range(3):
	for j in range(3):
		if i < j :
			arr[i][j], arr[j][i] = arr[j][i],arr[i][j]
print(arr)

#부분집합 생성
bit = [0,0,0,0]
a=0
for i in range(2):
    bit[0]=i
    for j in range(2):
        bit[1]=j
        for k in range(2):
            bit[2]=k
            for l in range(2):
                bit[3]=l
                a+=1
print(a)
#부분집합 생성2
def f(arr,N):
    for i in range(1,1 << N): #i가 0일떄 공집합 제거할려면 1부터시작
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += arr[j]
        #         print(arr[j], end=' ')
        # print(s)
        if s == 0 :
            return True
    return False


N=int(input())
arr = list(map(int,input().split()))
print(f(arr,N))


