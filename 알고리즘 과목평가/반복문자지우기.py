T = int(input())
for tc in range(1, T+1):
    s = input()     # 문자열
    stack = []
 
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        elif stack[-1] != i:
            stack.append(i)
 
    print(f'#{tc} {len(stack)}')

# 3
# ABCCB
# NNNASBBSNV
# UKJWHGGHNFTCRRCTWLALX