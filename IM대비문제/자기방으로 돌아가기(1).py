# 경우 : 홀 -> 짝 / 홀 -> 홀 / 짝 -> 짝
# 2, 3의 몫이 1로 같고 4, 5 가 2로 같고... 를 이용해서 각각 마주 보고 있는 방에 1씩 더해서 겹쳐 움직이는 것 중에 가장 큰 값 return
 
def solve():
    cnt = [0] * 201 # 방 사이를 빈칸의 리스트로 생각 / 홀수방과 짝수방이 마주 보고 있으므로 200개 있다고 가정
    for i in room:
        if i[0] < i[1]:
            start = (i[0]+1) // 2
            end = (i[1]+1) // 2
        else:       # 뒷 번호의 방에서 앞 번호의 방으로 오는 경우도 생각
            end = (i[0]+1) // 2
            start = (i[1]+1) // 2
        for j in range(start, end+1):
            cnt[j] += 1
 
    return max(cnt)
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)] # [출발방, 도착방]
    # print(room)
    result = solve()
    print(f'#{tc} {result}')