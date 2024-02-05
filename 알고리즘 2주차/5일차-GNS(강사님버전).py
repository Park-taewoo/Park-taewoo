# 정렬 : 두 요소 간의 크기 비교가 가능해야 합니다.
# GNS : 'ZRO', 'SVN' 'ONE', 'TWO' 등과 같은 문자열로 되어 있으니...
#  크기 비교가 불가능하니 크기 비교를 할 수 있도록 하는 무언가가 필요
# 딕셔너리 key-value를 활용
num_dic = {
'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3,
'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9
}
arr = ['SVN', 'THR', 'TWO', 'FIV', 'NIN', 'ONE', 'SIX', 'FIV', 'FIV']

def counting_sort(arr):
    count = [0]*10  #각 요소가 몇 개씩 나왔는지 세는 배열
    N = len(arr)
    sorted_arr = [None] * N # 요소가 정렬되어 들어갈 배열
    #각 요소가 몇 개씩 나왔는지 세기...
    for i in range(N):
        # arr[i] : 문자열  ex) ZRO SVN
        # num_dic[arr[i]]  ex) 0  7
        count[num_dic[arr[i]]] += 1
    #누적합 구해서 자리 구하기
    for i in range(1,10):
        count[i] = count[i-1] + count[i]
    #위치대로 넣어주기
    for i in range(N):
        # arr[i]를 sorted_arr에 복사
        # 위치는 count가 가지고 있는데 인덱스가 필요해서
        # num_dic[arr[i]]
        count[num_dic[arr[i]]] -= 1
        sorted_arr[count[num_dic[arr[i]]]] = arr[i]
    return sorted_arr


result = counting_sort(arr)

print(result)
