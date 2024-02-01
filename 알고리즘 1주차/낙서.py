Test_case=int(input())

for i in range(1,Test_case+1):
    N,M=map(int,input().split())
    N_list=list(map(int,input().split()))
    New_list=[]
    for j in range(N-M+1): #N-M+1 범위만큼
        result=0
        for k in range(j,j+M): #연속적인 수 즉 j부터 j+M까지 더하는 result값에 더한다.
            result+=N_list[k]
        New_list.append(result)
    print("#%d %d"%(i,max(New_list)-min(New_list)))   #구간의 최대합과 최소값을 뺀다.

