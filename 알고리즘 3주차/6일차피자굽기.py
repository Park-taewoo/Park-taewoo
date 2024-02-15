def solve():
    pass

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    cheese = list(map(int,input().split()))
    pizza = []
    for i range(M):
        pizza.append([i+1,cheese[i]])
    in_oven =pizza[:N]
    remain = pizza[N:]

    while len(in_oven)>1:
        check = in_oven.pop(0)
        check[1] //=2

        if check[1] == 0:
            if remain:
                in_oven.append(remain.pop(0))
        else:
            in_oven.append(check)

    in_oven[0]