# heap 구현
# 완전이진트리
# 최대(최소)힙 : 모든 부모노드가 자식노드보다 큰(작은)값을 가짐
# 최대 힙:힙안의 최대값은 트리의 루트에 위치함
# 최소힙:힙안의 최소값은 트리의 루트에 위치함
# 데이터를 pop() 하면 최대(최소)값이 삭제되면서 반환

# 완전이진트리이므로 배열에 트리를 저장한다.
heap = [None] * 16
# 현재 마지막 노드의 위치를 알아야 삽입 또는 삭제가 가능하다.
heapcount = 0  # 힙안의 마지막 요소를 가리키는 변수


# 최대 힙
def heap_push(value):  # heap에 요소 추가
    global heapcount
    # 마지막 위치에 요소 추가
    heapcount += 1
    heap[heapcount] = value
    # 부모요소와 크기비교 해서 부모보다 크다면 자리 바꾸기(-반복)

    current = heapcount  # 현재 : heapcount
    parent = current // 2  # 부모 : heapcount//2

    # 부모보다 자식이 크면
    while parent > 0 and heap[current] > heap[parent]:
        heap[current], heap[parent] = heap[parent], heap[current]

        current = parent
        parent = current // 2


heap_push(3)
heap_push(7)
heap_push(4)
heap_push(2)
heap_push(9)
heap_push(1)
heap_push(5)
print(heap)


def heap_pop():  # heap에서 최대값 반환 및 삭제
    global heapcount
    # 루트에 있는 요소 반환 및 삭제
    # 마지막에 있는 요소를 루트에 복사
    # 자식요소 중 더 큰 요소와 비교해서 부모노드가 더 작다면 교환(-반복)
    result = heap[1]
    heap[1] = heap[heapcount]
    heapcount -= 1
    parent = 1
    # child = 왼쪽 자식과 오른쪽 자식중 큰값의 번호
    child = parent * 2  # 왼쪽 자식으로 일단 선택
    if child + 1 <= heapcount: # 오른쪽 있니?
        if heap[child] < heap[child + 1]:
            child += 1
    #일단 둘 중에 큰 걸로 선택완료
    while child <= heapcount and heap[child] > heap[parent]:
        heap[child] ,heap[parent] = heap[parent] ,heap[child]
        #또 child를 새롭게 선택해야 하는데..
        parent = child

        child = parent * 2  # 왼쪽 자식으로 일단 선택
        if child + 1 <= heapcount:  # 오른쪽 있니?
            if heap[child] < heap[child + 1]:
                child += 1
    return result

