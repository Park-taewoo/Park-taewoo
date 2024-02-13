def solve():
    stack=[]
    for i in arr:
        if i in '123456789':
            stack.append(i)
    ret = 0
    for j in stack:
        ret += int(j)
    return ret
T=10
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(str,input()))
    result=solve()
    print(f'#{tc} {result}')

