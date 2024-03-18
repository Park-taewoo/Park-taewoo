#퀵 정렬은 두가지 파트로 구분
#1. 피벗을 기준으로 두 부분으로 가르기>>partition
#파티션을 했을 떄 상황? > 피벗값만 제자리를 찾은 상태
#나머지는 정렬되지 않은상황
#2. 나누어진 각 부분(피벗보다 큰 부분, 피벗보다 작은 부분)을 각각정렬
# 배열 복사해서 파이썬에만 가능한 방법(비효율적 이지만 로직만 보는걸로)
def quick_sort1(arr):
    #arr이 비어 있는 리스트거나
    #길이가 1이면 그냥 반환
    if not arr or len(arr) ==1:
        return arr 
    
    #파티션>>큰부분과 작은 부분으로 나누기
    left=[] #피벗보다 작은 요소 들어가는 배열
    right=[] #피벗보다 큰(크거나 같은) 요소 들어가는 배열
    #pivot 잡기 >>> 아무거나 잡으시면 됩니다.
    pivot=arr.pop(0) #제일 앞에 요소를 pivot으로 설정
    for e in arr:
        if pivot >e :
            left.append(e)
        else:
            right.append(e)
            
    # 작은 요소들 + pivot + 큰 요소들
    # (작은 요소들 정렬한거) + pivot + (큰 요소들 정렬한거)
    return quick_sort1(left) +[pivot] +quick_sort1(right)




T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    result=quick_sort1(arr)
    print(f'#{tc} {result[N//2]}')
