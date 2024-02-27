T = int(input())
for tc in range(1,T+1):
    #D : 두 기차의 거리,A의 속력,B의속력,F: 파리의 속력
    D,A,B,F = map(int,input().split())
    T = D*F / (A+B)
