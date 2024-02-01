#덤프 완료후,최대높이-최소높이 값을 반환하는 함수
def solve():
    #N번 덤프 수행
    #최대값 위치 찾고, 최소값 위치찾기
    #최대 위치에서 -1, 최소 위치에서 +1
    for _ in range(N):
        max_idx = 0
        min_idx = 0
        for i in range(100):
            if boxes[max_idx] < boxes[i]:
                max_idx = i
            elif boxes[min_idx] > boxes[i]:
                min_idx = i
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        # 덤프 완료 후 최대 촤도 다시계산
        for i in range(100):
            if boxes[max_idx] < boxes[i]:
                max_idx = i
            elif boxes[min_idx] > boxes[i]:
                min_idx = i
        return max_idx - min_idx


T=10
for tc in range(1,T+1):
    N = int(input())
    boxes = list(map(int,input().split()))
    result=solve()
    print(f'{tc} {result}')