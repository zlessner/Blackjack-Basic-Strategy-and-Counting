import random

J=10
Q=10
K=10
A=1

cards= [2,3,4,5,6,7,8,9,10,J,Q,K,A]

smallCards = [2,3,4,5,6]

bigCards = [10,J,Q,K,A]

count =0

minBet=5

bankRoll=500

deck= cards*4

numDecks=8

stack= numDecks * deck

random.shuffle(stack)

while True:

    play = str(input("Would you like to play the blackjack hand? y/n "))

    if play == 'y' or play == 'Y':

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

        if sum(player1)>21:
            bankRoll=bankRoll-minBet
        elif sum(dealer)>21:
            bankRoll=bankRoll+minBet
        elif sum(player1)<sum(dealer):
            bankRoll=bankRoll-minBet
        elif sum(player1)==sum(dealer):
            bankRoll=bankRoll
        else: 
            bankRoll=bankRoll+minBet
                
                










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
        print (sum(player1))
        print (dealer)
        print (sum(dealer))
        print (count)
        print (bankRoll)

    
    elif play == "N" or play =="n":
        break
    
    else:
        print("Please enter y/n")

