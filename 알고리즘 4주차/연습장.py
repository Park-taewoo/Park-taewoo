# N =int(input())
#
# lst = [[0]*7 for _ in range(2)]
#
# t1 = N
# for i in range(4):
#     lst[0][i] = t1
#     t1 += 1
#
# t2 = N
#
# for i in range(6,2,-1):
#     lst[1][i] = t2
#     t2 -= 1
#
# print(lst[0])
# print(lst[1])
# import sys
# sys.stdin = open('input.txt', 'r') #r 은 read약자
# sys.stdout = open('output.txt', 'w') #w 은 write의 약자
#
# a,b = map(int,input().split())
# print(a+b)
# print(a*b)

# t =149
# result =[]
#
# while t != 0:
#     result.append(t%2)
#     t//=2
#
#
# result.reverse()
# print(result)
# dic16={'A':10, 'B':11,'C':12, 'D':13,'E':14, 'F':15}
# a=dic16['A']
# print(a)

# print(0b11011110& 0b11011)
# print(0x4A3| 25)

# #신기한 XOR 연산
# key = 1004
#
# def encode_decode(num):
#     return num ^ key
# print(encode_decode(1000))
# print(encode_decode(4))

t = 1
for i in range(5):
    print(bin(t),t)
    t = t << 1

t= 0.1
print(f'{t:.2f}')

pri