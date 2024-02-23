# 1 암호 코드를 찾는다
# 2 암호 코드를 이루는 숫자 확인
# 3. 암호 코드가 유효한지 확인
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
    # 암호 코드 시작점찾기
    for i in range(N):
        for j in range(M - 1, 54, -1):
            if data[i][j] == 1:  # 시작점 찾음
                # 여기서 부터는 암호코드를 해석 >> 숫자 8개로 바꾸기
                code = []  # 숫자 8개가 들어갈 리스트
                current = j
                for _ in range(8):
                    num = 0
                    w1, w2, w3, w4 = 0, 0, 0, 0
                    # 숫자 알아내서 num에 넣고
                    # 현재위치 부터 7개 비트 확인해서
                    # 1의 개수 세기
                    while data[i][current] == 1:
                        w4 += 1
                        current -= 1
                    # 0의 개수 세기
                    while data[i][current] == 0:
                        w3 += 1
                        current -= 1
                    # 1의 개수 세기
                    while data[i][current] == 1:
                        w2 += 1
                        current -= 1
                    # 0 의 개수 세기
                    w1 = 7 - w2 - w3 - w4
                    current -= w1
                #(w1,w2,w3,w4)를 알고있음
                    code.append(num_dic[(w1,w2,w3,w4)]) #암호코드찾음
                # print(code) #암호코드 정상출력확인
                even_sum = code[0] +code[2]+code[4]+code[6]
                odd_sum= code[1] +code[3]+code[5]+code[7]
                if (odd_sum*3 +even_sum)%10: #나누어 떨어지지않음
                    return 0
                return odd_sum +even_sum
                # 암호 코드가 정상 코드인지 확인



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]
    result =solve()
    print(f'#{tc} {result}')