# def itoa(num):
#     result=[]
#     while num: # 0이 아닌동안
#         result.append(num%10)
#         num //=10
#     result.reverse()
#     return result

# def atoi(arr):
#     value = 0
#     for item in arr:
#         value = value*10 +item
#     return value

# num=int(input())
# arr =itoa(num)
# print(arr)
# print(atoi(arr))

def check(num):
    cnt=0
    while num:
        digit = num %10
        num //= 10
        if digit !=0 and digit %3 == 0:
            cnt+=1
    return cnt   
    
N=int(input())
for i in range(1,N+1):
    cnt = check(i)
    if cnt:
        for j in range(cnt):
            print('-',end='') #연속으로 붙이기
        print(' ',end='')
    else:
        print(i,end=' ')  