T = int(input())
for tc in range(1,T+1):
    A, B = map(int, input().split())
    code = []
    for _ in range(A):
        code.append(input())

    code_Translate = []
    for i in code:
        if '1' in i:
            code_Translate.append(i)
            break

    result = []
    for j in code_Translate[0]:
        result.append(j)
    lenth = len(result)
    code_review = []
    for k in range(lenth - 1, -1, -1):
        if result[k] == '1':
            code_review.append(result[k - 55:k + 1])
            break
    str = []
    for q in range(0, 56, 7):
        str.append(code_review[0][q:q + 7])

    good=''
    good2 = 0
    for t in range(len(str)):
        if str[t] == ['0', '0', '0', '1', '1', '0', '1']:
            good +=  '0'
            good2 += 0
        elif str[t] == ['0', '0', '1', '1', '0', '0', '1']:
            good += '1'
            good2 += 1
        elif str[t] == ['0', '0', '1', '0', '0', '1', '1']:
            good += '2'
            good2 += 2
        elif str[t] == ['0', '1', '1', '1', '1', '0', '1']:
            good += '3'
            good2 += 3
        elif str[t] == ['0', '1', '0', '0', '0', '1', '1']:
            good += '4'
            good2 += 4
        elif str[t] == ['0', '1', '1', '0', '0', '0', '1']:
            good += '5'
            good2 += 5
        elif str[t] == ['0', '1', '0', '1', '1', '1', '1']:
            good += '6'
            good2 += 6
        elif str[t] == ['0', '1', '1', '1', '0', '1', '1']:
            good += '7'
            good2 += 7
        elif str[t] == ['0', '1', '1', '0', '1', '1', '1']:
            good += '8'
            good2 += 8
        else:
            good += '9'
            good2 += 9
    c,v =0,0
    for w in range(1,9):
        if w%2 == 1:
            c += int(good[w-1])
        else:
            v += int(good[w-1])
    if ((c*3)+v)%10 == 0:
        print(f'#{tc} {good2}')
    else:
        print(f'#{tc} 0')