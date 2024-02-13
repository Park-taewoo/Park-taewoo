# (6+5*(2-8)/2)
# 중위표기식 > 후기표기식
# 먼저 연산되는게 먼저 튀어 나와야 한다!
# 연산 우선순위가 높은 연산자가 먼저 나와야 합니다...
# 연산자를 만나면 stack에 넣을건데...
#  1. 만약 현재 연산자 보다 우선순위가 낮은 연산자가
#     stack안에 있으면 들어가도 먼저나올 수 있음(stack이니까)
#    우선순위가 낮은 연산자가 stack안에 있으면 push
#  2.만약 현재 연산자 보다 우선순위가 높거나 같은 연산자가
#   stack안에 있으면...stack에 있는거 빼고 push
post_exp = ''   # 후위 표기식
stack = []
in_exp = input()    #중위 표기식
# 중위 표기식을 하나씩 읽기
icp = { #스택 안에 들어갈 때 우선순위
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '(' : 3
}
isp = { # 스택 안에서 우선순위
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0
}
for chr in in_exp:
    if chr in '+-*/()': #연산자 라면...
        if chr == ')':  #닫는 괄호라면...
            # 여는 괄호가 나올때 까지 다 빼면서 출력
            # 여는 괄호는 버림
            while stack and stack[-1] != '(':
                post_exp += stack.pop()
            stack.pop() #여는 괄호 삭제
        # stack에 넣고 빼고...작업해야 합니다.
        elif not stack:   #스택이 비었으면??
            stack.append(chr)
        else:   #스택이 비어있지 않음
            #현재 연산자보다 우선순위가 높은애가 stack에 있는지 확인...
            # if isp[stack[-1]] < icp[chr]:
            #     stack.append(chr)
            # else:   # 스택안에 있는 애가 나보다 우선순위가 높은데?
            #     while stack and isp[stack[-1]] >= icp[chr]:
            #             post_exp += stack.pop()
            #     stack.append(chr)
            while stack and isp[stack[-1]] >= icp[chr]:
                    post_exp += stack.pop()
            stack.append(chr)

    else:   #피연산자 라면 그냥 출력
        post_exp += chr
# 남아있는 애들 다 붙이기
while stack:
    post_exp += stack.pop()
print(post_exp)
# 6528-*2/+
# 후위 표기식 연산 (한자리 숫자만 있음..이라고 가정)
# 피연산가 나오면 stack에 넣고
# 연산자가 나오면 stack에서 두 개 빼서 연산해서 다시 넣기
# 표현식이 끝나면 stack에  마지막에 남아있는 숫자가 결과
stack = []
for chr in post_exp:
    if chr in '0123456789': #피연산자라면...
        stack.append(int(chr))
    else: # 연산자
        num2 = stack.pop()
        num1 = stack.pop()
        if chr == '+':
            stack.append(num1 + num2)
        elif chr == '-':
            stack.append(num1 - num2)
        elif chr == '*':
            stack.append(num1 * num2)
        else:
            stack.append(num1 // num2)
print(stack[-1])
