for test_case in range(1,11):
    N = int(input())
    buildings = list(map(int,input().split()))
    result = 0
 
    for i in range(2,N-2):
        # 양쪽 2칸에 세워진 건물의 높이 리스트에 넣고
        lst = []
        lst.append(buildings[i - 1]) #1  2 3
        lst.append(buildings[i - 2]) #0  1 2
        lst.append(buildings[i + 1]) #3  4 5 
        lst.append(buildings[i + 2]) #4  5 6
 
        # 그 중  가장 큰 건물 구하기
        max_b = lst[0]
        for j in lst:
            if j > max_b:
                max_b = j
 
        # 만약 가장 큰 건물보다 현재 건물의 높이가 높다면
        # 현재 건물의 높이에서 가장 큰 건물을 뺸 값을 result값에 더하기
        # 안 높으면 그냥 넘어가기
        if buildings[i] > max_b:
            result = result + (buildings[i] - max_b)
        else :
            continue
 

    print(f'#{test_case} {result}')