#1 전체를 절반으로 나눔
#2. 왼쪽과 오른쪽을 각각 정렬
#3. 왼쪽과 오른쪽을 병합
#4. 합친 전체를 반환
#arr: 정렬 하고자 하는 배열
def merge_sort(arr):
    #요소가 1개라면.... 그대로 반환
    if len(arr) ==1:
        return arr
    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    result=[]
    #왼쪽과 오른쪽 배열에서 각각 제일 작은 애들 비교 해서
    #더 작은애 result에 붙여주기
    #언제까지? 둘 중 하나가 다 떨어질떄 까지
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 남은 애들 붙여주기
    result+=left
    result+=right
    
    return result
arr=[7,4,5,6,2,1,5,4]
result=merge_sort(arr)
print(result)

#전체 배열을 자르지 않고 정렬할거기 떄문에 정렬 범위가 필요
def merge_sort2(start,end):
    #요소가 하나라면 재귀 호출 하지 않음
    if start==end:
        return 
    mid=(start+end)//2
    #왼쪽 정렬
    merge_sort2(start,mid)
    #오른쪽 정렬
    merge_sort2(mid+1,end)
    #병합
    #병합하기 위한 배열 선언
    sorted_arr=[]
    i = start
    j = mid +1
    # 둘 중 하나가 다 떨어질 때 까지
    # start~mid :i
    # mid+1~end :j
    while True:
        if i > mid or j >end:
            break
        # arr[i]와 arr[j]가 각각 왼쪽배열 ,오른쪽 배열의 제일 작은값   
        if arr[i] < arr[j]:
            sorted_arr.append(arr[i])
            i+=1
        else:
            sorted_arr.append(arr[j])
            j+=1
    # 남은 애들 붙여주기
    while i <= mid:
        sorted_arr.append(arr[i])
        i+=1
    while j <= end:
        sorted_arr.append(arr[j])
        j+=1
    
    # 방금 정렬한 배열의 길이 : M
    M=end-start+1
    for i in range(M):
        arr[start+i] =sorted_arr[i]
arr=[7,4,5,6,2,1,5,4]
merge_sort2(0,len(arr)-1)
print(result)
