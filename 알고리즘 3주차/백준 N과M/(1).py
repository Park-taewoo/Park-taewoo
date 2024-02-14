n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))        
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()



    





















n,m = map(int,input().split())
s=[]
def solve():
    if len(s)==m:
        print(' '.join())
        return
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            solve()
            s.pop()