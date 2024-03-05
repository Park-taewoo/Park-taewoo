# 조합(combination) : 전체중에 몇개 선택하기
# 부분집합이랑 거의 똑같은데....선택한 개수도 같이 알고 있으면 된다.

arr = [1, 2, 3, 4, 5]

N = len(arr)
M = 3  # 원하는 조합 개수


# idx번째 요소를 조합에 포함시킬지 말지 결정
# cnt:선택한 요소 개수
# selected : 선택한 요소 표시 배열
def comb(idx, cnt, selceted):
    lst = []
    if cnt == M:  # 원하는 개수 만큼 다 선택함
        print(selceted)
        for i in range(N):
            if selceted[i]:
                lst.append(arr[i])
        print(lst)
        return
    if idx == N:  # 인덱스는 끝났는데... 원하는 개수만큼 선택을 못함
        return
    selceted[idx] = 1
    comb(idx + 1, cnt + 1, selceted)
    selceted[idx] = 0
    comb(idx + 1, cnt, selceted)  # 선택안했어서 cnt는 그대로

comb(0,0,[0]*N)