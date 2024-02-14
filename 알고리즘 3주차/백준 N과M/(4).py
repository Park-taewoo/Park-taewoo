n,m = map(int,input().split())
s=[]

def solve():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for j in range(1,n+1):
        if not s or s[-1] <= j:
            s.append(j)
            solve()
            s.pop()
        
solve()