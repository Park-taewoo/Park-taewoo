# Poewrset : 모든 부분집합 구하기
# idx: idx번쨰 요소에 대해서 부분집ㅎ바 포함여부 결정 함수
# selceted : 각 요소가 부분집합에 포함되는지 표시하는 배열
# ex) [0,0,1,1,0] >> 2,3번 인덱스 요소가 부분집합에 포함
arr = [1, 2, 3, 4, 5]
N = len(arr)


def Poewrset(idx, selected):
    if idx == N:  # 인덱스를 벗어났음,모든 요소에 대해서 결정 완료
        print(selected)
        sum_v = 0
        for i in range(N):
            if selected[i]:
                print(arr[i],end=' ')
                sum_v += arr[i]
        print()
        print('----------')
        print(sum_v)
        if sum_v ==10:
            print('찾았다')
        print('///////////')
        return
        # idx번쨰 요소를 부분집합에 포함시키거나
    selected[idx] = 1
    Poewrset(idx + 1, selected)
    # idx번쨰 요소를 부분집합에 포함시키지 않거나
    selected[idx] = 0
    Poewrset(idx + 1, selected)
    # 위에꺼랑 같은 반복문 형태
    # for i in range(2):
    #     selected[idx] =i
    #     Poewrset(idx+1,selected)

#selcted = [0] * N
Poewrset(0,[0] * N)
