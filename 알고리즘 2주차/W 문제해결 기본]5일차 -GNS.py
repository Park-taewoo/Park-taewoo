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

#보충수업 강사님 버전
num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
num_dict = { num_str[i]:i for i in range(10)}

T = int(input())
for tc in range(1, T + 1):
    tmp = input()
    arr = input().split()

    # arr에서 문자열을 하나씩 가져와서 num_dict를 사용해서 0~9 값으로 변환
    cnt = [0] * (9 + 1)
    for key in arr:
        num = num_dict[key]
        cnt[num] += 1

    ans = f'#{tc} '
    for i in range(10):
        ans = ans + (f'{num_str[i]} ' * cnt[i])

    print(ans)