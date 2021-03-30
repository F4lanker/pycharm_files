cards_dict = {'6': '6', '7': '7', '8': '8', '9': '9', '10': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
step = (input().split())
trump = str(input())
f_card = int(cards_dict[step[0][0]])
f_suit = step[0][1]
s_card = int(cards_dict[step[1][0]])
s_suit = step[1][1]


def gradest_card(f_card, s_card):
    if f_card>s_card:
        return print(f_card)
    elif s_card>f_card:
        return print(s_card)
    else:
        print('Error')

if f_suit == s_suit:
    gradest_card(f_card, s_card)
if f_suit or s_suit == trump:
    if f_suit == trump and s_suit != trump:
        print('First')
    elif s_suit == trump and f_suit != trump:
        print('Second')
    else:
        gradest_card(f_card, s_card)


