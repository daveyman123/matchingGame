""" Sprite Sample Program """

import random
import arcade
import math
import time
import cards

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_PLAYER2 = .24
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_CURSOR = 0.01
SPRITE_SCALING_MPZ = .34
COIN_SCALE = 1
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5





class Ships(object):
    def __init__(self):
        self.ships = []
        self.setBuild()
        self.mpz1_list = []
        self.mpz2_list = []
        self.player_ships = []

        self.hit_list = None


    def build(self):
        lst = []
        for s in ("S", "C", "D", "H"):
            for v in range (1,14):

                if v == 2 or v == 7 or v == 12:
                    mana = 2
                    attack = 1
                    health = 1
                    sprite = "coin_01.png"
                    scale = SPRITE_SCALING_PLAYER

                if v == 6 or v == 11:
                    mana = 1
                    attack = 2
                    health = 2
                    sprite = "asfd.png"
                    scale = SPRITE_SCALING_PLAYER
                if v == 3 or v == 8 or v == 13:
                    mana = 3
                    attack = 1
                    health = 1
                    sprite = "character.png"
                    scale = SPRITE_SCALING_PLAYER2
                if v == 1 or v == 9 or v == 4:
                    mana = 4
                    attack = 4
                    health = 4
                    sprite = "cursor.png"
                    scale = SPRITE_SCALING_PLAYER
                if v == 5 or v == 10:
                    mana = 5
                    attack = 5
                    health = 5
                    sprite = "asfd.png"
                    scale = SPRITE_SCALING_PLAYER


                lst.append(Ship(sprite, scale, s, v, mana,health,attack))

        return lst

    def setBuild(self):
        self.ships = self.build()




# maybe use later also use iteritems when iterating over dictionary
    def getCard(self,cardKey):
        for k,v in self.mpz1.iteritems():
            return v

    def show(self):
        for k,v in self.ships.iteritems():
            print (v.show())


    def shuffle2(self):

        keys =  list(self.ships.keys())
        random.shuffle(keys)
        [(key, self.ships[key]) for key in keys]



    def getCards(self):
        return self.player_ships

    def rebuildCards(self,hand,mpzCards):
        d = {}
        d = self.build()
        for k,v in hand.iteritems():
            if hand[k] == d[k]:
                hand[v] = self.ships[v]
        for k,v in mpz1_list.iteritems():
            if mpzCards[k] == d[k]:
                mpzCards[v] == self.ships[v]


class Ship(arcade.Sprite, Ships):

    def __init__(self,sprite, scale,suit,val,mana,health, attack):
        super(Ship, self).__init__(filename = sprite, scale = scale )
        self.self = self
        self.suit = suit
        self.value = val
        self.Mana = mana

        self.health = health
        self.attack = attack


    def getHealth(self):
        return self.health
    def getMana(self):
        return self.Mana
    def getAttack(self):
        return self.attack
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

class Board(object):
    def __init__(self):

        self.mpz1_list = []


        self.deck1 = Ships()
        self.deck = self.deck1.build()
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
        self.hand = []
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



    def drawCard(self):

        randomChoice = random.choice(self.deck)
#make sure to come back and remove from deck
        self.deck.remove(randomChoice)

        self.hand.append(randomChoice)
        return randomChoice


    def showMPZ(self):
        print ("the cards for {} in the MPZ are ".format(self.name))
        self.showCards(self.mpzCards)


        # card2.getPlayer2().getTable().removeCards(h)

    def playerInfo(self):
        print ("cards in player {}'s hand, mana left {}".format(self.name,self.mana))


class Explosion(arcade.Sprite):
    # Static variable that holds all the explosion textures
    explosion_textures = []

    def __init__(self, selected_enemy=None):
        super().__init__("images/explosion6.png")

        # Start at the first frame
        self.current_texture = 0
        self.textures = []
        self.selected_enemy = selected_enemy
        if self.selected_enemy != None:
            self.center_x = selected_enemy.center_x
            self.center_y = selected_enemy.center_y


    def update(self):

        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):

            self.set_texture(self.current_texture)
        else:
            self.kill()


    def setTexture(self, texture_list):
        self.textures = texture_list


    def remove_textures(self):
        self.set_texture(0)


