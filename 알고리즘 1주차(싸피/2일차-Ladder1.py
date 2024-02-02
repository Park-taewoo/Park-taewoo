
# 현재 위치 좌표 잡고
# 이동 방향에 대한 변화량 설정하고
# 이동하면서 방향 전환을 해야하는지 확인
# - 아래쪽으로 이동중이었다면, 좌우에 사다리가 있는지 확인
# - 좌우로 이동중이었다면 아래쪽에 사다리가 있는지 확인
# 목적지에 도착하면 2인지 확인하고 2라면 출발지 출력
# 사다리 타기 했을 때 목적지에 도착 할 수 있는 출발지 반환
def solve():

    #이동을 위해서 방향 별로 변화량 배열
    # 0번: 하, 1번: 좌,   2번 : 우
    dr = [1,0,0]
    dc = [0,-1,1]
    for start in range(100):
        if ladder[0][start] == 1:   #시작점 찾은거니까...
            # 현재 위치를 저장하기 위해서 변수 선언 및 사다리 타기 시작
            r, c = 0, start
            d = 0   # 시작시 이동방향은 아래방향
            while r < 99:
                # 아래로 내려가는 경우
                if d == 0:
                    #왼쪽 오른쪽 봤더니 가는길이있으면, 방향 전환
                    if c > 0 and ladder[r][c-1] == 1:
                        d = 1

                    elif c < 99 and ladder[r][c+1] == 1:
                        d = 2
                    # 좌, 우로 가는경우
                else:
                    # 내려가는 길이 있으면 방향전환
                    # (1또는 2라면 내려가기)
                    if ladder[r+1][c] != 0:
                        d = 0
                # 이동
                r += dr[d]
                c += dc[d]
            if ladder[r][c] == 2:
                return start
    #이 문장은 아마 실행안될건데..인 풋이 잘들어가 있으면
    return -1

T = 10
for _ in range(T):
    tc = input()
    ladder = [list(map(int,input().split())) for _ in range(100)]
    result = solve()
    print(f'#{tc} {result}')
