#브루트 포스 이용...
# 함수를 짜는 기준?
# 1. 정말 많은 루프를 탈출해야한다…     Ex)100개 중 98개를 체크해야함…
# 2, 반복적으로 어떤 것을 수행 해야한다. 
# 3. 짜고 보니까 많이 써야되는 거여서, 미리 툴을 만든다는 느낌으로…


def solve():
    N = 9
    #sol1: 9개 중 7개를 일일이 순회돌려서 100인 것을 찾는 것 - 귀찮음.
    #sol2: 9개 합을 구한 후 이들 중에서 2개만 빼서 100인것을 찾는 것이 접근성이 더 용이함.(중요!!!)
    num = sum(lst)-100              # 찾아야 할 숫자를 계산(sol2를 이용!)
    for i in range(N-1):
        for j in range(i+1, N):     # N개중에서 2개를 뽑는 모든 조합
            if lst[i]+lst[j]==num:
                return lst[i], lst[j]

lst = [int(input()) for _ in range(9)]
# 중요!!!
# 위의 input 형태는
# a하고 enter하면 lst에 추가되고
# b하고 enter하면 lst에 추가되고 이런 느낌임..(너무 map(list(int,input().split()))에서 split()메소드에 적응되버려서 문제가 생김.
n, m =solve()   # 7명에 포함되지 않는 2명 찾기 
                # n과 m으로 lst[i], lst[j]가 쏙쏙 들어간다.(중요! 이 툴에 익숙해지자!!)
for i in sorted(lst):
    if i!=n and i!=m:
        print(i) #lst의 요소 개수만큼 반복해서 한 줄 마다 i가 출력됨!