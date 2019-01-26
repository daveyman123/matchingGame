import random
import string
import pygame



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
rect = pygame.Rect((0, 0, 50, 50))
rect.center = screen.get_rect().center

pygame.display.set_caption("Tracking System")

# - objects -

rect2 = pygame.Rect((0,0,100,100))
                                



pygame.display.flip()
rectangle_draging = False

clock = pygame.time.Clock()

message = "no collision"

running = True
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                if rect.collidepoint(event.pos):
                                        rectangle_draging = True
                                        mouse_x, mouse_y = event.pos
                                        offset_x = rect.x - mouse_x
                                        offset_y = rect.y - mouse_y

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:            
                        rectangle_draging = False

                elif event.type == pygame.MOUSEMOTION:
                    if rectangle_draging:
                        mouse_x, mouse_y = event.pos
                        rect.x = mouse_x + offset_x
                        rect.y = mouse_y + offset_y
                    if rect.collidepoint(rect2.x, rect2.y):
                        message = "collision"
                    else:
                        message = "No collision"

        print(message)                       

        screen.fill((255,255,255))

        pygame.draw.rect(screen, (0,255,255), rect2)

        pygame.draw.rect(screen, (255,0,0), rect)
        pygame.display.flip()

        clock.tick(FPS)

pygame.quit()

















        
        
