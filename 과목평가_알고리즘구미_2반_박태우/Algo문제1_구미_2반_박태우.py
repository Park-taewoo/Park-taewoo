T=int(input()) #테스트케이스 수 받아오기
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)] #NxN행렬을 받아오기
    cnt=0 #보너스 점수 변수 생성
    li=[] #보너스 점수들을 담을 리스트 생성
    for i in range(N): #NxN만큼 반복문 실행
        for j in range(N):
            cnt=0
            if i-1>=0:  #맞춘 과녁 기준 상
                cnt += arr[i-1][j] #보너스점수에 더하기
            if i+1<N: #맞춘 과녁 기준 하
                cnt += arr[i+1][j] #보너스점수에 더하기
            if j-1>=0: #맞춘 과녁 기준 좌
                cnt += arr[i][j-1] #보너스점수에 더하기
            if j+1<N: #맞춘 과녁 기준 우
                cnt += arr[i][j+1] #보너스점수에 더하기
            cnt = cnt-arr[i][j] #보너스 점수에서 맞힌칸 점수빼기
            if cnt<0: #만약 보너스 점수가 음수면 보너스 점수 0
                cnt = 0
            if cnt%2 == 0: #만약 보너스 점수가 짝수면 보너스점수 2배
                cnt=cnt*2
            if i==0 or i==N-1 or j==0 or j==N-1: #가장자리에 맞춘경우 보너스 점수는 0점
                cnt=0
            li.append(cnt) #보너스 점수를 리스트에 할당
    max_num=0 #보너스 점수에서 가장 큰값을 받을 변수생성
    for num in li: #보너스 점수 리스트중 가장 큰값을 반환하는 반복문
        if max_num < num:
            max_num = num
    print(f'#{tc} {max_num}')