def solve():
    stack=[]
    for i in lst:
        if i in '+*/-':
            if len(stack) <= 1:
                return 'error'
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':
                stack.append(num1+num2)
            elif i == '-':
                stack.append(num1 - num2)
            elif i == '/':
                stack.append(num1 // num2)
            elif i == '*':
                stack.append(num1 * num2)
        elif i == '.':
            if len(stack)>=2:
                return 'error'
            pass
        else:
            stack.append(int(i))
    return stack[0]

T=int(input())
for tc in range(1,T+1):
    lst = list(map(str,input().split()))
    result=solve()
    print(f'#{tc} {result}')