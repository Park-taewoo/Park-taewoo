import pprint
def solve():
    for i in range(N):
        r1,c1,r2,c2,color=map(int,input().split())
        for i in range(r1,r2+1): #행
            for j in range(c1,c2+1): #열
                my_list[i][j] += color
    pprint.pprint(my_list)
    cnt = 0
    for k in range(10):
        for u in range(10):
            if my_list[k][u] == 3:
                cnt += 1
    return cnt




T=int(input()) #(테스트 횟수 입력)
for tc in range(1,T+1):
    N=int(input())
    my_list = [[0] * 10 for _ in range(10)] #10x10 빈 배열생성
    result=solve()
    print(f'#{tc} {result}')

