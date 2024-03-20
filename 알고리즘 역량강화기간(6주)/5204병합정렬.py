# def merge_sort(arr):
#     global cnt
#     N = len(arr)
#     if N == 1:  # 요소가 1개 짜리는 정렬 되어 있는 상태
#         return arr
#     left = arr[:N // 2]
#     right = arr[N // 2:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     # 문제에서 요구하는 요구사항을 출력하기 위한 코드
#     if left[-1] > right[-1]:
#         cnt += 1
#
#     merged = []
#     # left와 right의 각각 제일 작은 값 비교
#     while left and right:
#         if left[0] < right[0]:
#             merged.append(left.pop(0))
#         else:
#             merged.append(right.pop(0))
#     # left 혹은 right 에 남아있는 요소를 merged 에 붙여주기
#     merged += left
#     merged += right
#
#     return merged

#

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     arr = merge_sort(arr)
#     print(f'#{tc} {arr[N // 2]} {cnt}')

def merge_sort2(start, end):
    global cnt
    if start == end:
        return
    mid = (end + start - 1) // 2
    merge_sort2(start, mid)
    merge_sort2(mid + 1, end)
    # 왼쪽 배열과 오른쪽 배열의 마지막 요소 비교
    if arr[mid] > arr[end]:
        cnt += 1
    # 왼쪽과 오른쪽 정렬되어 있음
    merged = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1
    # 남은거 다 갖다 붙이기
    while i <= mid:
        merged.append(arr[i])
        i += 1
    while j <= end:
        merged.append(arr[j])
        j += 1

    arr[start:end + 1] = merged


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    # arr = merge_sort(arr)
    # print(f'#{tc} {arr[N//2]} {cnt}')
    merge_sort2(0, N - 1)
    print(f'#{tc} {arr[N // 2]} {cnt}')