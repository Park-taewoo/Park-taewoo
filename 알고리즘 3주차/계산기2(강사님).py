
for tc in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''    # 후위표기법 저장
    S = []

    # 토큰을 읽어온다. => 한글자씩 읽어온다.
    for token in infix:
        # 토큰을 연산자/피연산자로 구분
        if token == '+':
            if S: # 빈스택이 아니면 먼저나온 +를 출력
                postfix += S.pop()
            S.append(token)  # 스택에 push
        elif token == '*':
            if S and S[-1] == '*':
                postfix += S.pop()
            S.append(token)  # 스택에 push
        else:
            postfix += token # 피연산자인 경우 출력

    while S:
        postfix += S.pop()

    # 후위표기를 계산
    for token in postfix:
        if token == '+':
            # 필요한 피연산자를 스택에서 pop
            b = S.pop()
            a = S.pop()
            S.append(a + b)
        elif token == '*':
            b = S.pop()
            a = S.pop()
            S.append(a * b)
        else: # 피연산자
            S.append(int(token))
    print(f'#{tc} {S[0]}')