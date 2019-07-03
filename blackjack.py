import random

J=10
Q=10
K=10
A=1

cards= [2,3,4,5,6,7,8,9,10,J,Q,K,A]

smallCards = [2,3,4,5,6]

bigCards = [10,J,Q,K,A]

count =0

bankRoll=500

deck= cards*4

numDecks=8

stack= numDecks * deck

random.shuffle(stack)

while True:

    play = str(input("Would you like to play the blackjack hand? y/n "))

    if play == 'y' or play == 'Y':
        
        bet=5

        if count/numDecks>=1:
            bet= bet*2
        elif count/numDecks>=2:
            bet= bet*3
        elif count/numDecks>=3:
            bet= bet*4
        else:
            bet=bet


        player1=[]

        dealer=[]

        player1Split1=[]

        player1.extend((stack.pop(), stack.pop()))

        dealer.append(stack.pop())



        if A in player1 or A in dealer:
            print ("Ace")
            continue


        else:
            def basicStrag():
                global bet
                while sum(dealer)<17:
                    if (player1[0]==2 and player1[1]==2) and (sum(dealer)>=7):
                        player1Split1.append(player1.pop())
                        player1.append(stack.pop())
        
                    elif sum(player1)>=17:
                        while sum(dealer)<17:
                            dealer.append(stack.pop())
                    elif (sum(player1)==16 or sum(player1)==15 or sum(player1)==14 or sum(player1)==13) and (sum(dealer)==2 or sum(dealer)==3 or sum(dealer)==4 or sum(dealer)==5 or sum(dealer)==6):
                        while sum(dealer)<17:
                            dealer.append(stack.pop())
                    elif (sum(player1)==16 or sum(player1)==15 or sum(player1)==14 or sum(player1)==13) and (sum(dealer)==7 or sum(dealer)==8 or sum(dealer)==9 or sum(dealer)==10):
                        player1.append(stack.pop())
                    elif (sum(player1)==12) and (sum(dealer)==4 or sum(dealer)==5 or sum(dealer)==6):
                        while sum(dealer)<17:
                            dealer.append(stack.pop())
                    elif (sum(player1)==12) and (sum(dealer)==2 or sum(dealer)==3 or sum(dealer)==7 or sum(dealer)==8 or sum(dealer)==9 or sum(dealer)==10):
                        player1.append(stack.pop())
                    elif (sum(player1)==11 and len(player1)==2):
                        bet=bet*2
                        player1.append(stack.pop())
                        while sum(dealer)<17:
                            dealer.append(stack.pop())
                    elif (sum(player1)==10 and len(player1)==2) and (sum(dealer)!=10):
                        bet=bet*2
                        player1.append(stack.pop())
                        while sum(dealer)<17:
                            dealer.append(stack.pop())
                    elif (sum(player1)==10) and (sum(dealer)==10):
                        player1.append(stack.pop())
                    elif (sum(player1)==9 and len(player1)==2) and (sum(dealer)==3 or sum(dealer)==4 or sum(dealer)==5 or sum(dealer)==6):
                        bet=bet*2
                        player1.append(stack.pop())
                        while sum(dealer)<17:
                            dealer.append(stack.pop())
                    elif (sum(player1)==9) and (sum(dealer)!=3 or sum(dealer)!=4 or sum(dealer)!=5 or sum(dealer)!=6):
                        player1.append(stack.pop())
                    elif (sum(player1)==5 or sum(player1)==6 or sum(player1)==7 or sum(player1)==8):
                        player1.append(stack.pop())

                    else:
                        break

                    
            basicStrag()

                





            if sum(player1)>21:
                bankRoll=bankRoll-bet
            elif sum(dealer)>21:
                bankRoll=bankRoll+bet
            elif sum(player1)<sum(dealer):
                bankRoll=bankRoll-bet
            elif sum(player1)==sum(dealer):
                bankRoll=bankRoll
            else: 
                bankRoll=bankRoll+bet

            

            
                
                










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



        if len(stack)<=208:
            stack= numDecks * deck
            random.shuffle(stack)
            count=0


        print (player1)
        print (sum(player1))
        print (dealer)
        print (sum(dealer))
        print (count)
        print (bankRoll)


        if (len(player1Split1)>=1):
                player1=[]
                player1.append(player1Split1)
                basicStrag()

    
    elif play == "N" or play =="n":
        break
    
    else:
        print("Please enter y/n")

