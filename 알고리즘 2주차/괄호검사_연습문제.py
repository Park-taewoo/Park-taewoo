# 닫는 괄호가 나오면, 스택에 들어가 있는 마지막 여는 괄호가 내 짝궁
#1. 만약 닫는괄호가 나왔는데, 스택이 비어서 짝궁이 없으면 에러
#2. 더 이상 닫는 괄호가 없는데, 스택에 여는 괄호가 있으면 에러

#주어진 문자열(괄호)에서 괄호 짝이 맞으면 True, 아니면 False
def solve(dd):
    stack = []
    for i in range(len(data)):
    #1. 여는 괄호를 만나면 stack에 Push
        if data[i] == '(':
            stack.append(data[i])
    #2. 닫는 괄호를 만나면 stack에 pop
        elif data[i] == ')':
            if not stack : #스택이 비어있으면 if len(stack) ==0: 같은 문장
               return False
            stack.pop()
    #   2번이 안되거나 stack에 여는 괄호가 남으면 에러
    if stack: #stack에 요소가 있으면(여는 괄호가 남아있으면)
        return False
    #반복문 도는 동안 짝궁도 다 맞고.. 남은것도 없네? >>>참
    return True

data = input()
print(solve(data))