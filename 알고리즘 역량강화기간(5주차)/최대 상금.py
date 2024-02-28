def dfs(num):
    global answer
    if num==N:
        answer = max(answer, int("".join(map(str, lst))))
        return
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]

            chk = int("".join(map(str, lst)))
            if (num, chk) not in v:
                dfs(num+1)
                v.append((num,chk))

            lst[j], lst[i] = lst[i], lst[j]

T = int(input())

for test_case in range(1, T + 1):
    st, t = map(str, input().split())
    N = int(t)
    lst, v = [], []
    L = len(st)
    answer = 0
    for i in st:
        lst.append(i)
    dfs(0)
    print(f'#{test_case} {answer}')