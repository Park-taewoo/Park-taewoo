T = int(input())
for tc in range(1,T+1):
    input_nums = input()
    input_strs = list(input().split())
    my_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    new_list = []
    for i in my_list:
        for j in range(len(input_strs)):
            if i == input_strs[j]:
                new_list.append(input_strs[j])

    print(f'#{tc}')
    print(*new_list)

