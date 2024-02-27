
T = int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    #16진수 데이터
    hex_data = [input() for _ in range(N)]
    # 2진수 데이터가 필요하기 때문에 2진수로 데이터로 변경
    bin_data= []
    for i in range(N):
        row = ''
        for j in range(M):
            hex_dict[hex_data[i][j]]