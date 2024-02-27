# 1이 있는 칸에 글자를 쓸 수 있고, 0이면 끊어짐!
def count(arr):
    ret = 0  # 반환(return의 약자) 값 초기화
    for lst in arr:  # arr의 행마다~~
        cnt = 0 #cnt를 0으로 초기화
        for j in range(len(lst)):  # 해당 리스트의 각 요소에 대해 반복
            if lst[j] == 1 :  # 해당 행의 j번째 요소가 0이 아닌 경우 
                cnt += 1
            else:  # 값이 0인 경우 #else 안에 if문 언제든 쓸 수 있다는 사실을 염두해두자.
                if cnt == K:
                    ret += 1 #return 할 것이 +1씩 증가된다!
                cnt = 0 # 순회하는 과정에서 언제든 초기화시킬 수 있다.
    return ret

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]
                                                # 우측 라인에 0 추가      # 아래 라인에 0 추가
    arr_t = list(map(list, zip(*arr)))  # 실용적인 스킬임!: (행렬을 이미징하면서...)전치행렬 생성 (리스트 언패킹)

    # 위의 count함수는 행만 고려해서, 들어갈 수 있는 개수를 구했다.
    # 그렇기 때문에, 열로 들어갈 수 있는 개수를 구해야하므로, 전치행렬로 뒤집어서 열로 들어갈 수 있는 개수를, 
    # count 함수처럼'행'의 관점에서 접근해서 개수를 셀 수 있도록 하자!
    ans = count(arr) + count(arr_t)
    # 행과 열에 대한 처리 (함수로 만든 것으로)
    print(f'#{tc} {ans}')