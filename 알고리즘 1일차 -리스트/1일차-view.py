list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_lit = []
for i in range(10):
    N = int(input())
    hi = list(map(int, input().split()))
 
    count = 0
    for j in range(N):
 
        if 1 < j < (N-2):
            my_list = [hi[j-2], hi[j-1], hi[j+1], hi[j+2]]
            
            my_max = my_list[0]
            for k in my_list:
                if my_max <= k:
                    my_max = k
 
            if hi[j] > my_max:
                count = count + (hi[j] - my_max)
    output_lit.append(count)
for f in range(len(list_1)):
    print(f'#{list_1[f]} {output_lit[f]}')