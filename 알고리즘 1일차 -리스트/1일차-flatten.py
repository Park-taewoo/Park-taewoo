for T in range(1, 11):  # 10번시행
    N = int(input())  # 덤프 횟수
    box_list = list(map(int, input().split()))  # 박스 높이 
 
    for _ in range(N): #덤프 횟수 반복문
        max_v, box_max_idx = box_list[0], 0  # 최댓값 설정  # 최솟값 설정
        min_v, box_min_idx = box_list[0], 0  
        for i in range(100):   #가로길이가 항상 100으로 주어진다.
            if max_v < box_list[i]:   #덤프를 한번했을때 가장 높은 박스와 가장 낮은 박스를 구함
                max_v = box_list[i]
                box_max_idx = i
            if min_v > box_list[i]:
                min_v = box_list[i]
                box_min_idx = i
        box_list[box_max_idx] -= 1  #가장 높은 박스에 -1을 하여 가장 낮은 박스에게 1을 주는 덤프실행
        box_list[box_min_idx] += 1
        max_box = box_list[0]        
        min_box = box_list[0]
    for j in box_list:        #최고 높이와 최소높이를 구하기
        if j > max_box:
            max_box = j
        elif j < min_box:
            min_box = j    
    print(f'#{T} {max_box - min_box}')