# def kfc(x):
#     if x ==3:
#         return
#     kfc(x+1)
#     kfc(x+1)
#     print(x)
# kfc(0)

N=3
k=5
idx_lst=[None]*k
def func(idx):
    if idx == k:
        print(idx_lst)
        return
    for i in range(N):
        idx_lst[idx] = i
        func(idx+1)
func(0)




#중복순열
path = []
def type1(x):
    if x == N:
        print(path)
        return

    for i in range(1,7):
        path.append(i)
        type1(x+1)
        path.pop()

#순열
def type2(x):
    if x == N:
        print(path)
        return

    for i in range(1,7):
        if used[i] == True : continue
        used[i] = True
        path.append(i)
        type2(x+1)
        path.pop()
        used[i] = False

used = [False for _ in range(7)]
N,type = map(int,input().split())

if type==1:
    type1(0)
if type==2:
    type2(0)