def solve():
    max_sum = -1
    D = 0  # 곱의 단조를 확인하기 위한 변수
    for i in range(A):
        for j in range(A):
            if i < j :
                b = arr[i]*arr[j]
                c = str(b)
                cnt = 0
                if max_sum < b:
                    for q in c:  # 곱이 단조 인지 확인
                        if D <= int(q):
                            cnt += 1
                            D = int(q)
                            if cnt == len(c) and max_sum < b:
                                max_sum = b
                        else:
                            break
                    D = 0
    return max_sum




T = int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    A = len(arr)
    result = solve()
    print(f'#{tc} {result}')