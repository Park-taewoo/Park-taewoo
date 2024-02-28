T = int(input())

for t_c in range(1, T + 1):
    N = int(input())
    truck = [list(map(int, input().split())) for _ in range(N)]
    truck.sort(key=lambda x: x[1])
    print(truck)