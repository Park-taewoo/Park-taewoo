#10번을 실행하고 빌딩의 수와 빌딩의 높이를 받는 반복문
for i in range(10):
    N=int(input())
    buliding_lst=list(map(int,input().split()))
    
    result = 0
    for j in range(2,N-2):  #리스트상에서 2번쨰와 N-2의 두번째 객체의 양옆 두개의 빌딩의 리스트 목록만들기
        new_lst=[]
        new_lst.append(buliding_lst[j-2])
        new_lst.append(buliding_lst[j-1])
        new_lst.append(buliding_lst[j+1])
        new_lst.append(buliding_lst[j+2])
        
        new_lst_high=new_lst[0]  
        for k in new_lst:        #양옆 두개 총 4개의 빌딩 중 가장 높은 빌딩의 수 반환
            if k > new_lst_high:
                new_lst_high = k
    
        if buliding_lst[j] > new_lst_high:     #양옆 두개의 빌딩 총 4개중 가장 높은 빌딩의 높이가 현재 빌딩의 높이보다 낮으면 뺀 값을 추가 높다면 반복문진행
            result = result + (buliding_lst[j]-new_lst_high)
        else:
            continue
        
        
    print(f'#{i+1} {result}')
            