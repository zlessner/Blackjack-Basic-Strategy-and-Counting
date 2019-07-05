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

total=0

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

        player1.extend((stack.pop(), stack.pop()))

        dealer.append(stack.pop())

        for x in player1:
            total= total + sum(list(x.values()))
            
        print (total)
        print (player1)

        # if A in player1 or A in dealer:
        #     print ("Ace")
        #     continue


        
        def basicStrag():
            global bet
            print(dealer, "line ", cf.f_lineno)
            print(player1, "line ", cf.f_lineno)
            while sum(dealer)<17:
                if (player1[0]==2 and player1[1]==2) and (sum(dealer)<=7):
                    # player1Split1=[]
                    player1Split1.append(player1.pop())
                    player1.append(stack.pop())
                    # print ("split")
                    # print(player1)
                    # print(player1Split1)
                elif (player1[0]==3 and player1[1]==3) and (sum(dealer)<=7):
                    # player1Split1=[]
                    player1Split1.append(player1.pop())
                    player1.append(stack.pop())
                    #print ("split")
                elif (player1[0]==4 and player1[1]==4) and (sum(dealer)==5 or sum(dealer)==6):
                    # player1Split1=[]
                    player1Split1.append(player1.pop())
                    player1.append(stack.pop())
                    #print ("split")
                elif (player1[0]==6 and player1[1]==6) and (sum(dealer)<=6):
                    # player1Split1=[]
                    player1Split1.append(player1.pop())
                    player1.append(stack.pop())
                    #print ("split")
                elif (player1[0]==7 and player1[1]==7) and (sum(dealer)<=7):
                    # player1Split1=[]
                    player1Split1.append(player1.pop())
                    player1.append(stack.pop())
                    #print ("split")
                elif (player1[0]==8 and player1[1]==8):
                    # player1Split1=[]
                    player1Split1.append(player1.pop())
                    player1.append(stack.pop())
                    #print ("split")
                elif (player1[0]==9 and player1[1]==9) and (sum(dealer)<=6 or sum(dealer)==8 or sum(dealer)==9):
                    # player1Split1=[]
                    player1Split1.append(player1.pop())
                    player1.append(stack.pop())
                    #print ("split")
    
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
                elif (sum(player1))<=11:
                    player1.append(stack.pop())

                else:
                    break


              
        basicStrag()




        if (sum(player1)==21 and sum(dealer)!=21 and len(player1)==2):
            bankRoll=bankRoll+(bet*1.5)
        elif sum(player1)>21:
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
        print (sum(player1))
        print (dealer)
        print (sum(dealer))
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

