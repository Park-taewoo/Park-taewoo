#숫자>문자열 바꾸기 123>>'123'
#문자>숫자 바꾸기 '123'>>123

#우리가 하려는거 숫자 123>>문자 '123'
#한 자리씩밖에 못바꾸니까...
#123에서 한자리씩 떼서 1,2,3을 각각 바꾸자
#숫자 123에 숫자 1어떻게 뗄 수 있나요
# 100으로 나누면 몫 = 1,나머지 = 23
# 10으로 나누면 몫: 12 나머지 :3
# 12 를 10으로 나누면 몫:1 , 나머지 :2
# 1을 10으로 나누면 몫 :0 나머지:1
def itoa(num): #숫자를 문자열로 바꾸어 반환하는 함수
    result= '' #최종 문자열이 저장될 변수
    #10씩 계속 나누어서 나머지를 문자열로 변경
    #몫이 0이 될때 까지
    while num>0:
        # if num == 0:
        #     break
        remain = num % 10
        result=chr(ord('0') + remain) +result
        num = num // 10


    return result
print(chr(48)) # 아스키코드 아스키코드48:0이므로 문자열 0 나옴
print(chr(ord('0')+1)) #ord는 해당하는 아스키코드를 들고와줌
print(itoa(123124)) #str

#문자열 숫자로 바꾸기
# print(type((ord('3') - ord('0'))))
def atoi(arg):
    #한 자리씩 바꿔서 다음자리 바꿀 때 곱하기 10해서 더해주면 됩니다..
    result = 0
    for num in arg:
        result *= 10 #기존값 곱하기 10
        result += ord(num) - ord('0') #방금 구한 숫자 더해주기
    return result

print(atoi('123')-atoi('1'))
