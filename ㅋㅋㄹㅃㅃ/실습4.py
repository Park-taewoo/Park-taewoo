pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def creata_data(subject,day,title='None'):
    global pro_num
    global global_data
    data = {}
    data['과목']=subject
    data['일차']=day
    data['제목']=title
    data['문제번호']=pro_num
    pro_num+=1
    return data

result_1=creata_data('python',3)
print(result_1)
result_2=creata_data('web','1','web 연습하기')
print(result_2)
result_3=creata_data(**global_data)
print(result_3)
