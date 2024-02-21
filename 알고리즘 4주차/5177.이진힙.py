def heap_push(value):  # heap에 요소 추가
    global heapcount
    global N
    global sum
    # 마지막 위치에 요소 추가
    for i in value:
        heapcount += 1
        heap[heapcount] = i
        # 부모요소와 크기비교 해서 부모보다 작다면 자리 바꾸기(-반복)

        current = heapcount  # 현재 : heapcount
        parent = current // 2  # 부모 : heapcount//2

        # 부모보다 자식이 작다면
        while parent > 0 and heap[current] < heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]

            current = parent
            parent = current // 2

    while True:
        N=N//2
        if N == 0 :
            break
        sum += heap[N]


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    A=list(map(int,input().split()))
    heap = [None]*(N+1)
    heapcount = 0
    sum = 0
    heap_push(A)
    print(f'#{tc} {sum}')
