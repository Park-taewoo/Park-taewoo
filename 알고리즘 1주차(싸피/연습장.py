
# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)
# 부분집합 생성하는 방법
arr=[3,6,7,1,5,4]

n = len(arr)
for i in range(1<<n): #1<<n: 부분 집합의 갯수
    for j in range(n): #원소의 수만큼 비트를 비교함
        if i&(1<<j): #i의 j번 비트가 1인경우
            print(arr[j],end=",")  #j번 원소 출력
    print()
print()

#선택정렬
a=[1,3,6,8,9,2]
N=len(a)

for i in range(N-1):
    min_idx = i
    for j in range(i+1,N):
        if a[min_idx] > a[j]:
            min_idx = j
    a[i],a[min_idx] = a[min_idx],a[i]
print(a)
#일반적인 셀력션 알고리즘
#k번쨰로 작은 원소를 찾는 알고리즘 시간복잡도 O(kn)
#1번부터 k번쨰까지 작은 원소들을 앞쪽으로 이동하고 배열의 k번쨰를 반환
arr=[11,3,6,7,1,5,4,8]
K=6
for i in range(0,K):
    min_idx = i
    for j in range(i+1,len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i],arr[min_idx] = arr[min_idx],arr[i]
print(arr[K-1])
print(arr)
