# 이진검색
arr=[324,32,22114,16,48,93,22,21,316]
#1.정렬된 상태의 데이터
arr.sort()
print(arr)
#2.이진 검색 - 반복문 버전
def binarySearch(target):
    #제일 왼쪽,오른쪽 인덱스 구하기
    low=0
    high=len(arr)-1
    #해당 숫자를 찾으면 종료
    # 더 이상 쪼갤 수 없을 때까지
    while low<=high:
        mid=(low+high)//2
        
        #가운데 숫자가 정답이면 종료
        if arr[mid]==target:
            return mid
        elif arr[mid] > target:
            high = mid -1
        elif arr[mid]<target:
            low = mid +1
    #못찾으면
    return -1
#이진 검색 - 재귀 함수 버전
def binarySearch2(low,high,target):
    # 기저조건(언제까지 재귀가 반복되어야 할까?)
    if low >high:
        return -1

    # 다음 재귀 들어가기 전엔 무엇을 해야할까?
    # 정답 판별
    mid =(low+high)//2
    if target==arr[mid]:
        return mid
    
    # 다음 재귀 함수 호출(파라미터)
    if target<arr[mid]:
        return binarySearch2(low,mid-1,target)
    else:
        return binarySearch2(mid+1,high,target)
    # 재귀 함수에서 돌아왔을 때 어떤 작업을 해야할까?

    


print(f'21={binarySearch(21)}')
print(f'324={binarySearch(324)}')
print(f'888={binarySearch(888)}')

print(f'21={binarySearch2(0,len(arr)-1,21)}')
print(f'324={binarySearch2(0,len(arr)-1,324)}')
print(f'888={binarySearch2(0,len(arr)-1,888)}')