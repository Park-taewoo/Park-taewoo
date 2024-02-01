#최소 충전 횟수를 반환하는 함수
def solve():
    #이전 전류장, 목적지>> 충전소 리스트(energe)에 추가
    energe.append(N)   #목적지 추가
    energe.insert(0,0)  # 시작 정류소 번호는 0
    last_charge = 0 #시작점에서는 충전하고 시작함
    cnt=0 #충전횟수
    print(energe)
    #정류장을 하나씩 순회
    for i in range(1,M+2): #시작 정류장은 탐에서 제외
    #1.이전 정류장 이랑, 현재 정류장이랑 거리가 k보다 크면 목적지까지 못감
        if energe[i] -energe[i-1] > K: #정류장 사이의 거리가 k보다 먼 경우
            return 0
    #2.이전 충전위치에서 +k 한 거리보다 현재 정류장이 더 멀면 충전하면 됨
        if energe[i] > last_charge+K:
            last_charge = energe[i-1] #제일 먼곳에서 충전(직전 충전소)
            cnt += 1
    #목적지 도착하면 반복문이 끝이 납니다.
    return cnt




T=int(input())
for tc in range(1,T+1):
    K,N,M=map(int,input().split()) #k=충전하고 갈 수 있는거리,N=최종 정류장,M=충전소 갯수
    energe=list(map(int,input().split()))
    result = solve()
    print(f'#{tc} {result}')












