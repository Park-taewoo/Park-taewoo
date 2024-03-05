#시간 초과가 뜸
# N=int(input())
# arr=list(range(1,N+1))


# for i in range(N-1):
#     arr.pop(0)
#     A=arr.pop(0)
#     arr.append(A)
# print(*arr)


#시간초과를 위해 라이브러리 사용
from collections import deque

def card(N):
    queue = deque(range(1, N+1))

    while len(queue) > 1:
        queue.popleft() #왼쪽 끝의 원소를 제거 후 반환
        queue.append(queue.popleft()) 
    return queue[0]

N = int(input())
print(card(N))