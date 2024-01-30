def solve():
    # 충전기 간의 거리가 이동가능한 정류장수보다 크면 충전할 수 없음 => 종점에 도착할 수 없다
    pos = 0 # 현재 위치 = 0
    cnt = 0 # 충전한 정류장 수
    while pos + K < N: # 현재 위치+이동 가능 거리가 종점 위치보다 크거나 같아지면 while문 종료
        for i in range(pos + K,pos,-1): # 현재 위치에서 갈 수 있는 자리부터 현재 위치까지 거꾸로 탐색(가장 멀리 있는 정류장)
            if i in charge: # 탐색하고 있는 장소가 정류장이 있는 곳이라면
                cnt += 1 # 충전하고
                pos = i # 충전소에서 다시 출발
                break # 이번 정류장은 탐색 종료
        else: # 근데 탐색이 break되지 않았다 = 정류장을 못 찾았다
            return 0 # 종점 도착 실패
    return cnt # while문 무사히 종료 = 도착했다 충전한 정류장 수 반환
 
T=int(input())
for T_num in range(1,T+1):
    K,N,M = map(int,input().split()) # K 이동가능한 정류장 수,N 종점 위치, M 충전기 설치된 정류장 수
    charge = list(map(int,input().split()))
    result = solve()
    print(f'#{T_num} {result}')