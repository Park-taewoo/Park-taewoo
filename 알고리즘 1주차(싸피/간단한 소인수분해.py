def solve():
    N=int(input())
    result_2 = 0
    result_3 = 0
    result_5 = 0
    result_7 = 0
    result_11 = 0
    while 1:
        if N%2==0:
            N=N//2
            result_2 +=1
        elif N%3==0:
            N=N//3
            result_3 +=1
        elif N%5==0:
            N=N//5
            result_5 +=1
        elif N%7==0:
            N=N//7
            result_7 +=1
        elif N%11==0:
            N=N//11
            result_11 +=1
        if N ==1:
            break
    return result_2, result_3, result_5, result_7, result_11

T = int(input())
for tc in range(1, T + 1):
    result_2, result_3, result_5, result_7, result_11 = solve()
    print(f'#{tc} {result_2} {result_3} {result_5} {result_7} {result_11}')