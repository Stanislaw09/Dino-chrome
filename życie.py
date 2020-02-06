import pygame, sys
from pygame.locals import*
pygame.init()

class Plansza():
    def __init__(self):
        self.FPS=2
        self.fpsClock=pygame.time.Clock()
        self.gra=Gra()
        self.okno=pygame.display.set_mode((900,700))
        self.mx=-100
        self.my=-100

    def Siatka(self):
        self.x=0
        self.y=0
        for i in range(0,35):
            for j in range(0,45):
                pygame.draw.rect(self.okno,(100,0,0),(self.x,self.y,20,20),1)
                self.x+=20
            self.y+=20
            self.x=0
        pygame.display.update()

    def Zaznaczenie(self,mx,my):
        pygame.draw.rect(self.okno,(255,0,150),(self.mx-(self.mx%20)+1,self.my-(self.my%20)+1,18,18))
        print(self.mx,"  ",self.my)
        pygame.display.update()

    def Event(self):
        self.pm=0
        while self.pm==0:
            for event in pygame.event.get():

                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type==MOUSEBUTTONDOWN:
                    self.mx,self.my=event.pos
                    self.gra.tab[int(self.mx/20)][int(self.my/20)]=1
                    self.Zaznaczenie(self.mx, self.my)

                if event.type==KEYDOWN and event.key==K_RETURN:
                    self.pm=1

    def Rysowanie(self):
        for j in range(0,35):
            for i in range(0,45):
                if self.gra.tab[i][j]==1:
                    pygame.draw.rect(self.okno,(255,0,150),(i*20,j*20,18,18))
        pygame.display.update()

    def Wykonanie(self):
        self.Siatka()
        self.Event()

        while True:
            self.fpsClock.tick(self.FPS)
            self.gra.Update()
            self.okno.fill((0,0,0))
            self.Siatka()
            self.Rysowanie()

            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==KEYDOWN and event.key==K_UP:
                    self.FPS+=1
                if event.type==KEYDOWN and event.key==K_DOWN and self.FPS>1:
                    self.FPS-=1
                if event.type==KEYDOWN and event.key==K_RETURN:
                    pygame.quit()
                    game=Plansza()
                    game.Wykonanie()


class Gra():
    def __init__(self):
        self.x=0
        self.y=0
        self.tab=[[0 for j in range(48)] for i in range(48)]
        self.change=[[0 for j in range(48)] for i in range(48)]

    def Otoczka(self,a,b):
        self.pom=0
        for j in range(b-1,b+2):
            for i in range(a-1,a+2):
                if self.tab[i][j]==1:
                    self.pom+=1

        if (((self.pom==3 or self.pom==4)  and  self.tab[a][b]==1)  or  (self.pom==3 and self.tab[a][b]==0)):
            self.change[a][b]=1
        else:
            self.change[a][b]=0

    def Zamiana(self):
        for j in range(45):
            for i in range(45):
                self.tab[i][j]=self.change[i][j]

    def Przejscie(self):
        for self.j in range(45):
            for self.i in range(45):
                self.Otoczka(self.i, self.j)

    def Update(self):
        self.Przejscie()
        self.Zamiana()


if __name__ == "__main__":
    game=Plansza()
    game.Wykonanie()
