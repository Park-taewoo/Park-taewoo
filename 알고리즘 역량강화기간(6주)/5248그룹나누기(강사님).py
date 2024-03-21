# 신청서를 보고 신청한 쌍을 하나의 그룹으로 만들어주기
# 모든 학생을 대표를 확인해서 몇 개의 그룹이 만들어졌는지 확인
# 특정 요소의 대표를 반환하는 함수
def find_set(x):
    # 대표 : 요소 스스로가 부모인 요소
    if p[x] == x:
        return x
    while p[x] != x:
        x = p[x]
    return x


# 두 요소의 집합을 하나로 합쳐주는 함수
# 각 요소의 대표중 하나의 부모를 다른 요소의 대표로 바꿔주기
def union(x, y):
    r1 = find_set(x)
    r2 = find_set(y)
    p[r1] = r2


def solve():
    for i in range(0, M * 2, 2):
        union(data[i], data[i + 1])
    # 모든 학생의 대표자를 확인해서 대표자가 몇명인지 확인
    r_set = set()
    for i in range(1, N + 1):
        r_set.add(find_set(i))
    return len(r_set)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # 0번 학생은 없으므로 사용하지 않음
    p = [x for x in range(N + 1)]
    result = solve()
    print(f'#{tc} {result}')