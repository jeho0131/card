import pygame
import random

BLACK = (255,255,255)
screen = pygame.display.set_mode([800,600])
mouseDown = False
keepGoing = True
clock = pygame.time.Clock()
picn = ["A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, "J", "Q", "K"] #번호 저장 해놓기
pics = ["♠", "◆", "♥", "♣"] #문양 저장 해놓기
sprite_list = pygame.sprite.Group()

class Card(pygame.sprite.Sprite):
    def __init__(self,num,shape,posn,poss):
        pygame.sprite.Sprite.__init__(self)
        self.num = num 
        self.shape = shape
        #self.number = self.num.get_rect() #좌표 저장하는 곳 만들기
        #self.picture = self.shape() #좌표 저장하는 곳 만들기 2
        self.pos1 = posn 
        self.pos2 = poss
        #좌표 저장하기
        '''self.num.x = pos1[0] 
        self.num.y = pos1[1]
        self.shape.x = pos2[0]
        self.shape.y = pos2[1]'''

    def update(self):++
        pass

nx = 0
ny = 0
ix = 0
iy = 0

for n in range(0,13):
    for i in range(0,4):
        C = Card(picn[n], pics[i],(nx,ny),(ix,iy)) #객체 만들기
        sprite_list.add(C)

        ix += 
        iy += 1
        nx += 1
        ny += 1

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
pygame.quit()
#2 ** 5 * 5 ** 2
#카드 배치 13 * 4
