def f(i, k, t): # k개의 원소를 가진 배열A, 부분집합 합이 t인경우
    if i == k:  # 모든 원소에 대해 결정하면
        ss = 0  # 부분집합 원소의 합
        for j in range(k):
            if bit[j]:  # A[i]가 포함된경우
                #print(A[j], end=' ')
                ss += A[j]
        if ss == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end = ' ')
            print()
        #print(ss)
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i + 1, k, t)
        # bit[i] = 1
        # f(i + 1, k)
        # bit[i] = 0
        # f(i + 1, k)


N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N  # bit[i]는 A[i]가 부분집합에 포함되는지 표시
f(0, N, 10)


def f1(i, k, s, t):
    if s ==t :
        for j in range(k):
            if bit[j]:
                print(A[j], end=' ')
        print()
    elif i == k:
        return
    elif s > t:
        return

    else:
        bit[i] = 1
        f1(i + 1, k,s+A[i],t)
        bit[i] = 0
        f1(i + 1, k, s, t)


N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N  # bit[i]는 A[i]가 부분집합에 포함되는지 표시
f1(0, N, 0,  10)
