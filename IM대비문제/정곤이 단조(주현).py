#D3 6190 정곤이의 단조 증가하는 수
 
#계산된 값이 단조증가인지 확인한다.
def check(number):
    temp_str = str(number) #입력받은 숫자를 '임시 문자열로 변환할거임.
    for k in range(len(temp_str)-1): # 숫자가 단조증가하는지 체크하는 로직!
        if temp_str[k] > temp_str[k+1]: # k번째 숫자 붙잡으면, k+1번째 숫자를 체크해서 서로 비교하는 느낌...
            return False    #만약 단조증가가 아니라면 False를 반환하고!! check 함수를 종료한다.(중요! 왜냐하면 return이 있으므로!)
    return True #if에 해당하지 않는다면,True를 반환...
 
T = int(input())
for tc in range(1, T+1):
    N = input()
    a_list = list(map(int, input().split()))
    mx = -1 # a_list[i]*a_list[j] 곱했는데, 단조 증가하는 수가 없다면, -1을 출력해야해서..
    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)): # i번째 숫자 * 그 이후의 넘버링의 숫자를 곱하기 위해서!
            num = a_list[i]*a_list[j]
            #두수를 곱한값이 결과값보다 커야하고, 곱한값은 단조증가수여야 한다.
            if mx < num and check(num): # mx를 계속 갱신시키기 위해서!! 동시에 단조증가 함수에서 True를 받아야함!!
                mx = num
    print(f'#{tc} {mx}')

# result가 -1로 나오는 경우를 살펴보자!
# 큰 수들만 포함된 경우, 곱이 항상 단조 증가하지 않을 수 있음
# 예를 들어, 리스트가 [32, 76, 91]이라고 해봅시다. 가능한 곱은 2432(32*76), 2912(32*91), 6916(76*91) 등입니다. 
# 이 경우에도 모든 곱이 단조 증가하는 수가 아니므로, 결과는 -1입니다.
