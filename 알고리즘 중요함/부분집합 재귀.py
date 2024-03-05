#bit의 idx 번째 요소에 1또는 0넣어주기
# 만약 하나가 결정되면...다음 인덱스 결정하는 함수 호출
def subset(idx,bit,N):
    if idx == N:
        # print(bit)
        for idx in range(N):
            if bit[idx]:
                print(arr[idx],end=' ')
        print()
        return
    # for i in range(2):
    #     bit[idx] = i
    #     subset(idx+1,bit,N)
    bit[idx] = 0
    subset(idx+1,bit,N)
    bit[idx] = 1
    subset(idx + 1, bit, N)


# 부분 집합 구하기
arr = ['A','B','C']
N = len(arr)
bit = [0] * N
subset(0,bit,N)


# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)
#             for idx in range(N):
#                 if bit[idx]:
#                     print(arr[idx],end=' ')
#             print()
