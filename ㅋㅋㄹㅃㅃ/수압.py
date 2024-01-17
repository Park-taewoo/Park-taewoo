#람다 사용예시
a = [(1,3),(5,1),(2,4),(6,5),(3,6)]
#요소를 받아서 뒷값 반환
# def sort_key(x):
#     return x[1]
    
# a.sort(key=sort_key)
a.sort(key=lambda x:x[1])
print(a)
