T=int(input())
for tc in range(1,T+1):
    nums=list(map(int,input().strip()))
    
    cnt=[0]*10
    for num in nums:
        cnt[num]+=1
    triplet_cnt=0
    run_cnt=0    
    print(cnt)
    for i in range(10):
        #트리플릿 검사
        while cnt[i] >=3:
            triplet_cnt +=1
            print('s')
            cnt[i]-=3
            print(triplet_cnt)
    #런 검사
        while i <=7 and cnt[i] > 0 and cnt[i+1] >0 and cnt[i+2]>0: #1~9값이니 8부터는 연속 3자리가 안됨
            run_cnt+=1
            print(run_cnt)
            print('d')
            cnt[i]-=1
            cnt[i+1]-=1
            cnt[i+2]-=1
    #베이비진 판단
    if triplet_cnt+run_cnt ==2 :
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')        
            