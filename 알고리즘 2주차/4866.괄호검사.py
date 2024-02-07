def solve(data):
    stack = []
    for i in data:
        if i == '(' or i == '{': # '('과 '{'는 스택에 추가
            stack.append(i)
        elif stack and i == '}' and stack[-1] == '{': # '}'을 만났는데 stack에 마지막원소가 '{'이면 '{' pop
            stack.pop()
        elif stack and i == ')' and stack[-1] == '(': # ')'을 만났는데 stack에 마지막원소가 '('이면 '(' pop
            stack.pop()
        elif i == ')' or i =='}': #위에 경우가 아니면 스택에 push
            stack.append(i)
    if stack:  #스택이 있으면
        return 0
    return 1 #스택이 비어있으면

T = int(input())
for tc in range(1,T+1):
    data = input()
    result=solve(data)
    print(f'#{tc} {result}')