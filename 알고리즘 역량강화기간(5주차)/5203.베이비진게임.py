#원래는...탐욕으로 하는게...이득인데
#카드를 받을 때 마다 순열 만들어서 앞쪽 세장만 가지고
#run인지 triplet인지 확인
#내가 가진 카드를 이용해서 순열만들기
#순열 만들어보고 앞에 3장이 run or triplet이라면 1,아니면 0반환
def perm(idx,cards):
    if len(cards)<3:
        return 0
    #idx번쨰 카드와 i번째 카드 자리 바꾸기
    if idx == len(cards):
        if cards[0] ==cards[1] ==cards[2]:
            return 1
        elif cards[0]+1 ==cards[1] and cards[0]+2 ==cards[2]:
            return 1
        else:
            return 0


    for i in range(idx,len(cards)):
        cards[idx],cards[i] = cards[i],cards[idx]
        #다음 카드 자리바꾸기 수행
        reuslt = perm(idx+1,cards)
        if reuslt ==1:
            return 1
        #바꾼 카드 원래대로 만들어놓기
        cards[idx], cards[i] = cards[i], cards[idx]
    return 0

T = int(input())
for tc in range(1,T+1):
    data=list(map(int,input().split()))
    cards_a = [] #플레이어 1
    cards_b = [] #플레이어 2
    winner= 0
    for i in range(12):
        if data[i]%2: #홀수번
            cards_b.append(data[i])
            if perm(0,cards_b):
                winner = 2
                break

        else: #짝수번
            cards_a.append(data[i])
            if perm(0,cards_a):
                winner = 1
                break
    print(f'#{tc} {winner}')