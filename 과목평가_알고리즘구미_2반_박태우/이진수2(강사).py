# 소수점 이하 num을 이진수로 바꾸어서 반환하는 함수
# 단, 13자리 이상이라면 'overflow'를 반환
def solve(num):
    result = ''
    # 0.5 부터 시작해서 0.25 0.125 ....을num 에서 빼보기
    n = 1/2
    while True:
        if num >= n:
            result += '1'
            num -= n
            if num == 0:
                break
        else:
            result += '0'
        n /= 2
 
        if len(result) > 12:
            result = 'overflow'
            break
    return result
 
T = int(input())
for tc in range(1,T+1):
    N = float(input())
    result = solve(N)
    print(f'#{tc} {result}')