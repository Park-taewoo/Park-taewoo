# cnt : 카드를 바꾼 횟수

cards = [1, 2, 3, 4, 5]


# 카드 바꾸는 함수
def solve(cnt):
    global max_money
    if cnt == M:
        money = cards_to_number(cards)
        if max_money < money:
            max_money = money
        return
    # 단 동일한 교홚을 해볼 필요는 없다
    # 교환 횟수와 모양이 같은 경우를 수행했었다면, 교환을 진행하지 않음


    # 카드 바꾸기(맨마지막 카드는 바꿀 수 없음)
    for i in range(N - 1):
        # i번 카드와 바꿀 카드번호 j
        for j in range(i + 1, N):
            cards[i], cards[j] = cards[j], cards[i]
            # 교환 횟수 증가 시켜서 다음 교환 하기
            solve(cnt + 1)
            cards[i], cards[j] = cards[j], cards[i]


# 카드를 숫자로 만들기 함수
def cards_to_number(cards):
    result = 0
    for num in cards:
        result = result * 10 + num

    return result


T = int(input())
for tc in range(1, T + 1):
    # 숫자 카드 정보, 교환횟수
    cards, M = input().split()
    # cards의 경우 숫자형태의 리스트 ( 사실은 문자열이 편함)
    cards = list(map(int, cards))
    # N : 카드의 개수 , M : 교환 횟수
    N = len(cards)
    M = int(M)
    max_money = 0
    solve(0)
    print(f'#{tc} {max_money}')