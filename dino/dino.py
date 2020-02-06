import pygame, sys, random
from pygame.locals import*
pygame.init()

FPS=60
fpsClock=pygame.time.Clock()

okno=pygame.display.set_mode((800,400))
pygame.display.set_caption('Dino Chrome')

def gra():

    class dino:
         x=100
         y=259
         px=0
         py=0
         jump=True
         fall=False
         lewa=pygame.image.load('lewa.png')
         prawa=pygame.image.load('prawa.png')
         recx1=53
         recy1=33
         recx2=20
         recy2=20
         vy=1

    class game:
        teren1=pygame.image.load('teren1.png')
        teren2=pygame.image.load('teren2.png')
        teren3=pygame.image.load('teren3.png')

        kaktus1=pygame.image.load('kaktus1.png')
        kaktus2=pygame.image.load('kaktus2.png')
        kaktus3=pygame.image.load('kaktus3.png')
        kaktus4=pygame.image.load('kaktus4.png')

        tlo1x=0
        tlo2x=800
        tlo3x=1600

        recx=33
        recy=60

        vtlo=8.0
        pom=0
        licznik=0
        licznik2=0.0

        czcionka=pygame.font.SysFont("monospace", 20)
        czcionka2=pygame.font.SysFont("monospace", 50)

    kaktus=pygame.image.load('kaktus1.png')
    kaktus2=pygame.image.load('kaktus4.png')
    kaktus3=pygame.image.load('kaktus3.png')

    odlkak=0
    odlkak2=0
    odlkak3=0
    i=0
    czas=4.4
    dy=0
    l=0

    wys=250
    wys2=250
    wys3=250

    while True:
        i+=1
        game.licznik2+=1
        game.pom+=0.2
        game.licznik+=0.2

        if game.pom>100:
            game.vtlo+=0.8
            game.pom-=100

        okno.fill((245,245,245))
        tekst=game.czcionka.render(str(game.licznik),200,(50,50,50))
        tekst2=game.czcionka.render(str("00"),200,(50,50,50))
        tekst3=game.czcionka.render(str("0"),200,(50,50,50))
        tekst4=game.czcionka2.render("GAME OVER!",200,(50,50,50))

        if game.licznik<100:
            okno.blit(tekst2,(717,20))
            okno.blit(tekst,(740,20))
        elif game.licznik<1000:
            okno.blit(tekst3,(717,20))
            okno.blit(tekst,(728,20))
        else:
            okno.blit(tekst,(740,20))

        tlo1=game.teren1
        tlo2=game.teren2
        tlo3=game.teren3

        if game.tlo1x<=-800:
            game.tlo1x=1600

        if game.tlo2x<=-800:
            game.tlo2x=1600

        if game.tlo3x<=-800:
            game.tlo3x=1600

        game.tlo1x-=game.vtlo
        game.tlo2x-=game.vtlo
        game.tlo3x-=game.vtlo

        okno.blit(tlo1,(game.tlo1x,300))
        okno.blit(tlo2,(game.tlo2x,300))
        okno.blit(tlo3,(game.tlo3x,300))

        if i%10==0 or i%10==1 or i%10==2 or i%10==3 or i%10==4:
            dinozaur=dino.lewa
        else:
            dinozaur=dino.prawa

        okno.blit(dinozaur,(dino.x,dino.y))

        if dino.jump==True:
            czas-=0.189
            dy=czas*czas
            dino.y-=dy
            if dino.y<=120:
                dino.jump=False
                dino.fall=True
                czas=1.52
        elif dino.fall==True:
            czas+=0.2
            dy=czas*czas
            dino.y+=dy
            if dino.y>=259:
                dino.fall=False
                dino.y=259
                czas=4.4

        if odlkak<-30 and odlkak3<400 and odlkak2<400:
            odlkak=random.randint(800,1400)
            if odlkak%4==0:
                kaktus=game.kaktus1
                wys=250
            if odlkak%4==3:
                kaktus=game.kaktus2
                wys=275
            if odlkak%4==2:
                kaktus=game.kaktus3
                wys=250
            if odlkak%4==0:
                kaktus=game.kaktus4
                wys=250

        if odlkak2<-30 and odlkak<400 and odlkak3<400:
            odlkak2=random.randint(800,1400)
            if odlkak2%4==0:
                kaktus2=game.kaktus1
                wys2=250
            if odlkak2%4==1:
                kaktus2=game.kaktus2
                wys2=275
            if odlkak2%4==2:
                kaktus2=game.kaktus3
                wys2=250
            if odlkak2%4==3:
                kaktus2=game.kaktus4
                wys2=250

        if odlkak3<-30 and odlkak2<400 and odlkak<400:
            odlkak3=random.randint(800,1400)
            if odlkak3%4==0:
                kaktus3=game.kaktus1
                wys3=250
            if odlkak3%4==1:
                kaktus3=game.kaktus2
                wys3=275
            if odlkak3%4==2:
                kaktus3=game.kaktus3
                wys3=250
            if odlkak3%4==3:
                kaktus3=game.kaktus4
                wys3=250

        odlkak-=game.vtlo
        odlkak2-=game.vtlo
        odlkak3-=game.vtlo

        okno.blit(kaktus,(odlkak,wys))
        okno.blit(kaktus2,(odlkak2,wys2))
        okno.blit(kaktus3,(odlkak3,wys3))

        if (abs(dino.x-odlkak)<=dino.recx1 and abs(dino.y-wys-2)<=dino.recy1 and dino.fall==False) or (abs(dino.x-odlkak2)<=dino.recx1 and abs(dino.y-wys2-2)<=dino.recy1 and dino.fall==False) or (abs(dino.x-odlkak3)<=dino.recx1 and abs(dino.y-wys3-2)<=dino.recy1 and dino.fall==False) or (abs(dino.x-odlkak)<=game.recx and abs(dino.y-wys)<=dino.recy1 and dino.jump==False) or (abs(dino.x-odlkak2)<=game.recx and abs(dino.y-wys2)<=dino.recy1 and dino.jump==False) or (abs(dino.x-odlkak3)<=game.recx and abs(dino.y-wys3)<=dino.recy1 and dino.jump==False):

            okno.blit(tekst4,(260,70))
            pygame.display.update()

            while True:

                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type==KEYDOWN and event.key==K_SPACE:
                        gra()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if event.type==KEYDOWN and event.key==K_SPACE and dino.y>=259:
                dino.jump=True

        pygame.display.update()
        fpsClock.tick(FPS)
gra()
