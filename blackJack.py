import random
import time

cards = [
    'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
    'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
    'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
    'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK',
]

playerCard = []
dealerCard = []

playerScore = 0
dealerScore = 0

playerWon = False

def yieldScore(cardList):
    cardList = goBackA(cardList)
    score = 0
    for i in cardList:
        if i[1] == 'A':
            if not score + 11 > 21:
                score += 11
            else:
                score += 1
        elif i[1] in ['J', 'Q', 'K']:
            score += 10
        else:
            score += int(i[1:])
    return score


def goBackA(cardList):
    sortedCardList = []
    cardsWithA = []
    for i in cardList:
        card = i
        if 'A' in card:
            cardList.remove(card)
            cardList.append(card)
    return cardList


if __name__ == '__main__':
    random.shuffle(cards)
    
    for i in range(2):
        playerCard.append(cards.pop())
        dealerCard.append(cards.pop())

    playerScore = yieldScore(playerCard)
    print('플레이어 카드: {}, 점수: {}점'.format(playerCard, playerScore))

    dealerScore = yieldScore(dealerCard)
    print('딜러 카드: {}, 점수: {}점'.format(dealerCard, dealerScore))

    if playerScore == 21 and dealerScore == 21:
        print('동점!!! 딜러의 승리 입니다!')
    elif playerScore == 21:
        print('블랙잭!!! 플레이어의 승리 입니다!')
    elif dealerScore == 21:
        print('블랙잭!!! 딜러의 승리 입니다!')
    

    while True:
        ans = input('\n카드를 더 받으시겠습니까?(y/n) ')
        if ans in ['y', 'Y']:
            playerCard.append(cards.pop())
            playerScore = yieldScore(playerCard)
            print('플레이어 카드: {}, 점수: {}점'.format(playerCard, playerScore))
            if playerScore == 21:
                print('블랙잭!!!')
                playerWon = True
                break
            elif playerScore > 21:
                break
        elif ans in ['n', 'N']:
            break

    if not playerWon:
        print('딜러 차례 입니다.')
        while True:
            pass
        
        
