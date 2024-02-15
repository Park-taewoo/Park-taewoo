# 큐 구현에 필요한 상태값
# q : 실제 데이터가 저장될 배열
# rear : 마지막 요소를 가리키는 변수,
# front : 제일 앞요소(다음에 삭제될 요소)를 가리키는 변수
# 큐에서 수행할 수 있는 동작
# 삽입 : enQueue
# 삭제 : deQueue
# 다음요소 확인 : peek
# 큐가 비었는지 확인 : isEmpty
# 큐가 가득찼는지 확인 : isFull
class Queue:
    def __init__(self, size=10):
        self.q = [None] * size
        self.front = -1
        self.rear = -1

    # 큐에 데이터 삽입
    def en_queue(self, value):
        if self.is_full():
            print('가득 찼는데요?')
        else:
            self.rear += 1
            self.q[self.rear] = value

    # 큐에서 데이터 삭제(큐안의 요소중에 제일먼저 삽입된 요소를 반환 및 삭제)
    def de_queue(self):
        if self.is_empty():
            print('큐가 비었어요')
            return None
        self.front += 1
        return self.q[self.front]

    # 큐가 비었는지 확인 : front와 rear가 같으면 비어있음
    def is_empty(self):
        return self.front == self.rear

    # 큐가 가득 찼는지 확인
    def is_full(self):
        return self.rear == len(self.q) - 1

    # 다음에 빠져나갈 요소(가장 먼저 삽입된 요소 반환)
    def peek(self):
        if not self.is_empty():
            return self.q[self.front + 1]
        print('큐가 비었습니다.')
        return None


class Queue2:
    def __init__(self, size=10):
        self.q = [None] * size
        self.size = size
        # 똑같으면 큐가 비었다. rear 다음 칸이 front면 가득찼다.
        self.front = 0
        self.rear = 0

    # rear의 다음칸에 front가 있을때
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.rear == self.front

    def en_queue(self, value):
        # (self.rear + 1) % self.size
        # 마지막 칸일때 0번으로 돌아가기 위해서 나머지 연산을 활용
        if self.is_full():
            print('큐가 가득 찼습니다.')
        else:
            self.rear = (self.rear + 1) % self.size
            self.q[self.rear] = value

    def de_queue(self):
        if self.is_empty():
            print('큐가 비었습니다')
        else:
            self.front = (self.front + 1) % self.size
            return self.q[self.front]


# 이야기가 나온김에.....
class Node:
    def __init__(self, value):
        self.value = value  # 노드의 value
        self.next = None  # 다음 노드 요소


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def en_queue(self, value):
        # 새로운 노드를 만들어서
        # rear의 next에 연결하기
        # 요소가 없으면 rear에 연결
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def de_queue(self):
        # 요소가 하나 밖에 없음!
        value = self.front.value
        if self.front.next is None:
            self.front = None
            self.rear = None
        else:
            # 원래 프론트의 next를 새로운 front로
            self.front = self.front.next
        return value


queue = LinkedQueue()
queue.en_queue('A')
print(queue.de_queue())
queue.en_queue('B')
print(queue.de_queue())
queue.en_queue('C')
print(queue.de_queue())
queue.en_queue('D')
print(queue.de_queue())




queue = Queue2(10)
queue.en_queue('A')
queue.en_queue('B')
queue.en_queue('C')
queue.en_queue('D')
queue.en_queue('E')
queue.en_queue('F')
queue.en_queue('G')
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
queue.en_queue('A')
queue.en_queue('B')
queue.en_queue('C')
queue.en_queue('D')
queue.en_queue('E')
queue.en_queue('F')
queue.en_queue('G')
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
