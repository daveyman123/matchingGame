import random

class Card(object):
    def __init__(self,suit,val,mana,health, attack):

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
        print "{} of {} with {} mana {} health {} attack".format(self.value,self.suit,self.mana,self.health,self.attack)




class Deck(object):
    def __init__(self):
        self.cards = {}


        self.build()

    def build(self):
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



                self.cards[s + str(v)]=Card(s, v, mana,health,attack)

    def getCards(self):
        return self.cards


    def show(self):
        for k,v in self.cards.iteritems():
            v.show()


    def shuffle2(self):

        keys =  list(self.cards.keys())
        random.shuffle(keys)
        [(key, self.cards[key]) for key in keys]



#    def shuffle(self):
#        for i in range(len(self.cards)-1, 0, -1):
#            r = random.randint(0,i)
#            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]



class Hand(object):
    def __init__(self):
        self.hand = {}

class Board(object):
    def __init__(self):
        self.mpzCards = {}


        self.deck = Deck()

    def minionPlayZone1(self):
        return self.mpz1Cards


    def removeCards(self, cards):

        for key in cards.keys():
            del self.cards[key]


    def addCard(self, card):
        self.cards.update(card)

    def getCards(self):

        return self.cards

    def getCard(self,card):
        return self.cards[card]

    def show(self):
        for k,v in self.cards.iteritems():
            v.show()

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

    def playCard(self, card):
        input = raw_input("enter a card")
        d = {}
        if card in self.hand:
            cardToBePlayed = self.hand[card]

            self.hand.pop(card)
            self.cardToBePlayed = {card:cardToBePlayed}
            self.mpzCards.addCard(d)

        return d

    # def draw(self, deck):
    #     self.hand.update(deck.drawCard())
    #     return self
    def showHand(self):
        for key,value in self.hand.iteritems():
            value.show()

    def getHand(self):
        return self.hand


    def discard(self):
        return self.hand.pop()

    def showInfo(self):
        print "hero = {} mana = {}".format(self.hero,self.mana)

    def drawCard(self):

        randomChoice = random.choice(self.deck.cards.keys())
        value = self.deck.cards[randomChoice]
        self.deck.cards.pop(randomChoice)

        self.card = {randomChoice:value}
        self.hand.update(self.card)





        # card2.getPlayer2().getTable().removeCards(h)

    def playerInfo(self):
        print "cards in player {}'s hand, mana left {}".format(self.name,self.mana)



# class TurnPhases():
#     def __init__(self,player1,player2,table,deck):

class Game(object):


    def run(self):
        gameOver = False
        deck = Deck()
        player1 = Player("bob", "warlock")
        player2 = Player("bilbo", "shaman")
        while gameOver == False:
            player1.mana += 1
            player1.showInfo()
            player1.drawCard()
            player1.playerInfo()
            player1.showHand()
            gameOver = True




def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
