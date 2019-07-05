import random

from inspect import currentframe

cf = currentframe()

#display card names
#figure out ace thing
#figure out split thing
#finish up basic strategy
#catch fixes in logic (such as possibly when to double down with a 9)
#simulate many times to see if make any money over time
#sudo code and readme

# cards= [2,3,4,5,6,7,8,9,10,J,Q,K,A]


cards= [{"2":2}, {"3":3}, {"4":4}, {"5":5}, {"6":6}, {"7":7}, {"8":8}, {"9":9}, {"10":10}, {"J":10}, {"Q":10}, {"K":10}, {"A":11}]

for key in cards:
    global face
    face = list(key.keys())
    print (face[0])



# print (cards[0].items())

# show= list(cards[0].keys())

# print (sum(cards[0].values()))

# print (show[0])


smallCards = [list(cards[0].keys()),list(cards[1].keys()),list(cards[2].keys()),list(cards[3].keys()),list(cards[4].keys())]

bigCards = [list(cards[8].keys()),list(cards[9].keys()),list(cards[10].keys()),list(cards[11].keys()),list(cards[12].keys())]



count =0

bankRoll=500

deck= cards*4

numDecks=8

stack= numDecks * deck

random.shuffle(stack)


# while True:
for i in range(500):

#     play = str(input("Would you like to play the blackjack hand? y/n "))

#     if play == 'y' or play == 'Y':

        bet=5

        if count/numDecks>=3:
            bet= bet*4
        elif count/numDecks>=2:
            bet= bet*3
        elif count/numDecks>=1:
            bet= bet*2
        else:
            bet=bet


        player1=[]

        dealer=[]

        player1Split1=[]

        playerTotal=0
        dealerTotal=0

        player1.extend((stack.pop(), stack.pop()))

        dealer.append(stack.pop())

            

        
        def basicStrag():
            global bet
            global playerTotal
            global dealerTotal


            print(dealer, "line ", cf.f_lineno)
            print(player1, "line ", cf.f_lineno)
            
            while dealerTotal<17:
                    if (sum(player1[0].values())==2 and sum(player1[1].values())==2) and (sum(dealer[0].values())<=7):
                        # player1Split1=[]
                        player1Split1.append(player1.pop())
                        player1.append(stack.pop())
                        # print ("split")
                        # print(player1)
                        # print(player1Split1)
                    elif (sum(player1[0].values())==3 and sum(player1[1].values())==3) and (sum(dealer[0].values())<=7):
                        # player1Split1=[]
                        player1Split1.append(player1.pop())
                        player1.append(stack.pop())
                        #print ("split")
                    elif (sum(player1[0].values())==4 and sum(player1[1].values())==4) and (sum(dealer[0].values())==5 or sum(dealer[0].values())==6):
                        # player1Split1=[]
                        player1Split1.append(player1.pop())
                        player1.append(stack.pop())
                        #print ("split")
                    elif (sum(player1[0].values())==6 and sum(player1[1].values())==6) and (sum(dealer[0].values())<=6):
                        # player1Split1=[]
                        player1Split1.append(player1.pop())
                        player1.append(stack.pop())
                        #print ("split")
                    elif (sum(player1[0].values())==7 and sum(player1[1].values())==7) and (sum(dealer[0].values())<=7):
                        # player1Split1=[]
                        player1Split1.append(player1.pop())
                        player1.append(stack.pop())
                        #print ("split")
                    elif (sum(player1[0].values())==8 and sum(player1[1].values())==8):
                        # player1Split1=[]
                        player1Split1.append(player1.pop())
                        player1.append(stack.pop())
                        #print ("split")
                    elif (sum(player1[0].values())==9 and sum(player1[1].values())==9) and (sum(dealer[0].values())<=6 or sum(dealer[0].values())==8 or sum(dealer[0].values())==9):
                        # player1Split1=[]
                        player1Split1.append(player1.pop())
                        player1.append(stack.pop())
                        #print ("split")
        
                    elif playerTotal>=17:
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                    elif (playerTotal==16 or playerTotal==15 or playerTotal==14 or playerTotal==13) and (dealerTotal==2 or dealerTotal==3 or dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                    elif (playerTotal==16 or playerTotal==15 or playerTotal==14 or playerTotal==13) and (dealerTotal==7 or dealerTotal==8 or dealerTotal==9 or dealerTotal==10):
                        player1.append(stack.pop())
                    elif (playerTotal==12) and (dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                    elif (playerTotal==12) and (dealerTotal==2 or dealerTotal==3 or dealerTotal==7 or dealerTotal==8 or dealerTotal==9 or dealerTotal==10):
                        player1.append(stack.pop())
                    elif (playerTotal==11 and len(player1)==2):
                        bet=bet*2
                        player1.append(stack.pop())
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                    elif (playerTotal==10 and len(player1)==2) and (dealerTotal!=10):
                        bet=bet*2
                        player1.append(stack.pop())
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                    elif (playerTotal==10) and (dealerTotal==10):
                        player1.append(stack.pop())
                    elif (playerTotal==9 and len(player1)==2) and (dealerTotal==3 or dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                        bet=bet*2
                        player1.append(stack.pop())
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                    elif (playerTotal==9) and (sum(dealer)!=3 or dealerTotal!=4 or dealerTotal!=5 or dealerTotal!=6):
                        player1.append(stack.pop())
                    elif (playerTotal)<=11:
                        player1.append(stack.pop())

                    else:
                        break

                    
            for x in player1:
                playerTotal= playerTotal + sum(list(x.values()))
            for y in dealer:
                dealerTotal= dealerTotal + sum(list(y.values()))


              
        basicStrag()




        if (playerTotal==21 and playerTotal!=21 and len(player1)==2):
            bankRoll=bankRoll+(bet*1.5)
        elif playerTotal>21:
            bankRoll=bankRoll-bet
        elif dealerTotal>21:
            bankRoll=bankRoll+bet
        elif playerTotal<dealerTotal:
            bankRoll=bankRoll-bet
        elif playerTotal==dealerTotal:
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

        # print (A)
        # J="J"
        # Q="Q"
        # K="K"
        # A="A"

        # for i in player1:
        #     print (i, "line ", cf.f_lineno)
        #     print (random.randint(1,100), "line ", cf.f_lineno)
        #     if i==10:
        #         # if (random.randint(1,100)) < 25:
        #         i="J"
        #         print(player1, "line ", cf.f_lineno)


        print (player1)
        print (playerTotal)
        print (dealer)
        print (dealerTotal)
        print (count)
        print (bankRoll)  
        print ("break")      



        if (len(player1Split1)>=1):
            print("split")
            player1=[]
            dealer=[dealer[0]]
            player1.append(player1Split1.pop())
            player1.append(stack.pop())
            print(player1, "line ", cf.f_lineno)
            print(dealer, "line ", cf.f_lineno)
            player1Split1=[]
            basicStrag()


        if len(stack)<=208:
            stack= numDecks * deck
            random.shuffle(stack)
            count=0
            print("Entire deck has been shuffled")

    
    # elif play == "N" or play =="n":
    #     break
    
    # else:
    #     print("Please enter y/n")

