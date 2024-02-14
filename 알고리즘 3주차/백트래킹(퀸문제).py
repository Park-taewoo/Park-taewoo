# 완전탐색하다 어 이거 아닌거 같은데 하면 탐색 안함
# N*N 행렬에 N개의 퀸을 놓을 수 있는 경우의 수는 몇개?
N = int(input())
arr = [[0] * N for _ in range(N)]  # 모양을 알고 싶으면 생성
cnt = 0
col = [0] * N  # 열에 퀸이 놓였는지 표시
# row행에 퀸을 놓기
# 대각선 표시를 위한 배열
dia1 = [0] * (N * 2 - 1)  # r+c    #대각선갯수
dia2 = [0] * (N * 2 - 1)  # r-c +(N-1)


def dfs(row):
    global cnt
    if row == N:
        # 모든행에 퀸 다 놓았음, 하나의 정답 케이스를 찾았음
        for r in arr:
            print(r)
        print('----------------')
        cnt += 1
        return

    # 퀸 놓기 >> 모든 열에 놓아보기
    for i in range(N):
        if not col[i] and not dia1[row + i] and not dia2[row - i + N - 1]  : #col[i] == 0
            arr[row][i] = 1
            col[i] = 1
            dia1[row + i] = 1
            dia2[row - i + N - 1] = 1

            dfs(row + 1)

            arr[row][i] = 0
            dia1[row + i] = 0
            dia2[row - i + N - 1] = 0
            col[i] = 0


dfs(0)
print(cnt)