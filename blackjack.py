import random

from inspect import currentframe

from cards import (cards, smallCards, bigCards)

from rules import (count, bankRoll, deck, numDecks, stack) 

cf = currentframe()

random.shuffle(stack)


#sudo code and readme
# soft 17 rule



# while True:
for i in range(10000):

    # play = str(input("Would you like to play the blackjack hand? y/n "))

    # if play == 'y' or play == 'Y':

        if bankRoll<=0:
            break

        if bankRoll>=5:
            bet=5
        else:
            print ("Bet is remainder of bankroll")
            bet=bankRoll

        if count/numDecks>=3:
            bet= bet*4
            print ("Bet quadrupled due to true count")
        elif count/numDecks>=2:
            bet= bet*3
            print ("Bet trippled due to true count")
        elif count/numDecks>=1:
            bet= bet*2
            print ("Bet doubled due to true count")
        else:
            bet=bet



        player1=[]

        dealer=[]

        player1Split1=[]

        playerTotal=0
        dealerTotal=0
        otherTotal=0

        player1.extend((stack.pop(), stack.pop()))

        dealer.append(stack.pop())

        game=True
        dealerGame=True
        woof=True
        meow=True
        roar=True
        goodbye=True
        howdy=True
        yo=True
        more=True
        evenMore=True
        open=False
        close=False
        open2=False
        close2=False
        close3=False
        open3=False
        aceList=[]
        aceList2=[]
        playerList=[]

        

        for x in player1:
            playerTotal= playerTotal + sum(list(x.values())) 
        # print("shalom")
        # print(playerTotal)

        for y in dealer:
            dealerTotal= dealerTotal + sum(list(y.values()))

        for z in range(len(player1)):
                ace=list(player1[z].keys())
                if (ace[0]=="A"):
                    for worth in list(player1[z]):
                        player1[z][worth] = 11


        
        def basicStrag():
            global bet
            global playerTotal
            global dealerTotal
            global over
            global game
            global dealerGame
            global woof
            global meow
            global roar
            global goodbye
            global howdy
            global yo
            global open
            global close
            global open2
            global close2
            global playerList
            global otherTotal
            global more
            global close3
            global evenMore
            global open3

            
            while dealerTotal<17:

                playerList=[]
                for x in player1:
                    for number in x:
                        playerList.append(number)

                for h in player1:
                    if playerList.count('A')>=1:
                        otherTotal=playerTotal-11    
                    else:
                        otherTotal=otherTotal + sum(list(h.values())) 

                aceList=[]
                for x in dealer:
                    for number in x:
                        aceList.append(number)
                # print(aceList)
                # print ('hi')
                # print (aceList.count('A'))
                
                # print ("hola")
                # print (otherTotal)

                if (sum(player1[0].values())==2 and sum(player1[1].values())==2) and (sum(dealer[0].values())<=7):
                    player1.pop()
                    player1.append(stack.pop())
                    playerTotal=0
                    for x in player1:
                        playerTotal= playerTotal+ sum(list(x.values())) 
                    print ("split")
                    print (sum(player1[0].values()))
                    bet=bet*2
                    print ("Bet doubled due to split")
                    continue
                elif (sum(player1[0].values())==3 and sum(player1[1].values())==3) and (sum(dealer[0].values())<=7):
                    player1.pop()
                    player1.append(stack.pop())
                    playerTotal=0
                    for x in player1:
                        playerTotal= playerTotal+ sum(list(x.values())) 
                    print ("split")
                    print (sum(player1[0].values()))
                    bet=bet*2
                    print ("Bet doubled due to split")
                    continue
                elif (sum(player1[0].values())==4 and sum(player1[1].values())==4) and (sum(dealer[0].values())==5 or sum(dealer[0].values())==6):
                    player1.pop()
                    player1.append(stack.pop())
                    playerTotal=0
                    for x in player1:
                        playerTotal= playerTotal+ sum(list(x.values())) 
                    print ("split")
                    print (sum(player1[0].values()))
                    bet=bet*2
                    print ("Bet doubled due to split")
                    continue
                elif (sum(player1[0].values())==6 and sum(player1[1].values())==6) and (sum(dealer[0].values())<=6):
                    player1.pop()
                    player1.append(stack.pop())
                    playerTotal=0
                    for x in player1:
                        playerTotal= playerTotal+ sum(list(x.values())) 
                    print ("split")
                    print (sum(player1[0].values()))
                    bet=bet*2
                    print ("Bet doubled due to split")
                    continue
                elif (sum(player1[0].values())==7 and sum(player1[1].values())==7) and (sum(dealer[0].values())<=7):
                    player1.pop()
                    player1.append(stack.pop())
                    playerTotal=0
                    for x in player1:
                        playerTotal= playerTotal+ sum(list(x.values())) 
                    print ("split")
                    print (sum(player1[0].values()))
                    bet=bet*2
                    print ("Bet doubled due to split")
                    continue
                elif (sum(player1[0].values())==8 and sum(player1[1].values())==8):
                    player1.pop()
                    player1.append(stack.pop())
                    playerTotal=0
                    for x in player1:
                        playerTotal= playerTotal+ sum(list(x.values())) 
                    print ("split")
                    print (sum(player1[0].values()))
                    bet=bet*2
                    print ("Bet doubled due to split")
                    continue
                elif (sum(player1[0].values())==9 and sum(player1[1].values())==9) and (sum(dealer[0].values())<=6 or sum(dealer[0].values())==8 or sum(dealer[0].values())==9):
                    player1.pop()
                    player1.append(stack.pop())
                    playerTotal=0
                    for x in player1:
                        playerTotal= playerTotal+ sum(list(x.values())) 
                    print ("split")
                    print (sum(player1[0].values()))
                    bet=bet*2
                    print ("Bet doubled due to split")
                    continue
                elif (sum(player1[0].values())==11 and sum(player1[1].values())==11):
                    player1.pop()
                    player1.append(stack.pop())
                    playerTotal=0
                    for x in player1:
                        playerTotal= playerTotal+ sum(list(x.values())) 
                    print ("split")
                    print (sum(player1[0].values()))
                    bet=bet*2
                    print ("Bet doubled due to split")
                    continue

                    
                elif playerList.count('A')==1 and (playerList.count('2')==1 or playerList.count('3')==1) and len(playerList)==2 and (dealerTotal!=5 and dealerTotal!=6):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif playerList.count('A')==1 and (playerList.count('2')==1 or playerList.count('3')==1) and len(playerList)==2 and (dealerTotal==5 or dealerTotal==6):
                    bet=bet*2
                    print ("Bet doubled due to doubling down")
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                    if playerTotal>21:
                        playerTotal=playerTotal-10
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif playerList.count('A')==1 and (playerList.count('4')==1 or playerList.count('5')==1) and len(playerList)==2 and (dealerTotal!=4 and dealerTotal!=5 and dealerTotal!=6):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif playerList.count('A')==1 and (playerList.count('4')==1 or playerList.count('5')==1) and len(playerList)==2 and (dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                    bet=bet*2
                    print ("Bet doubled due to doubling down")
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                    if playerTotal>21:
                        playerTotal=playerTotal-10
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif playerList.count('A')==1 and playerList.count('6')==1 and len(playerList)==2 and (dealerTotal!=3 and dealerTotal!=4 and dealerTotal!=5 and dealerTotal!=6):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif playerList.count('A')==1 and (playerList.count('6')==1 or playerList.count('7')==1) and len(playerList)==2 and (dealerTotal==3 or dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                    bet=bet*2
                    print ("Bet doubled due to doubling down")
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                    if playerTotal>21:
                        playerTotal=playerTotal-10
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif playerList.count('A')==1 and playerList.count('7')==1 and len(playerList)==2 and (dealerTotal==2 or dealerTotal==7 or dealerTotal==8):
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                    break
                elif playerList.count('A')==1 and playerList.count('7')==1 and len(playerList)==2 and (dealerTotal==9 or dealerTotal==10 or dealerTotal==11):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif playerTotal<=17 and playerList.count('A')>=1 and otherTotal<=6:
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif playerTotal==18 and playerList.count('A')>=1 and (dealerTotal!=2 and dealerTotal!=7 and dealerTotal!=8) and otherTotal<=7:
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif playerTotal>=17 and playerTotal<=21:
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                    break
                elif (playerTotal==16 or playerTotal==15 or playerTotal==14 or playerTotal==13) and (dealerTotal==2 or dealerTotal==3 or dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==16 or playerTotal==15 or playerTotal==14 or playerTotal==13) and (dealerTotal==7 or dealerTotal==8 or dealerTotal==9 or dealerTotal==10 or dealerTotal==11):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif (playerTotal==12) and (dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==12) and (dealerTotal==2 or dealerTotal==3 or dealerTotal==7 or dealerTotal==8 or dealerTotal==9 or dealerTotal==10 or dealerTotal==11):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif (playerTotal==11 and len(player1)==2 and dealerTotal!=11):
                    bet=bet*2
                    print ("Bet doubled due to doubling down")
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==11 and dealerTotal==11):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif (playerTotal==10 and len(player1)==2) and (dealerTotal!=10 and dealerTotal!=11):
                    bet=bet*2
                    print ("Bet doubled due to doubling down")
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==10) and (dealerTotal==10 or dealerTotal==11):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif (playerTotal==9 and len(player1)==2) and (dealerTotal==3 or dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                    bet=bet*2
                    print ("Bet doubled due to doubling down")
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==9) and (dealerTotal!=3 and dealerTotal!=4 and dealerTotal!=5 and dealerTotal!=6):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif playerTotal<=11:
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())

                elif playerTotal>21:
                    aceList2=[]
                    for x in player1:
                        for number in x:
                            aceList2.append(number)
                    # print(aceList2)
                    # print ('hi')
                    # print (aceList2.count('A'))
                    for i in range(len(player1)):
                        front=list(player1[i].keys())
                        back=list(player1[i].values())
                        if (aceList2.count('A')==1):
                            if game==True:
                                playerTotal=playerTotal-10
                                # print ("player total below")
                                # print (playerTotal)
                                # print("woof woof") 
                            game=False
                            continue

                    if playerTotal>21:
                        if aceList2.count('A')==2 and goodbye==True:
                            playerTotal=playerTotal-10
                            goodbye=False
                            continue  

                        if aceList2.count('A')==3 and howdy==True:
                            playerTotal=playerTotal-10
                            howdy=False
                            if goodbye==True:
                                open=True
                            continue
                    
                        if aceList2.count('A')==4 and yo==True:
                            playerTotal=playerTotal-10
                            yo=False
                            if goodbye==True or howdy==True:
                                close=True
                            continue

                        if aceList2.count('A')==5 and evenMore==True:
                            playerTotal=playerTotal-10
                            evenMore=False
                            if goodbye==True or howdy==True or yo==True:
                                open3=True
                            continue
                        
                        if open==True:
                            playerTotal=playerTotal-10
                            open=False
                            continue

                        if close==True:
                            playerTotal=playerTotal-10
                            close=False
                            continue

                        if open3==True:
                            playerTotal=playerTotal-10
                            evenMore=False
                            continue

                        else:
                            break    
                        
                                

                else:
                    break


            while dealerTotal>21:
                for a in range(len(dealer)):
                    front1=list(dealer[a].keys())
                    back1=list(dealer[a].values())
                    if (back1[0]==11):
                        if dealerGame==True:
                            for value1 in list(dealer[a]):
                                dealerTotal=dealerTotal-10
                                # print("meow meow") 
                                if dealerTotal<=21 and dealerTotal>=17: 
                                    break
                                dealer.append(stack.pop())
                                dealerTotal= dealerTotal + sum(dealer[-1].values())
                            
                        dealerGame=False
                
                if dealerTotal<17:
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                        if aceList.count('A')>=1 and dealerTotal==17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                if dealerTotal<=21 and dealerTotal>=17:            
                    break
                if dealerTotal>21:
                    aceList=[]
                    for x in dealer:
                        for number in x:
                            aceList.append(number)
                    # print(aceList)
                    # print ('hi')
                    # print (aceList.count('A'))

                    if aceList.count('A')==2 and woof==True:
                        dealerTotal=dealerTotal-10
                        woof=False
                        if dealerTotal<=21 and dealerTotal>=17:            
                            break
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                            if aceList.count('A')>=1 and dealerTotal==17:
                                dealer.append(stack.pop())
                                dealerTotal= dealerTotal + sum(dealer[-1].values())
                        continue

                    if aceList.count('A')==3 and meow==True:
                        dealerTotal=dealerTotal-10
                        meow=False
                        if woof==True:
                                open2=True
                        if dealerTotal<=21 and dealerTotal>=17:            
                            break
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                            if aceList.count('A')>=1 and dealerTotal==17:
                                dealer.append(stack.pop())
                                dealerTotal= dealerTotal + sum(dealer[-1].values())
                        continue

                    if aceList.count('A')==4 and roar==True:
                        dealerTotal=dealerTotal-10
                        roar=False
                        if meow==True or woof==True:
                                close2=True
                        if dealerTotal<=21 and dealerTotal>=17:            
                            break
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                            if aceList.count('A')>=1 and dealerTotal==17:
                                dealer.append(stack.pop())
                                dealerTotal= dealerTotal + sum(dealer[-1].values())
                        continue

                    if aceList.count('A')==5 and more==True:
                        dealerTotal=dealerTotal-10
                        more=False
                        if meow==True or woof==True or roar==True:
                                close3=True
                        if dealerTotal<=21 and dealerTotal>=17:            
                            break
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                            if aceList.count('A')>=1 and dealerTotal==17:
                                dealer.append(stack.pop())
                                dealerTotal= dealerTotal + sum(dealer[-1].values())
                        continue

                    if open2==True:
                        dealerTotal=dealerTotal-10
                        open2=False
                        if dealerTotal<=21 and dealerTotal>=17:            
                            break
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                            if aceList.count('A')>=1 and dealerTotal==17:
                                dealer.append(stack.pop())
                                dealerTotal= dealerTotal + sum(dealer[-1].values())
                        continue

                    if close2==True:
                        dealerTotal=dealerTotal-10
                        close2=False
                        if dealerTotal<=21 and dealerTotal>=17:            
                            break
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                            if aceList.count('A')>=1 and dealerTotal==17:
                                dealer.append(stack.pop())
                                dealerTotal= dealerTotal + sum(dealer[-1].values())
                        continue
                    
                    if close3==True:
                        dealerTotal=dealerTotal-10
                        close3=False
                        if dealerTotal<=21 and dealerTotal>=17:            
                            break
                        while dealerTotal<17:
                            dealer.append(stack.pop())
                            dealerTotal= dealerTotal + sum(dealer[-1].values())
                            if aceList.count('A')>=1 and dealerTotal==17:
                                dealer.append(stack.pop())
                                dealerTotal= dealerTotal + sum(dealer[-1].values())
                        continue

                    else:
                        break


 
              
        basicStrag()




        if (playerTotal==21 and dealerTotal!=21 and len(player1)==2):
            bankRoll=bankRoll+(bet*1.5)
            print("Player wins hand, blackjack pays off 3 to 2")
        elif playerTotal>21:
            bankRoll=bankRoll-bet
            print("Dealer wins hand")
        elif dealerTotal>21:
            bankRoll=bankRoll+bet
            print("Player wins hand")
        elif playerTotal<dealerTotal:
            bankRoll=bankRoll-bet
            print("Dealer wins hand")
        elif playerTotal==dealerTotal:
            bankRoll=bankRoll
            print("Hand pushes")
        else: 
            bankRoll=bankRoll+bet
            print("Player wins hand")

            

        
        
        cat=[]
        for x in player1:
            cat.append((list(x.keys())))

        lion=[]
        for x in dealer:
            lion.append((list(x.keys())))


        for x in cat:
            if x in smallCards:
                count +=1

            if x in bigCards:
                count -=1


        for x in lion:
            if x in smallCards:
                count +=1

            if x in bigCards:
                count -=1




        oink=[]
        for x in player1:
            oink.append(list(x.keys()))

        moo=[]
        for x in dealer:
            moo.append(list(x.keys()))

        
        print(f'Player hand: {oink}')
        print (playerTotal)
        print(f'Dealer hand: {moo}')
        print (dealerTotal)
        print(f'New true count: {count}')
        print(f'Bankroll: ${bankRoll}')
        print ('\n' + "Next hand" + '\n')      



        # if (len(player1Split1)>=1):
        #     print("split")
        #     player1=[]
        #     dealer=[dealer[0]]
        #     player1.append(player1Split1.pop())
        #     player1.append(stack.pop())


        #     splitPlay=[]
        #     for x in player1:
        #         splitPlay.append(list(x.keys()))

        #     splitDeal=[]
        #     for x in dealer:
        #         splitDeal.append(list(x.keys()))

        #     print(splitPlay, "line ", cf.f_lineno)
        #     print(splitDeal, "line ", cf.f_lineno)
        #     player1Split1=[]
        #     basicStrag()


        if len(stack)<=208:
            stack= numDecks * deck
            random.shuffle(stack)
            count=0
            print("Entire deck has been shuffled")

    
    # elif play == "N" or play =="n":
    #     break
    
    # else:
    #     print("Please enter y/n")

