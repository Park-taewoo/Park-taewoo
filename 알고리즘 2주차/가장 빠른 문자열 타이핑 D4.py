T = int(input())

for tc in range(1, T+1):
    str_A, str_B = input().split()
    str_A=list(str_A)
    str_B=list(str_B)
    len_A = len(str_A)
    len_B = len(str_B)
    cnt = 0

    for i in range(len_A-len_B+1):
        if str_A[i:i+len_B] == str_B:
            str_A[i:i + len_B] ='*'
            cnt += 1

    result = len_A - (len_B*cnt) + cnt

    print(f'#{tc} {result}')


