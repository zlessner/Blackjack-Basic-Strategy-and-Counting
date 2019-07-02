import random

# cards= [
#     {"2": 2},
#     {"3": 3},
#     {"4": 4},
#     {"5": 5},
#     {"6": 6},
#     {"7": 7},
#     {"8": 8},
#     {"9": 9},
#     {"10": 10},
#     {"J": 10},
#     {"Q": 10},
#     {"K": 10},
#     {"A": 1},
# ]

J=10
Q=10
K=10
A=1

cards= [2,3,4,5,6,7,8,9,10,J,Q,K,A]

smallCards = [2,3,4,5,6]

bigCards = [10,J,Q,K,A]

count =0

deck= cards*4

numDecks=8

stack= numDecks * deck

random.shuffle(stack)

player1=[]

dealer=[]

player1Total=0
dealerTotal=0

player1.extend((stack.pop(), stack.pop()))

dealer.append(stack.pop())


while sum(dealer)<17:
    if sum(player1)>=17:
        dealer.append(stack.pop())
    else:
        player1.append(stack.pop())
        
        










for x in player1:
    if x in smallCards:
        count +=1

    if x in bigCards:
        count -=1


for x in dealer:
    if x in smallCards:
        count +=1

    if x in bigCards:
        count -=1





print (player1)
print (dealer)
print (count)

