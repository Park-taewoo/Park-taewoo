# 퀵 정렬은 두 가지 파트로 구분
# 1. 피벗을 기준으로 두 부분으로 가르기 >> partition
# 파티션을 했을 때 상황? > 피벗값만 제자리를 찾은 상태
# 나머지는 정렬되지 않은상황
# 2. 나누어진 각 부분(피벗보다 큰부분, 피벗보다 작은 부분)을 각각정렬
# 배열 복사...파이썬에서만 가능한 방법(비효율적 이지만 로직만 보는걸로)
def quick_sort1(arr):
    # arr이 비어있는 리스트 거나.. 길이가 1이면...그냥 반환
    if not arr or len(arr) == 1:
        return arr
    # 파티션 >>> 큰부분과 작은 부분으로 나누기
    left = []   # 피벗보다 작은 요소 들어가는 배열
    right = []  # 피벗보다 큰(크거나 같은) 요소 들어가는 배열
    # pivot 잡기 >>> 아무거나 잡으시면 됩니다..
    pivot = arr.pop(0) #제일 앞에 요소를 pivot으로 설정
    for e in arr:
        if pivot > e:
            left.append(e)
        else:
            right.append(e)

    # 작은 요소들 + pivot + 큰 요소들
    # (작은 요소들 정렬한거) + pivot + (큰 요소들 정렬한거)
    return quick_sort1(left) + [pivot] + quick_sort1(right)

#인덱싱을 활용한 퀵정렬 (다른 배열을 만들지 않고..인덱싱만 활용)
# 다른 언어에서도 별다른 수정없이 쓸 수 있는거..

# partion 함수: 영역내의 요소를 피벗보다 작은 요소와 큰요소로
# 구분하고 pivot 위치를 반환
# hoare patition
def partition(arr,start,end):
    # pivot : 제일 왼쪽 요소를 임의로 피벗으로 설정
    pivot = arr[start]
    i = start   # 큰 값에서 멈추는 변수
    j = end     # 작은 값에서 멈추는 변수
    while i <= j:
        #i가 가리키는 값이 피벗보다 작으면 지나가기..
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        # 자리 바꿔주면 큰 값이 뒤로가고 작은 값이 앞으로 옴..
        if i < j:   #역전이 일어나면 바꾸면 정렬 안 됨..
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]
    return j

def quick_sort2(arr,start,end):
    if start >= end:    #요소가 하나이거나 정렬할 요소가 없음
        return
    #파티션 부분을 따로 함수로 빼서 작성
    p = partition(arr,start,end)
    #왼쪽(피벗 보다 작은쪽 정렬)
    quick_sort2(arr,start,p-1)
    # 왼쪽(피벗 보다 큰쪽 정렬)
    quick_sort2(arr, p+1,end)

arr= [1,3,5,4,1,6,9,2]
# result = quick_sort1(arr)
quick_sort2(arr,0,len(arr)-1)
# print(result)
print(arr)
