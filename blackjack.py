import random

from inspect import currentframe

cf = currentframe()

#figure out ace thing
#figure out split thing
#finish up basic strategy
#catch fixes in logic (such as possibly when to double down with a 9)
#simulate many times to see if make any money over time
#sudo code and readme
# adding "or 11 logic"
# soft 17 rule
# [['A'], ['J'], ['10']]



cards= [{"2":2}, {"3":3}, {"4":4}, {"5":5}, {"6":6}, {"7":7}, {"8":8}, {"9":9}, {"10":10}, {"J":10}, {"Q":10}, {"K":10}, {"A":11}]

smallCards = [list(cards[0].keys()),list(cards[1].keys()),list(cards[2].keys()),list(cards[3].keys()),list(cards[4].keys())]

bigCards = [list(cards[8].keys()),list(cards[9].keys()),list(cards[10].keys()),list(cards[11].keys()),list(cards[12].keys())]



# print (cards[0].items())

# show= list(cards[0].keys())

# print (sum(cards[0].values()))

# print (show[0])





count =0

bankRoll=500

deck= cards*4

numDecks=8

stack= numDecks * deck

random.shuffle(stack)


# while True:
for i in range(10000):

    # play = str(input("Would you like to play the blackjack hand? y/n "))

    # if play == 'y' or play == 'Y':

        if bankRoll<=0:
            break

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

        game=True
        dealerGame=True
        woof=True
        meow=True
        roar=True
        goodbye=True
        howdy=True
        yo=True
        open=False
        close=False
        open2=False
        close2=False
        aceList=[]
        aceList2=[]

        

        for x in player1:
            playerTotal= playerTotal + sum(list(x.values()))  


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

            # print(moo, "line ", cf.f_lineno)
            # print(oink, "line ", cf.f_lineno)
            
            while dealerTotal<17:
                print (playerTotal)
                # if (sum(player1[0].values())==2 and sum(player1[1].values())==2) and (sum(dealer[0].values())<=7):
                #     # player1Split1=[]
                #     player1Split1.append(player1.pop())
                #     player1.append(stack.pop())
                #     playerTotal= playerTotal + sum(player1[-1].values())
                #     # print ("split")
                #     # print(player1)
                #     # print(player1Split1)
                # elif (sum(player1[0].values())==3 and sum(player1[1].values())==3) and (sum(dealer[0].values())<=7):
                #     # player1Split1=[]
                #     player1Split1.append(player1.pop())
                #     player1.append(stack.pop())
                #     playerTotal= playerTotal + sum(player1[-1].values())
                #     #print ("split")
                # elif (sum(player1[0].values())==4 and sum(player1[1].values())==4) and (sum(dealer[0].values())==5 or sum(dealer[0].values())==6):
                #     # player1Split1=[]
                #     player1Split1.append(player1.pop())
                #     player1.append(stack.pop())
                #     playerTotal= playerTotal + sum(player1[-1].values())
                #     #print ("split")
                # elif (sum(player1[0].values())==6 and sum(player1[1].values())==6) and (sum(dealer[0].values())<=6):
                #     # player1Split1=[]
                #     player1Split1.append(player1.pop())
                #     player1.append(stack.pop())
                #     playerTotal= playerTotal + sum(player1[-1].values())
                #     #print ("split")
                # elif (sum(player1[0].values())==7 and sum(player1[1].values())==7) and (sum(dealer[0].values())<=7):
                #     # player1Split1=[]
                #     player1Split1.append(player1.pop())
                #     player1.append(stack.pop())
                #     playerTotal= playerTotal + sum(player1[-1].values())
                #     #print ("split")
                # elif (sum(player1[0].values())==8 and sum(player1[1].values())==8):
                #     # player1Split1=[]
                #     player1Split1.append(player1.pop())
                #     player1.append(stack.pop())
                #     playerTotal= playerTotal + sum(player1[-1].values())
                #     #print ("split")
                # elif (sum(player1[0].values())==9 and sum(player1[1].values())==9) and (sum(dealer[0].values())<=6 or sum(dealer[0].values())==8 or sum(dealer[0].values())==9):
                #     # player1Split1=[]
                #     player1Split1.append(player1.pop())
                #     player1.append(stack.pop())
                #     playerTotal= playerTotal + sum(player1[-1].values())
                #     #print ("split")
    
                if playerTotal>=17 and playerTotal<=21:
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                    break
                elif (playerTotal==16 or playerTotal==15 or playerTotal==14 or playerTotal==13) and (dealerTotal==2 or dealerTotal==3 or dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==16 or playerTotal==15 or playerTotal==14 or playerTotal==13) and (dealerTotal==7 or dealerTotal==8 or dealerTotal==9 or dealerTotal==10 or dealerTotal==11):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif (playerTotal==12) and (dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==12) and (dealerTotal==2 or dealerTotal==3 or dealerTotal==7 or dealerTotal==8 or dealerTotal==9 or dealerTotal==10 or dealerTotal==11):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif (playerTotal==11 and len(player1)==2 and dealerTotal!=11):
                    bet=bet*2
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==11 and dealerTotal==11):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif (playerTotal==10 and len(player1)==2) and (dealerTotal!=10 or dealerTotal!=11):
                    bet=bet*2
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==10) and (dealerTotal==10 or dealerTotal==11):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif (playerTotal==9 and len(player1)==2) and (dealerTotal==3 or dealerTotal==4 or dealerTotal==5 or dealerTotal==6):
                    bet=bet*2
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                elif (playerTotal==9) and (dealerTotal!=3 or dealerTotal!=4 or dealerTotal!=5 or dealerTotal!=6):
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())
                elif playerTotal<=11:
                    player1.append(stack.pop())
                    playerTotal= playerTotal + sum(player1[-1].values())

                elif playerTotal>21:
                    for i in range(len(player1)):
                        front=list(player1[i].keys())
                        back=list(player1[i].values())
                        if (back[0]==11):
                            #AceList length for double Aces
                            if game==True:
                                for value in list(player1[i]):
                                    playerTotal=playerTotal-10
                                    # player1[i][value] = 1
                                    print ("player total below")
                                    print (playerTotal)
                                    print("woof woof") 
                            game=False
                            continue

                    if playerTotal>21:
                        aceList2=[]
                        for x in player1:
                            for number in x:
                                aceList2.append(number)
                        print(aceList2)
                        print ('hi')
                        print (aceList2.count('A'))    

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
                        
                        if open==True:
                            playerTotal=playerTotal-10
                            open=False
                            continue

                        if close==True:
                            playerTotal=playerTotal-10
                            close=False
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
                            # if sum(dealer[-1].values())==11:
                            for value1 in list(dealer[a]):
                                # dealer[a][value1] = 1
                                dealerTotal=dealerTotal-10
                                print("meow meow") 
                                if dealerTotal<=21 and dealerTotal>=17: 
                                    break
                                dealer.append(stack.pop())
                                dealerTotal= dealerTotal + sum(dealer[-1].values())
                                # if sum(dealer[-1].values())==11:
                                #     dealerTotal=dealerTotal-10
                                # if dealerTotal>21:
                                #     continue
                            
                        dealerGame=False

                if dealerTotal<17:
                    while dealerTotal<17:
                        dealer.append(stack.pop())
                        dealerTotal= dealerTotal + sum(dealer[-1].values())
                if dealerTotal<=21 and dealerTotal>=17:            
                    break
                if dealerTotal>21:
                    aceList=[]
                    for x in dealer:
                        for number in x:
                            aceList.append(number)
                    print(aceList)
                    print ('hi')
                    print (aceList.count('A'))

                    if aceList.count('A')==2 and woof==True:
                        dealerTotal=dealerTotal-10
                        woof=False
                        if dealerTotal<=21 and dealerTotal>=17:            
                            break
                        while dealerTotal<17:
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
                        continue

                    if open2==True:
                        dealerTotal=dealerTotal-10
                        open2=False
                        if dealerTotal<=21 and dealerTotal>=17:            
                            break
                        while dealerTotal<17:
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
                        continue

                    else:
                        break


            



                        


              
        basicStrag()




        if (playerTotal==21 and dealerTotal!=21 and len(player1)==2):
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
        print(f'True count: {count}')
        print(f'Bankroll: ${bankRoll}')
        print ("Next hand")      



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

