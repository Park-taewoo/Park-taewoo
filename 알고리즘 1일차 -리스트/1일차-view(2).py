# 각 건물들의 조망권 확보세대 계산
def solve():
    result = 0
    # 각 건물들의 조망권 확보세대 계산
    for i in range(2,N-2):
        # data[i] : i번째 건물의 높이
        # 양쪽 2칸내에 있는 건물을 살펴보면됩니다.
        # max_b = max(data[i-2], data[i-1], data[i+1], data[i+2])
        # #######################################################
        # max_b = data[i - 2]
        # for building in [data[i - 1], data[i + 1], data[i + 2]]:
        #    if max_b < building:
        #        max_b = building
        #######################################################
        max_b = data[i-2]
        for j in range(i-2,i+3):    #주변 건물에서 최대값 찾기
            if j == i:  
                continue
            if max_b < data[j]:
                max_b = data[j]
        #######################################################

        # i번째 건물높이랑 주변 건물의 최고층 비교 : i번째 건물이 더 높으면 조망권이 있음
        if data[i] > max_b:
            result += data[i] - max_b # 조망권이 확보된 세대수
    return result
T = 10
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    result = solve()
    print(f'#{tc} {result}')
