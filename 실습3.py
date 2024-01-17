number_of_people = 0
user_info={}


def increase_user():
    global number_of_people
    number_of_people += 1
    pass


def create_user():
    global user_info
    user_name = str(input('성함이 어떻게 되시나요? : '))
    user_age = int(input('연세가 어떻게 되시나요? : '))
    user_adress = str(input('거주기가 어디시나요? : '))
    user_info={'name':{user_name}, 'age':{user_age},'address':{user_adress}}   
    print(f'현재 가입 된 유저 수 : {number_of_people}')
    increase_user()
    print(f'{user_name}님 환영합니다!')
    print(user_info)
    print(f'현재 가입 된 유저 수 : {number_of_people}')
    pass



create_user()