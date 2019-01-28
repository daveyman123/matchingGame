import random
import string
import pygame
import time

MIDNIGHT_BLUE = (25,25,112)
RED = (255, 0, 0)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 128, 0)



class Rectangle:
        x = 0 #starting position x and y
        y = 0
        rect = pygame.Rect((x, y, 111, 33))
        color = (255,255,0)
        rectangle_draging = False
        
        def __init__(self, x, y, screen, color):
                self.x = x
                self.y = y
                self.rect = pygame.Rect((x, y, 111,33))
                self.screen = screen
                self.color = color

        def set_draging(self, rectangle_d):
                self.rectangle_draging = rectangle_d
                
        def get_draging(self):
                return self.rectangle_draging
                            
        def draw(self):
                pygame.draw.rect(screen, self.color, self.rect)
        
        def get_rect(self): ## get rekt haha
                return self.rect
                
        def set_y(self, y):
                self.y = y

        def set_x(self, x):
                self.x = x

        def get_color(self):
                return self.color
                

def randomAlphabet():
        randomizedAlphabet = []
        alphabet = (string.ascii_uppercase)
        alphabetList = []
        for i in alphabet:
                alphabetList.append(i)
        x = len(alphabetList)

       


        while x > 0:
                z = random.randint(0,x)
                
                h = alphabetList[z-1]
                randomizedAlphabet += h
                alphabetList.remove(h)
                x-=1
                x = len(alphabetList)

        return randomizedAlphabet 

FPS = 30

pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((255,255,255))
#rect = pygame.Rect((0, 0, 50, 50))
#rect.center = screen.get_rect().center

rectObject = Rectangle(200,200, screen, MIDNIGHT_BLUE)
rect = rectObject.get_rect()

#rect.center = screen.get_rect().center

pygame.display.set_caption("matching game")

# - objects -

rect2 = pygame.Rect((0,0,100,100))
                                



pygame.display.flip()


rectDict = {}



def randomColor():
        colorList = [GREEN,MIDNIGHT_BLUE,YELLOW,ORANGE,PINK,RED,PURPLE]
        newColorList = []
       
                
                
        random.shuffle(colorList)
              
        return colorList

x = randomColor()
y = randomColor()
for i in range(len(randomColor())):
        
        rectDict["rect{0}".format(i)]=Rectangle(10,i*55, screen, x[i])


rectDict2 = {}
for i in range(len(randomColor())):
        rectDict2["rect{0}".format(i)]=Rectangle(300,i*55, screen, y[i])
        

        
        
        
        
        



clock = pygame.time.Clock()

message = "no collision"

rectangle_draging = False


score = 0
font = pygame.font.Font(None, 32)
font_color = (100, 200, 150)


           
running = True
while running:


        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                for k,v in rectDict.iteritems():
                                        

                                        if v.get_rect().collidepoint(event.pos):
                                                v.set_draging(True)
                                                message = str(v.get_draging())
                                                
                                                mouse_x, mouse_y = event.pos
                                                offset_x = v.get_rect().x - mouse_x
                                                offset_y = v.get_rect().y - mouse_y
                                for k,v in rectDict2.iteritems():
                                        

                                        if v.get_rect().collidepoint(event.pos):
                                                v.set_draging(True)
                                                message = str(v.get_draging())
                                                
                                                mouse_x, mouse_y = event.pos
                                                offset_x = v.get_rect().x - mouse_x
                                                offset_y = v.get_rect().y - mouse_y
                                
                                

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        for k,v in rectDict.iteritems():
                                v.set_draging(False)

                        
                                
                        for k,v in rectDict2.iteritems():
                                v.set_draging(False)

                        
                                
                
                elif event.type == pygame.MOUSEMOTION:
                    
                        
                    for k,v in rectDict.iteritems():
                            
                                if v.get_draging():

                                            
                                                
                                        mouse_x, mouse_y = event.pos
                                        v.get_rect().x = mouse_x + offset_x
                                        v.get_rect().y = mouse_y + offset_y
                                        for h,m in rectDict2.iteritems():
                                                if v.get_rect().colliderect(m.get_rect()) and v.get_color() == m.get_color():
                                                        rectDict.pop(k,v)
                                                        rectDict2.pop(h,m)
                                                        score +=1
                                                        break
                                                        message = "collision"
                                                
                                                else:
                                                        message = "No collision"
                                        break     
                   

        screen.fill((255,255,255)) #important to do this before drawing other objects

        #pygame.draw.rect(screen, (0,255,255), rect2)

        #rectObject.draw()
        txt_surf = font.render(str(score), True, font_color)
        #pygame.draw.rect(screen, font_color, rect, 2)
        screen.blit(txt_surf,screen.get_rect().center)

        for k,v in rectDict.iteritems():
                v.draw()

        
        for k,v in rectDict2.iteritems():
                v.draw()

        print(message)            
        
        
        pygame.display.flip()

        clock.tick(FPS)

pygame.quit()

















        
        
