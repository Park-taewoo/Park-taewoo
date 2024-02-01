# 오름차순 앞에서 N/2 뒤에서 N/2개를 가져오기
def selection_sort(arr):
    #0번부터 N-1번까지 위치에 들어갈 요소 찾아서 넣어주기
    N = len(arr)
    for i in range(N-1): #마지막 요소는 굳이 안넣어도 원래 자기 자리
        # 정렬된 애 빼고,제일 작은거 찾아서 i번쨰 넣어주기
        min_idx = i
        for j in range(i,N):
            if arr[min_idx] > arr[j]:
                min_idx =j
        #제일 작은애 찾았으니 i번쨰 넣어주기
        arr[min_idx],arr[i] = arr[i],arr[min_idx]
    return arr


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr = selection_sort(arr)
    #제일 끝에서 하나 앞에서 하나
    print(f'#{tc}',end=' ')
    for i in range(N//2):
        print(f'{arr[N-i-1]} {arr[i]}',end = ' ')
    print()
