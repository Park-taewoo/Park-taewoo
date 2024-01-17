def rental_book(a,b):
    decrease_book(b)
    name=a
    print(f'{name}님이 {b}권의 책을 대여하였습니다.')
    pass

number_of_book = 100

def decrease_book(A):
    global number_of_book
    book_borrow=number_of_book-A
    print(book_borrow)
    pass
rental_book('홍길동',3)