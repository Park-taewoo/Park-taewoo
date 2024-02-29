def solve():
    for _ in range(M):
        a,b,c = map(int, input().split())
        a -= 1
        b -= 1
        arr[a][b] =c
        for i in range(1,N):
            if 0<=a+i<N and 0<=b+i<N:
                if c==1:
                    if arr[a+i][b] == 1: #아래

                    if arr[a-i][b]==1: #위

                    if arr[a][b+i] == 1: #오른쪽

                    if arr[a][b-i] == 1: #왼쪽

                    if arr[a-i][b-i] == 1: #왼 아래대각

                    if arr[a+i][b - i] == 1: #왼 윗대각

                    if arr[a - i][b + i] == 1: #오른 아래대각

                    if arr[a + i][b + i] == 1:  # 오른 윗대각

T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[0]*N for _ in range(N)]
    result= solve()