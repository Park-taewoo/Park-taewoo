T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    d1=[-1,1,0,0]
    d2=[0,0,-1,1] # 상하좌우
    d3=[-1,-1,1,1] # 대각 위 좌 우 아래 좌 우
    d4=[-1,1,-1,1]
    max_num=0
    for i in range(N):
        for j in range(N):
            cnt = 0
            cnt1 = 0
            cnt += arr[i][j]
            cnt1 += arr[i][j]
            for k in range(1,M):  # + 모양 검사
                for q in range(4):
                    n = i + d1[q]*k
                    r = j + d2[q]*k
                    if 0<= n < N and 0<= r <N:
                        cnt += arr[n][r]
            for k in range(1,M):  # 대각 모양 검사
                for q in range(4):
                    n = i + d3[q]*k
                    r = j + d4[q]*k
                    if 0<= n < N and 0<= r <N:
                        cnt1 += arr[n][r]
            if max_num < cnt:
                max_num = cnt
            if max_num < cnt1:
                max_num = cnt1
    print(max_num)









# 2
# 5 2
# 1 3 3 6 7
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3
# 6 3
# 29 21 26 9 5 8
# 21 19 8 0 21 19
# 9 24 2 11 4 24
# 19 29 1 0 21 19
# 10 29 6 18 4 3
# 29 11 15 3 3 29

