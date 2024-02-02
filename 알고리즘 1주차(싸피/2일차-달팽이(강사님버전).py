#from pprint import pprint as print #pprint 모둘을 print로 사용가능

#인자로 받은 N*N 행렬에 나선모양으로 숫자 채우기
def solve(arr):
    r,c = 0,0
    d = 0 #0:우,1:하,2:좌,3:상
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    num = 1
    # 한 칸씩 이동... 숫자 다 채울때 까지
    while True:
        #숫자 채워넣기
        arr[r][c] = num
        num += 1
        #다음에 이동할 칸으로 좌표계산
        r += dr[d]
        c += dc[d]
        #r,c가 정상범위인지 확인
        #비정상이면 방향전환
        if (0<= r < N and 0<= c < N and arr[r][c] == 0) : #정상
            pass
        else:
            r -= dr[d]
            c -= dc[d]
            d += 1  #방향전환환
            d = d % 4
            r += dr[d]
            c += dc[d]
        if num > N*N:
            break
    return arr
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)] #N*N 2차원 배열 만들기
    solve(arr)
    print(f'#{tc}')
    for row in arr:
        print(*row)