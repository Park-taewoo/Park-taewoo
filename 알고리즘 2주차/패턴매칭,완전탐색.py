#패턴이 있으면 1 없으면 0반환
def brute_force():
    for i in range(N-M+1):
        for j in range(M):
            if target[i+j] != pattern[j]:# i번에서 시작하는 길이 M 문자열은 패턴이 아님
                break
        else: #패턴 찾음
            return 1
    #반복문 다 도는 동안 패턴을 못찾았으면 리턴 0
    return 0
target='ABCDEFABCFEG'
N = len(target)
pattern = 'EFAB'
M = len(pattern)
print(brute_force())