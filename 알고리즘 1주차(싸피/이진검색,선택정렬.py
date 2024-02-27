# #이진검색
# def binary_search(arr,N,key):
#     start = 0 #  구간 조기화
#     end = N - 1
#     while start <=end: #검색 구간이 유요하면 반복
#         middle = (start/end)//2     #중앙원소 인덱스
#         if arr[middle]==key:      #검색 성공
#             return middle        # 검색을 성공했기 때문에 반환하고 종료
#         elif arr[middle] > key:#중앙값이 키보다 크면
#             end = middle - 1   #중앙값 왼쪽으로 검색
#         else:  #키보다 작은경우
#             start = middle + 1  #중앙값 오른쪽으로 검색
#     return -1   #검색 실패
# #선택 정렬
# def SelectionSort(a,N):
#     for i in range(N-1): # i 주어진 구간의 시작
#         min_idx = i # 맨앞원소를 최소로 가정
#         for j in range(i+1,N): #실제 최소값 위치 검색
#             if a[min_idx]>a[j]:
#                 min_idx = j
#         a[i],a[min_idx] = a[min_idx],a[i] #최솟값을 구간의 맨 앞으로 이동
#     return

# N=5
# arr = [-1,3,-2,5,2]
# print((arr))
# SelectionSort(arr,N)
# print(arr)

#이진탐색(Binary Search)
#1.전체 대상data(start~end) 중, 중간값을 key와 비교
#   1-1 만약 중간값이(data[m]) key라면 탐색 종료: 탐색성공
# 2.만약 중간값이(data[m]) key가 아니라면
    #2-1 data[m]가 key 보다 큰 경우
    # end를 m-1로 바꾸고 1번부터 다시 시작
    #2-2 data[m]가 key 보다 작은 경우
    # start를 m+1로 바꾸고 1번부터 다시시작
# 3. 만약 start>end 라면 종료 (못찾음)

#arr의 key가 있는지 없는지 True/False로 반환
def binary_search(arr,key):
    #반복구조로 작성
    start = 0      #초기위치 설정
    end = len(arr)-1

    while start <= end:
        if start > end:
            break
        middle = (start+end)//2
        if arr[middle] == key:
            return True
        elif arr[middle] > key: #중간값이 key보다 큰경우
            end= middle -1
        else:                  #중간값이 key보다 작은경우
            start = middle + 1
    return False #while 문을 다 돌았는데 못찾으면 False 반환


#재귀로 하는 이진탐색 찾으면 True, 못찾으면 False
def binary_search2(start,end,key):
    #재귀가 더이상 호출되지 않는 조건 : 못찾았을떄
    if start > end :
        return False
    middle = (start+end)//2
    if arr[middle]==key:
        return True
    #못찾았으면 탐색 범위 재설정해서 재귀 호출
    elif arr[middle]>key: # 중간값 기준 앞부분만 재 탐색
        return binary_search2(start,middle-1,key)
    else: #뒷 부분만 재 탐색
        return binary_search2(middle+1,end,key)


arr = [2,4,7,9,11,19,23]
arr2 = [2,4,7,9,6,0,100]
for el in arr2:
    result=binary_search(arr,el)
    print(result)
result=binary_search(arr,4)
print(result)