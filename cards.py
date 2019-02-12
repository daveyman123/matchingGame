import random
import time

class Deck(object):
    def __init__(self):
        self.cards = {}




    def build(self):
        d = {}
        for s in ("S", "C", "D", "H"):
            for v in range (1,14):

                if v == 2 or v == 7 or v == 12:
                    mana = 2
                    attack = 1
                    health = 1

                if v == 6 or v == 11:
                    mana = 1
                    attack = 2
                    health = 2

                if v == 3 or v == 8 or v == 13:
                    mana = 3
                    attack = 1
                    health = 1

                if v == 1 or v == 9 or v == 4:
                    mana = 4
                    attack = 4
                    health = 4
                if v == 5 or v == 10:
                    mana = 5
                    attack = 5
                    health = 5



                d[s + str(v)]=Card(s, v, mana,health,attack)
        return d

    def setBuild(self):
        self.cards = self.build()

# maybe use later also use iteritems when iterating over dictionary
    def getCard(self,cardKey):
        for k,v in self.mpzCards.iteritems():
            return v

    def show(self):
        for k,v in self.cards.iteritems():
            print (v.show())


    def shuffle2(self):

        keys =  list(self.cards.keys())
        random.shuffle(keys)
        [(key, self.cards[key]) for key in keys]



    def getCards(self):
        return self.cards

    def rebuildCards(self,hand,mpzCards):
        d = {}
        d = self.build()
        for k,v in hand.iteritems():
            if hand[k] == d[k]:
                hand[v] = self.cards[v]
        for k,v in mpzCards.iteritems():
            if mpzCards[k] == d[k]:
                mpzCards[v] == self.cards[v]


class Card(Deck):
    def __init__(self,suit,val,mana,health, attack):
        super(Card, self).__init__()
        self.self = self
        self.suit = suit
        self.value = val
        self.mana = mana

        self.health = health
        self.attack = attack


    def getHealth(self):
        return self.health
    def getMana(self):
        return self.Mana
    def getAttack(self):
        return self.health
    def setHealth(self,health):
        self.health = health

    def setAttack(self, attack):
        self.attack = attack

    def show(self):
        return "{} of {} with {} mana {} health {} attack".format(self.value,self.suit,self.mana,self.health,self.attack)

    def attacking(self, card2):
        card1 = self
        card1Attack = (card1.getHealth() - card2.getAttack())
        card2Attack = (card2.getHealth() - card1.getAttack())
        card1.setHealth(card1Attack)
        card2.setHealth(card2Attack)
        self.changeCard(card1)
        self.changeCard(card2)

    def changeCard(self,card):

        for k,v in self.getCards().iteritems():
            for k,v in card.iteritems():
                if k == card[k]:
                    self.getCards()[k] = card[k]




#    def shuffle(self):
#        for i in range(len(self.cards)-1, 0, -1):
#            r = random.randint(0,i)
#            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]




class Board(object):
    def __init__(self):

        self.mpzCards = {}


        self.deck = Deck()
        self.deck.setBuild()
    def getCard(self,cardKey):

        for k,v in self.mpzCards.iteritems():
            if k == cardKey:
                return v


    def removeCards(self, cards):

        for key in cards.keys():
            del self.mpzCards[key]


    def addCard(self, card):
        self.mpzCards.update(card)

    def getCards(self):

        return self.mpzCards



    def showCards(self, cardsToShow):
        for k,v in cardsToShow.iteritems():
            print (v.show())

    # def rebuildCards(self):
    #
    #     self.deck.rebuildCards(self.hand,self.mpzCards)


    # def combine(self):
    #     return self.player1.getTable().getCards().update(self.player2.getTable().getCards())

class Player(Board):
    def __init__(self, name, hero):
        super(Player, self).__init__()
        self.mana = 0
        self.name = name
        self.hero = hero

        self.turn = 0
        self.card = {}
        self.hand = {}
        self.cardToBePlayed = {}

    def getMana(self):
        return self.mana

    def getTable(self):
        return self.table

    def playCard(self):
        card = 0
        while card not in self.hand:
            card = raw_input("enter a card in your hand you want to play into the main playing zone. for exampe S8 is the 8 of spades ")

        if card in self.hand:
            cardToBePlayed = self.hand[card]

            self.hand.pop(card)
            self.cardToBePlayed = {card:cardToBePlayed}
            self.addCard(self.cardToBePlayed)
    def playRandomCard(self):

        card = random.choice(self.hand.keys())
        cardToBePlayed = self.hand[card]

        self.hand.pop(card)
        self.cardToBePlayed = {card:cardToBePlayed}
        self.addCard(self.cardToBePlayed)



    # def draw(self, deck):
    #     self.hand.update(deck.drawCard())
    #     return self
    def showHand(self):
        for key,value in self.hand.iteritems():
            print (value.show())

    def getHand(self):
        return self.hand


    def discard(self):
        return self.hand.pop()

    def showInfo(self):
        print ("hero = {} mana = {}".format(self.hero,self.mana))

    def drawCard(self):

        randomChoice = random.choice(self.deck.cards.keys())
        value = self.deck.cards[randomChoice]
        self.deck.cards.pop(randomChoice)

        self.card = {randomChoice:value}
        self.hand.update(self.card)


    def remove(self):
        h = {}
        for k,v in self.mpzCards.iteritems():
            if v.getHealth()<=1:
                h[k]=v
                print (v.show() + " was removed from play because it died")
        self.removeCards(h)


    def attacking(self,player):
        cardAttack = raw_input("select the card you want to attack with ")
        cardDefend = raw_input("in the opposing play zone select the card you want to attack ")

        cardAttack = self.getCard(cardAttack)
        cardDefend = player.getCard(cardDefend)


        print (cardAttack.show())
        print (cardDefend.show())

        cardAttack.attacking(cardDefend)

        for i in range(3):
            print ("...")
            time.sleep(1)

        self.remove()

        self.deck.rebuildCards(self.hand,self.mpzCards)






    def showMPZ(self):
        print ("the cards for {} in the MPZ are ".format(self.name))
        self.showCards(self.mpzCards)


        # card2.getPlayer2().getTable().removeCards(h)

    def playerInfo(self):
        print ("cards in player {}'s hand, mana left {}".format(self.name,self.mana))



# class TurnPhases():
#     def __init__(self,player1,player2,table,deck):

class Game(object):


    def run(self):
        gameOver = False
        deck = Deck()
        deck.setBuild()
        player1 = Player("bob", "warlock")
        player2 = Player("bilbo", "shaman")
        while gameOver == False:
            player1.mana += 1
            player1.showInfo()
            player1.drawCard()
            player2.drawCard()

#initial showing of cards

            player1.playerInfo()
            print ("player 1 hand")
            player1.showHand()
            print ("player 2 hand")
            player2.showHand()
            player1.showMPZ()
            player2.showMPZ()

#playing cards
            player1.playCard()
            player2.playRandomCard()

            print ("player 1 hand")
            player1.showHand()
            print ("player 2 hand")
            player2.showHand()
            player1.showMPZ()
            player2.showMPZ()

#attacking
            player1.attacking(player2)
            player1.showMPZ()
            player2.showMPZ()
            gameOver = True




def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
