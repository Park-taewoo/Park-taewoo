def solve():
    #행에서 회문찾기 모든 행을 순회하기
    for i in range(N):
        for j in range(N-M+1): #회문의 시작점 순회
            #is_find =True
            for k in range(M//2):#data[i][j]에서 시작하는 길이 M인 회문이 있는지 검사
                if data[i][j+k] != data[i][j+M-1-k] :#회문이 아니면 바로 다음꺼찾기
                   # is_find = False
                    break
            else: #반복문 도문 동안 break가 실행 안되면 실행
                # print('회문찾음')
                return data[i][j:j+M]
            #if is_find: #True이면 회문
                #print('회문찾음')
                #print(data[i][j:j + M])
#열에서 회문찾기 모든 열을 순회하기
    for i in range(N):
        for j in range(N-M+1): #회문의 시작점 순회
            #is_find =True
            for k in range(M//2):#data[i][j]에서 시작하는 길이 M인 회문이 있는지 검사
                if data[j+k][i] != data[j+M-1-k][i] :#회문이 아니면 바로 다음꺼찾기
                    break
            else: #반복문 도문 동안 break가 실행 안되면 실행
                #print('회문찾음')
                result = ''
                for a in range(j,j+M):
                    result +=data[a][i]
                return result


T = int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    data=[input() for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')
