T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    i = 0 #A를 이동하는 인덱스
    j = 0 #B를 이동하는 인덱스
    cnt = 0
    while i < N:
        # A[i],B[j] 둘이 똑같은지 보면 된다.
        # 같으면 j,i 각각 1씩 증가
        if A[i] == B[j]:
            i += 1
            j += 1
        else: # 다르면 j는 0으로 돌리고, i는 다음 칸으로 이동
            i = i - j + 1
            j = 0
        # j가 M이라면 패턴을 찾으면 패턴갯수증가
        if j == M :
            cnt += 1
         # j = 0,i는 그대로 두면됨
            j=0
    print(f'#{tc} {N-(M-1)*cnt}')