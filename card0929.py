import pygame
import random
from pygame.locals import QUIT,Rect

BLACK = (255,255,255)
screen = pygame.display.set_mode([800,600])
mouseDown = False
keepGoing = True
clock = pygame.time.Clock()
picn = []
pics = []
picn.append(pygame.image.load("card1.png")) #번호 저장 해놓기
picn.append(pygame.image.load("card2.png"))
picn.append(pygame.image.load("card3.png"))
picn.append(pygame.image.load("card4.png"))
picn.append(pygame.image.load("card5.png"))
picn.append(pygame.image.load("card6.png"))
picn.append(pygame.image.load("card7.png"))
picn.append(pygame.image.load("card8.png"))
picn.append(pygame.image.load("card9.png"))
picn.append(pygame.image.load("card10.png"))
picn.append(pygame.image.load("card11.png"))
picn.append(pygame.image.load("card12.png"))
picn.append(pygame.image.load("card13.png"))
pics.append(pygame.image.load("card14.png"))
pics.append(pygame.image.load("card15.png"))
pics.append(pygame.image.load("card16.png"))
pics.append(pygame.image.load("card17.png"))

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


'''for i in range(0,4):
    for n in range(0,13):
        C = Card(picn[n], pics[i],(nx,ny),(ix,iy)) #객체 만들기
        sprite_list.add(C)

        ix += 31
        nx += 31

    iy += 150
    ny += 150'''
#카드 번호 섞기
mixcard = []
for m in range(1,53):
    mixcard.append(m)
random.shuffle(mixcard)
print(mixcard)

nx = 20
ny = 20
sx = 30
sy = 45
mn = 0
ms = 0
count = 0

#카드 섞기 
for s in range(0,4):
    for n in range(0,13):
        mn = mixcard[count] #미리 섞은 카드 번호 넣기 
        
        #카드의 모양과 숫자 넣기 
        while mn >= 13:
            mn = mn - 13
            ms += 1

        if ms == 4:
            ms = 3

        #카드 크기 바꾸기 
        smalln = pygame.transform.scale(picn[mn-1], (10,20))
        smalls = pygame.transform.scale(pics[ms], (31,50))

        #카드 스프라이트에 저장하기 
        N = Card(smalln, (nx, ny))
        sprite_list.add(N)
        S = Card(smalls, (sx,sy))
        sprite_list.add(S)
                
        nx += 61
        sx += 61
        count += 1
        ms = 0
        mmax = 0

    nx = 20
    sx = 30
    ny += 150
    sy += 150

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
