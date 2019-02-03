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

    def getCards(self):
        return self





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

    def drawCard(self):
        d = {}
        randomChoice = random.choice(self.cards.keys())
        value = self.cards[randomChoice]
        self.cards.pop(randomChoice)

        d = {randomChoice:value}
        return d
class Table(object):
    def __init__(self):
        self.cards = {}

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



class Player(object):
    def __init__(self, name, hero):
        self.hand = {}
        self.mana = 0
        self.name = name
        self.hero = hero
        self.table = Table()

    def getMana(self):
        return self.mana

    def getTable(self):
        return self.table

    def playCard(self, card):
        d = {}
        if card in self.hand:
            cardToBePlayed = self.hand[card]

            self.hand.pop(card)
            d = {card:cardToBePlayed}
            self.table.addCard(d)

        return d

    def draw(self, deck):
        self.hand.update(deck.drawCard())
        return self
    def showHand(self):
        for key,value in self.hand.iteritems():
            value.show()

    def getHand(self):
        return self.hand


    def discard(self):
        return self.hand.pop()

    def showInfo(self):
        print "hero = {} mana = {}".format(self.hero,self.mana)


    def attack(self,card1, card2):
        card1Attack = (card1.getHealth() - card2.getAttack())
        card2Attack = (card2.getHealth() - card1.getAttack())
        card1.setHealth(card1Attack)
        card2.setHealth(card2Attack)
        h = {}
        d = self.table.getCards()
        for k,v in d.iteritems():
            if v.getHealth()<=1:
                h[k]=v
        self.table.removeCards(h)



deck = Deck()

deck.shuffle2()

bob = Player("bob", "Shaman")
bilbo = Player("bilbo", "Warlock")

bob.draw(deck).draw(deck).draw(deck)
bob.showInfo()
print "bob hand"
bob.showHand()
try:
    card1 = str(raw_input("pick a card to play for example: S8 = 8 of spades "))
except:
    print"error"

bob.playCard(card1)
print "bob hand"
bob.showHand()


##Bilbo setup
bilbo.draw(deck).draw(deck).draw(deck)
bilbo.showInfo()
print "bilbos hand"
bilbo.showHand()

card2 = random.choice(bilbo.getHand().keys())
bilbo.playCard(card2)
print "bilbos table"
bilbo.getTable().show()

print "bob table"
bob.getTable().show()

print "cards are attacking"
bob.attack(bob.getTable().getCard(card1),bilbo.getTable().getCard(card2))
print "bilbos table"
bilbo.getTable().show()

print "bob table"
bob.getTable().show()
