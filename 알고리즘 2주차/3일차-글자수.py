T=int(input())
for tc in range(1,T+1):
    str1=str(input())
    str2=str(input())
    max_str=0

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt +=1

        if max_str < cnt:
            max_str = cnt
    print(f'#{tc} {max_str}')
