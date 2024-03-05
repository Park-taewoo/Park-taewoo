arr=['A','B','C']
N=len(arr)
#각 요소의 부분집합 포함여부 표시배열
selectde = [0]*N
# idx 번째 요소를 부분집합에 포함하거나,포함하지 않거나
def ps(idx):
    if idx == N:
        print(selectde)
        return
    for i in range(2):
        selectde[idx] = i
        ps(idx+1)
ps(0)