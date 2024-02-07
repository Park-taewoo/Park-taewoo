def solve():
    stack =['@']
    for i in s:
        if stack[-1] != i:
            stack.append(i)
        elif stack [-1] == i:
            stack.pop()
    return len(stack)-1


T = int(input())
for tc in range(1,T+1):
    s = input()
    result =solve()
    print(f'#{tc} {result}')