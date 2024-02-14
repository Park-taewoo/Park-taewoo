# powerset : 모든 부분집합 구하기
# idx:  idx번째 요소에 대해서 부분집합 포함여부 결정 함수
# selected : 각 요소가 부분집합에 포함되는지 표시하는 배열
# ex)  [0,0,1,1,0] >>> 2,3번 인덱스 요소가 부분집합에 포함
# 부분집합의 요소의 합이 10인 모든 부분집합을 알고 싶다!
arr = [1,2,3,4,5,6,7,8,9,10]
N = len(arr)
cnt = 0
def powerset(idx,selected,tmp_sum):
    global cnt
    cnt += 1
    if tmp_sum > 10:    # 총합이 10이 될 가능성이 없음!
        return  # 더 이상 경우의 수를 고려하지 않는다.
    if idx == N:    #인덱스 벗어남, 모든 요소에 대해서 결정 완료
        # print(selected)
        sum_v = 0
        sub_set = []
        for i in range(N):
            if selected[i]:
                # print(arr[i],end=' ')
                sub_set.append(arr[i])
                sum_v += arr[i]
        if sum_v == 10:
            print('찾았다!')
            print(sub_set)
        return
    #idx번째 요소를 부분집합에 포함시키거나
    selected[idx] = 1
    powerset(idx+1, selected,tmp_sum + arr[idx])
    # idx번째 요소를 부분집합에 포함시키지 않거나
    selected[idx] = 0
    powerset(idx + 1, selected, tmp_sum)

#0번인덱스 부터 선택시작, 처음 합은 0
powerset(0, [0] * N, 0)
print(cnt)
