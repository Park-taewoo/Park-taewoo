def solve():
     
# 최댓값의 위치 찾기
# 돌면서 빼기
# 반복
    money = 0   #판매 수익을 저장할 변수
    start = 0
    while start < N: #이익 구하기
        # 최댓값 찾기
        max_idx = start
        for i in range(start, N):
            if arr[i] > arr[max_idx]:
                max_idx = i
        # 최댓값 찾음!
        for i in range(start, max_idx):
            money += arr[max_idx] - arr[i]
 
        start = max_idx + 1
    return money
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = solve()
    print(f'#{tc} {result}')