#정렬 알고리즘: 거품 정렬, 선택 정렬 >>> 효율낮음
arr = [3,5,7,9,4,6,1,2]

#두개씩 비교하는걸 끝까지 N-1번
N= len(arr)
for i in range(N-1):
    #두개씩 비교 하기
    for j in range(0,N-1): #for j in range(0,N-1-i): 을 하면 정리됐던 뒤에껀 정리안하는 반복문
        #j번이랑 j+1번이랑 비교
        if arr[j] > arr[j+1]:
            # tmp = arr[j]
            # arr[j] = arr[j+1]
            # arr[j+1] = tmp
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
#1. 요소 출현 횟수세기
#2. 누적합 구하기 (위치 계산하기
#3. 각 위치에 맞게 넣어주기
#1번
arr = [4,4,1,3,2,7,8,1,4,5,6,9,10]
print(arr)
K=10
N=len(arr)
print(N)
#횟수를 세기 위한 배열
count = [0]*(K+1)
for i in range(N):
    #arr[i]
    count[arr[i]]+=1
print(count)

#2번 누적합 구하기 (위치 계싼하기)
for i in range(1,K+1):
    #count[i] = count[i-1]+ count[i]
    count[i] += count[i-1]
print(count)
#3번 각 위치에 맞게 넣어주기
sorted_arr = [None] * N
for i in range(N):
    print([arr[i]])
    #arr[i] 가 어디에 들어가는지 확인하고 넣어주기
    count[arr[i]] -= 1
    sorted_arr[count[arr[i]]] = arr[i]
print(sorted_arr)
