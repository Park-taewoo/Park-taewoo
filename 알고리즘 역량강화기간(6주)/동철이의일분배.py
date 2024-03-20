# 완전탐색 + 가지치기 >> 백트래킹
# 각 직원이 모든 업무를 수행하는 경우의 수를 고려 : 완전탐색
# idx : 직원의 번호
# rate: 직원들이 업무를 수행했을 때, 성공할 확률 누적합
def solve(idx, rate,selected:set):
    if idx ==N: #모든 직원이 업무를 모두 골랐으면 그만
        print(rate*100)
        return


    # i : 업무번호
    for i in range(N):
        # arr[idx][i] : idx번 직원이 i번 업무를 성공할 확률
        if i not in selected:
            selected.add(i)
            solve(idx+1,rate * arr[idx][i],selected)
            selected.remove(i)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100

    solve(0,1,set())
