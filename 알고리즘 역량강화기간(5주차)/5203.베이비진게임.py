# 원래는...탐욕으로 하는게...이득인듯한데..
# 카드를 받을 때 마다 순열 만들어서 앞쪽 세장만 가지고
# run인지 triplet인지 확인
#내가 가진 카드를 이용해서 순열만들기
#현재 카드보다 뒤에 있는 카드들과 자리바꾸기를 모두 해보기
#순열 만들어보고 앞에 3장이 run or triplet 이라면 1, 아니면 0반환
def perm(idx,cards):
    if len(cards) < 3:
        return 0
    if idx == len(cards):
        # print(cards)
        if cards[0] == cards[1] == cards[2]:
            return 1
        elif (cards[0] + 1 == cards[1]) and (cards[0] + 2 == cards[2]):
            return 1
        else:
            return 0

    # idx번째 카드와 i번째 카드 자리 바꾸기
    for i in range(idx,len(cards)):
        cards[idx], cards[i] = cards[i], cards[idx]
        #다음 카드 자리바꾸기 수행
        result = perm(idx+1,cards)
        if result == 1:
            return 1
        # 바꾼 카드 원래대로 만들어 놓기
        cards[idx], cards[i] = cards[i], cards[idx]
    return 0

T = int(input())
for tc in range(1,T+1):
    data = list(map(int,input().split()))
    cards_a = []    #플레이어1
    cards_b = []    #플레이어2
    winner = 0
    for i in range(12):
        if i % 2:
            cards_b.append(data[i])
            if perm(0,cards_b):
                winner = 2
                break
        else:
            cards_a.append(data[i])
            if perm(0, cards_a):
                winner = 1
                break
    print(f'#{tc} {winner}')




# 5 3 5 3 5 3 2 0 9 2 0 0
