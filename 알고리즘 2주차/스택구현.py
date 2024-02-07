# 스택 구현하기 클래스로 짜기
# 상태값 : 데이터를 저장할 배열
#        마지막 요소를 가리키는 변수
#        최대 크기
# 행동 : 삽입, 삭제, 비었는지 확인, 마지막 요소 반환..등등
class Stack:
    def __init__(self, max_size=10):
        self.s = [None] * max_size
        self.top = -1
        self.max_size = max_size

    def push(self, value):
        # 스택이 가득 찼으면 넣지마라!
        if self.is_full():
            print('Stack is full!!')
        else:
            self.top += 1
            self.s[self.top] = value

    # 마지막 요소 반환하고 삭제
    def pop(self):
        if self.is_empty():
            print('Stack is empty!!')
        else:
            result = self.s[self.top]
            self.top -= 1
            return result

    def is_empty(self):  # 비었는지 확인
        if self.top == -1:
            return True
        return False

    def is_full(self):  # 가득 차있는지 확인
        if self.top + 1 == self.max_size:
            return True
        return False

    # 마지막요소 반환
    def peek(self):
        if not self.is_empty():
            return self.s[self.top]

    def __str__(self):
        return str(self.s)


stack = Stack(5)
stack.push('A')
stack.push('B')
stack.push('C')
print(stack.pop())
print(stack.pop())
print(stack.pop())
