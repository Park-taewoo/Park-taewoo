def solve():
    arr = list(map(int,input().split()))
    jump_sum=0 #점프해서 얻은 합의 변수
    frog_which=0 #개구리 위치를 나타내는 변수
    a=0
    for i in range(K):
 #점프해서 얻은 합
        if arr[frog_which]>0 and arr[a]<0:
            frog_which = arr[frog_which] - arr[a]
            a = frog_which
            if frog_which < 0 or frog_which > N:  # 개구리가 연못을 벗어나면 게임 끝
                break
            jump_sum += arr[frog_which]

        else:
            a=frog_which
            frog_which = frog_which + arr[a]#개구리의 위치를 그 번호만큼 점프한다
            if frog_which < 0 or frog_which > N:  # 개구리가 연못을 벗어나면 게임 끝
                break
            jump_sum += arr[frog_which]

    return jump_sum

T=int(input())
for tc in range(1,T+1):
    N,K=map(int,input().split())
    result=solve()
    print(f'#{tc} {result}')


