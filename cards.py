import random

class Table(object):
    def __init__(self):
        self.card = []

    def setCard(self, card):
        self.card.append(card)

    def getCard(self):
        return self.card

    def showTable(self):
        for i in self.card:
            i.show()

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


    def attack(card1, card2):
        card1.health -= card2.getAttack
        card2.health -= card1.getAttack


    def show(self):
        print "{} of {} with {} mana {} health {} attack".format(self.value,self.suit,self.mana,self.health,self.attack)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ("Spades", "Clubs", "Diamonds", "Hearts"):
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

                self.cards.append(Card(s, v, mana,health,attack))


    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name, hero):
        self.hand = []
        self.mana = 0
        self.name = name
        self.hero = hero
        self.table = Table()

    def getMana(self):
        return self.mana

    def getTable(self):
        return self.table

    def playCard(self):
        cardToBePlayed = self.hand[0]
        self.table.setCard(cardToBePlayed)
        self.hand.pop(0)

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    def showHand(self):
        for card in self.hand:
            card.show()

    def getHand(self):
        return self.hand


    def discard(self):
        return self.hand.pop()

    def showInfo(self):
        print "hero = {} mana = {}".format(self.hero,self.mana)

deck = Deck()

deck.shuffle()

bob = Player("bob", "Shaman")
bilbo = Player("bilbo", "Warlock")
bob.draw(deck).draw(deck).draw(deck)
bob.showInfo()
print "hand"
bob.showHand()
print "table"
bob.getTable().showTable()
bob.playCard()
print "hand"
bob.showHand()
print "table"
bob.getTable().showTable()
