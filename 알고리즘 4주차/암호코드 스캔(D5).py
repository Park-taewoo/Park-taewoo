def solve():
    num_dic = {
        (3, 2, 1, 1): 0,
        (2, 2, 2, 1): 1,
        (2, 1, 2, 2): 2,
        (1, 4, 1, 1): 3,
        (1, 1, 3, 2): 4,
        (1, 2, 3, 1): 5,
        (1, 1, 1, 4): 6,
        (1, 3, 1, 2): 7,
        (1, 2, 1, 3): 8,
        (3, 1, 1, 2): 9,
    }
    d = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
          '4': "0100", '5': "0101", '6': "0110", '7': "0111",
          '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
          'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
    new_data=[] #암호코드일 가능성이 있는 아이를 받아오는 변수
    for i in range(N):
        for j in range(M):
            if data[i][j] !=0:
                new_data.append(data[i])
                break












T= int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    data = [list(map(int, input())) for _ in range(N)]
    result =solve()
    print(f'#{tc} {result}')