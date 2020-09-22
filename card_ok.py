import pygame
import random

BLACK = (255,255,255)
screen = pygame.display.set_mode([800,600])
mouseDown = False
keepGoing = True
clock = pygame.time.Clock()
picn = pygame.image.load("card1.png") #번호 저장 해놓기
pics = pygame.image.load("card14.png") #문양 저장 해놓기
sprite_list = pygame.sprite.Group()

class Card(pygame.sprite.Sprite):
    def __init__(self,cimage,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = cimage
        self.rect = self.image.get_rect() #  n is string,  문자열은 rect 가 존재하나? 
        self.pos = pos
        #좌표 저장하기
        self.rect.x = self.pos[0] 
        self.rect.y = self.pos[1]

    def update(self):
        pass

nx = 0
ny = 0
ix = 0
iy = 0
i = 0
n = 0

N = Card(picn,(50, 50))


sprite_list.add(N)

S = Card(pics, (100,100))
sprite_list.add(S)

'''for i in range(0,4):
    for n in range(0,13):
        C = Card(picn[n], pics[i],(nx,ny),(ix,iy)) #객체 만들기
        sprite_list.add(C)

        ix += 31
        nx += 31

    iy += 150
    nx += 150'''

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    #카드 그리기
    screen.fill(BLACK)
    sprite_list.update()
    sprite_list.draw(screen)
    

    clock.tick(60)
    pygame.display.update()

    i += 1
    n += 1
    
pygame.quit()
#2 ** 5 * 5 ** 2
#카드 배치 13 * 4