class Button(arcade.Sprite):
    # Static variable that holds all the explosion textures
    explosion_textures = []

    def __init__(self):
        super().__init__("images/gold_1.png")

        # Start at the first frame
        self.current_texture = 0
        self.textures = []
        self.center_x = 500
        self.center_y = 100


    def update(self):

        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):

            self.set_texture(self.current_texture)
        else:
            self.current_texture = 0
            self.textures.clear()
            self.textures.append(arcade.load_texture("images/gold_1.png", scale=COIN_SCALE))
            self.set_texture(self.current_texture)


    def setTexture(self, texture_list):
        self.textures = texture_list


    def remove_textures(self):
        self.set_texture(0)






class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists


        self.player1 = Player("bob", "warlock")

        self.hand = None
        self.xyz = None
        self.selected_enemy = None
        self.enemy = None
        self.bullet_list = None
        self.selected_player = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0


        #load sounds
        self.gun_sound = arcade.sound.load_sound("sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound("sounds/phaseJump1.wav")



        # Don't show the mouse cursor
        self.set_mouse_visible(False)



        self.mpz1_rect = None


    def buttonDraw(self):

        self.xyz = self.player1.drawCard()

        self.player_list.append(self.xyz)
    def setup(self):
        self.bulletToKill = []
        self.background = arcade.load_texture("images/stars.jpg")
        self.button_list = arcade.SpriteList()

        self.explosion_texture_list = []
        self.explosion_texture_list.append(arcade.load_texture("images/explosion6.png", scale=COIN_SCALE))
        self.explosion_texture_list.append(arcade.load_texture("images/explosion5.png", scale=COIN_SCALE))
        self.explosion_texture_list.append(arcade.load_texture("images/explosion4.png", scale=COIN_SCALE))
        self.explosion_texture_list.append(arcade.load_texture("images/explosion3.png", scale=COIN_SCALE))
        self.explosion_texture_list.append(arcade.load_texture("images/explosion2.png", scale=COIN_SCALE))
        self.explosion_texture_list.append(arcade.load_texture("images/explosion1.png", scale=COIN_SCALE))
        self.explosion_texture_list.append(arcade.load_texture("images/explosion0.png", scale=COIN_SCALE))



        self.coin_texture_list = []
        self.coin_texture_list.append(arcade.load_texture("images/gold_1.png", scale=COIN_SCALE))
        self.coin_texture_list.append(arcade.load_texture("images/gold_2.png", scale=COIN_SCALE))
        self.coin_texture_list.append(arcade.load_texture("images/gold_3.png", scale=COIN_SCALE))
        self.coin_texture_list.append(arcade.load_texture("images/gold_4.png", scale=COIN_SCALE))
        self.explosion = Explosion()

        self.explosion_list = arcade.SpriteList()

        self.explosion_list.append(self.explosion)

        self.button = Button()
        # self.button.setTexture(self.coin_texture_list)
        self.button_list.append(self.button)
        self.button.center_x = 500
        self.button.center_y = 100

        self.buttonList = arcade.SpriteList()
        self.buttonSprite = arcade.Sprite("mpz1_rect.png", SPRITE_SCALING_PLAYER2)
        self.buttonSprite.center_x = 300
        self.buttonSprite.center_y = 300
        self.buttonList.append(self.buttonSprite)
        """ Set up the game and initialize the variables. """

        player1 = Player("bob","hunter")
        board = Board()
        self.mpz1_list = []
        self.mpz2_list = []


        self.selected_enemy_list = []
        self.selected_player_list = []
        self.hit_list = []
        # Sprite lists

        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.cursor_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.xyz = arcade.SpriteList()
        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl


        self.mpz1_rect = arcade.Sprite("mpz1_rect.png", SPRITE_SCALING_MPZ)







        self.mpz1_rect.center_x = (SCREEN_WIDTH/2)-100
        self.mpz1_rect.center_y = (SCREEN_HEIGHT/2)-100

        # ship1 = Ship("character.png", SPRITE_SCALING_PLAYER2)
        enemy_ship2 = Ship("coin_01.png", SPRITE_SCALING_PLAYER, "c", 14,3,2,4)

        enemy_ship1 = Ship("enemy.png", SPRITE_SCALING_PLAYER2, "s",4,4,4,4)
        self.enemy_list.append(enemy_ship1)
        self.enemy_list.append(enemy_ship2)
        self.mpz2_list.append(enemy_ship1)
        self.mpz2_list.append(enemy_ship2)
        enemy_ship1.center_x = 200
        enemy_ship1.center_y = 350
        enemy_ship2.center_x = 300
        enemy_ship2.center_y = 350


        x = 55
        for i in self.player_list:

            i.center_x = x
            i.center_y = 55
            x += 55

        # Create cursor
        self.cursor_sprite = arcade.Sprite("cursor.png", SPRITE_SCALING_CURSOR)


        # Create the coins
        # for i in range(COIN_COUNT):
        #
        #     # Create the self.coin instance
        #     # self.coin image from kenney.nl
        #     self.coin = self.coin("coin_01.png", SPRITE_SCALING_COIN)
        #
        #     # Position the self.coin
        #     self.coin.center_x = random.randrange(SCREEN_WIDTH)
        #     self.coin.center_y = random.randrange(SCREEN_HEIGHT)
        #
        #     # Add the self.coin to the lists
        #     self.coin_list.append(self.coin)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # self.coin_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()
        self.cursor_sprite.draw()
        self.mpz1_rect.draw()
        self.xyz.draw()
        self.button.draw()
        self.explosion_list.draw()


        #x = arcade.sprite_list.SpriteList(self.mpz1)

        # Put the text on the screen.
        output = f"Score: {self.score}"
        # for i in self.player_list:
        #     arcade.draw_text(str(i.getAttack()), 10,20,arcade.color.WHITE, 14)
        if self.selected_player != None:
            print("here6")
            arcade.draw_text("Selected Ship has " + str(self.selected_player.getAttack()) + " Attack, "+str(self.selected_player.getHealth()) +
                " Health and Costs " + str(self.selected_player.getMana()) + " Fuel", 10,20,arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        if self.selected_player != None:
            start_x = self.selected_player.center_x
            start_y = self.selected_player.center_y


            # Get from the mouse the destination location for the bullet
            # IMPORTANT! If you have a scrolling screen, you will also need
            # to add in self.view_bottom and self.view_left.
            dest_x = x
            dest_y = y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.degrees(math.atan2(y_diff,x_diff))-90
            self.selected_player.angle = angle
            #self.selected_player.rotate_point(dest_x,dest_y,start_x,start_y,angle)
        # Move the center of the player sprite to match the mouse x, y
        else:
            for i in self.player_list:
                i.angle = 0

        self.cursor_sprite.center_y = y
        self.cursor_sprite.center_x = x
        # self.coin_list = arcade.SpriteList()
        # self.coin.append(arcade.Sprite("images/gold_1.png",1))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if len(self.hit_list) > 0:
            if self.hit_list[0] not in self.mpz1_list:
                self.hit_list[0].center_y = y
                self.hit_list[0].center_x = x
                print ("here")

        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y
    def on_mouse_press(self,x,y,buttons,modifiers):
        if(arcade.check_for_collision(self.cursor_sprite,self.button)):
                print ("here5")
                self.button.setTexture(self.coin_texture_list)
                self.coin_texture_list.append(arcade.load_texture("images/gold_1.png", scale=COIN_SCALE))
                self.coin_texture_list.append(arcade.load_texture("images/gold_2.png", scale=COIN_SCALE))
                self.coin_texture_list.append(arcade.load_texture("images/gold_3.png", scale=COIN_SCALE))
                self.coin_texture_list.append(arcade.load_texture("images/gold_4.png", scale=COIN_SCALE))

                self.button_list = arcade.SpriteList()
                self.button_list.append(self.button)
                print (len(self.coin_texture_list))
                self.buttonDraw()
        # self.mpz2_list = arcade.check_for_collision_with_list(self.mpz1_rect, self.mpz2_list)
        self.selected_enemy_list = arcade.check_for_collision_with_list(self.cursor_sprite, self.enemy_list)
        bullet = arcade.Sprite("images/laserBlue01.png", 1)
        self.bullet_list.append(bullet)


        if len(self.hit_list) > 0:
            self.selected_player_list.append(self.hit_list[0])
            print ("here")
            self.selected_player = self.selected_player_list[0]
            print (self.selected_player_list[0])
            # print(self.selected_player.show())
        else:
            print("select a player to attack")



        if self.selected_player in self.mpz1_list:
            print ("here2")


            if len(self.mpz2_list) > 0 and len(self.selected_enemy_list) > 0:
                self.selected_enemy = self.selected_enemy_list[0]

                print ("here3")
                x_diff = self.selected_enemy.center_x - self.selected_player.center_x
                y_diff = self.selected_enemy.center_y - self.selected_player.center_y
                angle = math.atan2(y_diff, x_diff)

                bullet.center_x = self.selected_player.center_x
                bullet.center_y = self.selected_player.center_y

                # Angle the bullet sprite so it doesn't look like it is flying
                # sideways.
                bullet.angle = math.degrees(angle)
                print(f"Bullet angle: {bullet.angle:.2f}")


                arcade.play_sound(self.gun_sound)

                self.gun_sound = arcade.sound.load_sound("sounds/laser1.wav")


                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.

                bullet.change_x = math.cos(angle) * BULLET_SPEED
                bullet.change_y = math.sin(angle) * BULLET_SPEED



                self.selected_player_list = []
                self.selected_player = None


        if len(self.hit_list) == 0:
            self.selected_player_list = []
            self.selected_player = None

        # self.selected_button = arcade.check_for_collision_with_list(self.cursor_sprite, self.buttonList)
        # if len(self.selected_button) > 0:
        #     self.button()

    def on_mouse_release(self, x,y,buttons,modifiers):
        if self.selected_player not in self.mpz1_list:
            self.selected_player = None
            self.mpz1_list = arcade.check_for_collision_with_list(self.mpz1_rect, self.player_list)
        else:
            self.mpz1_list = arcade.check_for_collision_with_list(self.mpz1_rect, self.player_list)


        x = len(self.mpz1_list)
        if x > 0:
            k = 0
            z = self.mpz1_rect.left + 55
            h = self.mpz1_rect.bottom +55
            while k < x:

                self.mpz1_list[k].center_x = z
                self.mpz1_list[k].center_y = h


                k+=1
                z += 55

        l = 55
        for i in self.player_list:
            if i not in self.mpz1_list:
                i.center_x = l
                i.center_y = 55
                l += 55




    def update(self, delta_time):
        """ Movement and game logic """

        self.button.update()
        self.explosion_list.update()
        if len(self.bullet_list) > 0:

            for x in self.selected_enemy_list:

                if arcade.check_for_collision(self.bullet_list[-1],x):

                    self.bullet_list[-1].kill()



                    self.explosion = Explosion(x)
                    self.explosion.setTexture(self.explosion_texture_list)
                    self.explosion_list.append(self.explosion)
                    arcade.play_sound(self.hit_sound)


                    self.hit_sound = arcade.sound.load_sound("sounds/phaseJump1.wav")




        # Call update on all sprites (The sprites don't do much in this
        # example though.)


                # self.button_list.append(button)
        # self.coin_list = arcade.SpriteList()
        # self.coin = arcade.SpriteList()
        #
        # self.coin_list.update()
        # self.coin_list.update_animation()
        self.bullet_list.update()

        # Generate a list of all sprites that collided with the player.
        self.hit_list = arcade.check_for_collision_with_list(self.cursor_sprite, self.player_list)

        # Loop through each colliding sprite, remove it, and add to the score.


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
