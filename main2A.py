import pygame
import time
import random
import sys
from tkinter import *
pygame.init()
width = 800
length = 600
fire = False
speedbullet = 20
bullets = []
enemyis = []
font = pygame.font.SysFont("arial", 20)
score = 0
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
gameover = False
menu = True
pause = False
fps = 30
#pygame.mixer.music.load("effect/bgmusic.mp3")
bg = pygame.image.load("effect/space.jpg")
shipim = pygame.image.load("effect/ship.png")
bbup = pygame.image.load("effect/bullet.png")
alien = pygame.image.load("effect/alien.png")
bso = pygame.mixer.Sound("effect/bullet.wav")
adi = pygame.mixer.Sound("effect/painr.wav")
hitme = pygame.mixer.Sound("effect/hitme.wav")
fireball = pygame.image.load("effect/fireball.png")
explotion = pygame.image.load("effect/explode.png")
flashi = pygame.image.load("effect/lighting.png")
snail = pygame.image.load("effect/snail.png")
aid = pygame.image.load("effect/hospital.png")
pbut = pygame.image.load("effect/pause.png")
plbut = pygame.image.load("effect/play.png")
blast = pygame.image.load("effect/blastlaser.png")
dangar = pygame.image.load("effect/ship.png")
dangarlaser = pygame.image.load("effect/greenlaser.png")
dangarwarn = pygame.image.load("effect/laserwarn.png")
menubut = pygame.image.load("effect/menu.png")
smallbomb = pygame.image.load("effect/bomb.png")
grenade=  pygame.image.load("effect/grenade.png")
bgsize = bg.get_size()
pygame.display.set_icon(shipim)
display = pygame.display.set_mode((bgsize[0], bgsize[1]))
pygame.mixer.music.set_volume(60)
explode = []
respeed = pygame.time.Clock()
maoue = []
missile = []
item = []
imi = 0
par = True
pausebe = True
pygame.display.set_caption("whiteline")
#pygame.mixer.music.play()
explodelista = []
explodelistb = []
explodelistab = []
for i in range(0, 9):
    explodelista.append(pygame.image.load(
        f'effect/bomb/regularExplosion0{i}.png'))
for i in range(0, 9):
    explodelistb.append(pygame.image.load(
        f'effect/bomba/regularExplosion0{i}.png'))
for i in range(0, 9):
    explodelistab.append(pygame.image.load(
        f'effect/bombab/regularExplosion0{i}.png'))
clock = 0
dangatime = 600
aimbot = False
blasta = False
blastt = 0
power = 100

#properties
shiphealth = 100
shipspeed = 10
gamefps = 25
enemycount = 30
enemyspeed = 10
dangacount = 10

    
class watashi:
    def __init__(self, posx, posy, sta):
        self.posx = posx
        self.posy = posy
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.health = shiphealth
        self.speed = shipspeed
        self.sta = sta
        self.gar = 1

    def draw(self):
        if self.sta == "normal":
            self.speed = 8
        if self.sta == "flashing":
            self.speed = 20
        if self.sta == "snail":
            self.speed = 5
        if self.up == True and self.posy < 550:
            self.posy += self.speed
        if self.down == True and self.posy > 0:
            self.posy -= self.speed
        if self.right == True and self.posx < 750:
            self.posx += self.speed
        if self.left == True and self.posx > 0:
            self.posx -= self.speed
        display.blit(shipim, (self.posx, self.posy))


class explodeing(object):
    def __init__(self, x, y, ip):
        self.x = x
        self.y = y
        self.ip = ip
        self.para = -1

    def explodeit(self):
        if self.ip == 1:
            try:
                display.blit(explodelista[self.para], (self.x, self.y))
            except:
                pass
        if self.ip == 2:
            try:
                display.blit(explodelistb[self.para], (self.x, self.y))
            except:
                pass


class bulletob(object):
    def __init__(self, fireposx, fireposy, typa):
        self.fireposx = fireposx
        self.fireposy = fireposy
        self.typa = typa

    def fireit(self, color):
        if self.typa == "normal":
            display.blit(bbup, (self.fireposx, self.fireposy))
        if self.typa == "noinar":
            display.blit(grenade, (self.fireposx, self.fireposy))
        if self.typa == "blast":
            display.blit(blast, (self.fireposx, self.fireposy))


class maou(object):
    def __init__(self, fposx, fposy, obtype):
        self.fposx = fposx
        self.fposy = fposy
        self.obtype = obtype

    def umaou(self):
        if self.obtype == "ob":
            display.blit(fireball, (self.fposx+17, self.fposy))
        elif self.obtype == "flashing":
            display.blit(flashi, (self.fposx+17, self.fposy))
        elif self.obtype == "snail":
            display.blit(snail, (self.fposx+17, self.fposy))
        elif self.obtype == "hp":
            display.blit(aid, (self.fposx+17, self.fposy))
will=0

class danga:
    def __init__(self):
        self.posx = 300
        self.posy = 25
        self.left = True
        self.right = False

    def move(self):
        if self.right == True:
            self.posx += 8
        elif self.left == True:
            self.posx -= 8
        if self.posx <= 0:
            self.right = True
            self.left = False
        elif self.posx >= 750:
            self.left = True
            self.right = False
        display.blit(dangar, (self.posx, self.posy))

    def fire(self):
        for enemyi in enemyis:
            if enemyi.eposx in range(self.posx, self.posx+25) or enemyi.eposx+25 in range(self.posx, self.posx+25):
                explode.append(explodeing(enemyi.eposx, enemyi.eposy, 1))
                adi.play()
                enemy.newpos(enemyi)
            if ship.posx in range(self.posx, self.posx+25) and ship.gar == 1 or ship.posx+25 in range(self.posx, self.posx+25) and ship.gar == 1 or ship.posx+12 in range(self.posx, self.posx+25) and ship.gar == 1:
                ship.gar -= 1
                ship.health -= 5
                adi.play()
                explode.append(explodeing(ship.posx, ship.posy, 1))
        display.blit(dangarlaser, (self.posx, self.posy))
class special(object):
    #to b
    pass

class enemy(object):
    def __init__(self, eposx, eposy, renum):
        self.eposx = eposx
        self.eposy = eposy
        self.renum = renum
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.par = 1

    def movee(self):
        if self.left == True:
            self.eposx -= enemyspeed
        elif self.right == True:
            self.eposx += enemyspeed
        elif self.up == True:
            self.eposy -= enemyspeed
        elif self.down == True:
            self.eposy += enemyspeed
        if self.eposx < 0:
            self.left = False
            self.right = True
            #self.up=False
            #self.down=False
        if self.eposx > 750:
            self.left = True
            self.right = False
            #self.up=False
            #self.down=False
        if self.eposy < 0:
            #self.left=False
            #self.right=False
            self.up = False
            self.down = True
        if self.eposy > 350:
            #self.left=False
            #self.right=False
            self.up = True
            self.down = False
        display.blit(alien, (self.eposx, self.eposy))

    def newpos(self):
        self.par = 1
        x = random.randint(50, 750)
        y = random.randint(50, 350)
        self.eposx = x
        self.eposy = y


class homing(object):
    def __init__(self, eposx, eposy, bposx, bposy):
        self.eposx = eposx
        self.eposy = eposy
        self.bposy = bposy
        self.bposx = bposx

    def updatemi(self):
        try:
            sx = self.eposx-self.bposx
            sy = self.eposy-self.bposy
            vy = 4
            vx = (sx*vy)/sy
            self.bposy -= vy
            self.bposx -= vx
            display.blit(smallbomb, (self.bposx, self.bposy))
        except:
            pass
dagas=[]
for i in range(0,dangacount):
    dagas.append(danga())


for dange in dagas:
    dange.posx=random.randint(0,725)
ils = 0
ship = watashi(400, 500, "normal")
watashi.draw(ship)
for i in range(0, enemycount):
    disp = random.randint(1, 2)
    enemyis.append(enemy(50, 50, i))
    if disp == 1:
        enemyis[i].left = True
    elif disp == 2:
        enemyis[i].right = True
    elif disp == 3:
        enemyis[i].up = True
    elif disp == 4:
        enemyis[i].down = True
    enemy.newpos(enemyis[i])

while gameover == False:
    cur = pygame.mouse.get_pos()
    isit = pygame.mouse.get_pressed()
    if isit[0] == 1:
            if cur[0] in range(0, 25) and cur[1] in range(0, 25):
                pause = True
            if cur[0] in range(773, 798) and cur[1] in range(0, 25):
                pause = False
                menu = True
                gameover = False
    display.blit(pbut, (0, 0))
    while menu == True:
        isit = pygame.mouse.get_pressed()
        pygame.event.get()
        display.fill(green)
        cur = pygame.mouse.get_pos()
        cont = font.render("STARTGAME", 20, (255, 255, 255))
        stop = font.render("QUIT", 20, (255, 255, 255))
        pygame.draw.rect(display, blue, (325, 200, 150, 50))
        pygame.draw.rect(display, red, (325, 300, 150, 50))
        display.blit(cont, (350, 210))
        display.blit(stop, (380, 310))
        if isit[0] == 1:
            if cur[0] in range(325, 470) and cur[1] in range(200, 250):
                print("cont")
                menu = False
            if cur[0] in range(30, 470) and cur[1] in range(300, 350):
                print("stop")
                menu = False
                gameover = True
            else:
                pass
        else:
            pass
        pygame.display.update()
        respeed.tick(10)
    while pause == True:
        respeed.tick(10)
        pygame.event.get()
        isits = pygame.mouse.get_pressed()
        curs = pygame.mouse.get_pos()
        display.blit(plbut, (0, 0))
        pygame.display.update()
        if isits[0] == 1:
            if cur[0] in range(0, 25) and curs[1] in range(0, 25):
                pause = False
                pass
            if cur[0] in range(773, 798) and cur[1] in range(0, 25):
                print("pause")
            else:
                pass

    for dange in dagas:
        danga.move(dange)
    clock += 50
    if clock not in range(dangatime, dangatime+500):
        ship.gar = 1
        will = random.randint(0, dangacount-1)
    elif clock in range(dangatime, dangatime+500):
        danga.fire(dagas[will])
        if clock >= dangatime+500:
            dangatime = random.randint(0, 2000)
    

    if clock == 1000 and power <= 150:
        print(gamefps)
        power += 50*2.5 * 1/gamefps
    if clock == 2500:
        ship.sta = "normal"
        clock = 0
    scoreshow = font.render("score "+str(score), 1, (255, 0, 0))
    hps = font.render("HP "+str(ship.health), 1, (255, 0, 0))
    energy = font.render("Energy "+str(power)+"%", 1, (255, 0, 0))
    display.blit(energy, (515, 5))
    display.blit(scoreshow, (695, 5))
    display.blit(hps, (630, 5))
    display.blit(plbut, (700, 600))
    display.blit(menubut, (773, 5))
    pygame.display.update()
    display.fill(white)
    display.blit(bg, (0, 0))
    respeed.tick(gamefps)
    #if score < 0:
    #gameover = True
    if blasta == True:
        blastt += 1
        display.blit(blast, (ship.posx+14, ship.posy-650))
        if blastt == 100:
            blasta = False
            blastt = 0

    for maio in maoue:
        maio.fposy += 15
        maou.umaou(maio)
        if maio.fposy > 600 or (maio.fposy in range(ship.posy-25, ship.posy+25) and maio.fposx in range(ship.posx-20, ship.posx+20)):
            if (maio.fposy in range(ship.posy-25, ship.posy+25) and maio.fposx in range(ship.posx-25, ship.posx+25)):
                if maio.obtype == "flashing" and ship.sta == "normal":
                    ship.sta = "flashing"
                    clock = 0

                elif maio.obtype == "snail" and ship.sta == "normal":
                    ship.sta = "snail"
                    clock = 0

                elif ship.sta == "snail" and maio.obtype == "flashing":
                    ship.sta = "normal"

                elif ship.sta == "flashing" and maio.obtype == "snail":
                    ship.sta = "normal"

                elif maio.obtype == "hp":
                    ship.health += 1
                    ship.sta = "normal"

                elif maio.obtype == "ob":
                    ship.health -= 1
                    hitme.play()
                    explode.append(explodeing(ship.posx, ship.posy, 2))
                    try:
                        maoue.pop(maoue.index(maio))
                    except:
                        pass
            try:
                maoue.pop(maoue.index(maio))
            except:
                pass
        else:
            pass
    
    for enemyi in enemyis:
        '''
        if aimbot == True:
            if ship.posx in range(enemyi.eposx, enemyi.eposx+50) and enemyi.par == 1:
                bullets.append(bulletob(ship.posx, ship.posy))
                enemyi.par = 0
        '''
        enemy.movee(enemyi)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ship.down = False
                ship.up = True
                ship.left = False
                ship.right = False
            elif event.key == pygame.K_UP:
                ship.up = False
                ship.down = True
                ship.left = False
                ship.right = False
            elif event.key == pygame.K_RIGHT:
                ship.right = True
                ship.up = False
                ship.down = False
                ship.left = False
            elif event.key == pygame.K_LEFT:
                ship.left = True
                ship.up = False
                ship.down = False
                ship.right = False
            elif event.key == pygame.K_SPACE:
                if len(bullets) < 5:
                    bso.play()
                    bullets.append(bulletob(ship.posx+20, ship.posy, "normal"))
                '''
                phew = random.randint(0,100)
                ynr = random.randint(0,len(enemyis))
                if phew in range(0,100):
                    try:
                        missile.append(homing(enemyis[ynr].eposx,enemyis[ynr].eposy,ship.posx,ship.posy))
                    except:
                        pass
                '''
            elif event.key == pygame.K_LSHIFT:
                if blasta == False and power >= 150:
                    print("blast")
                    power -= 150
                    blasta = True
            elif event.key == pygame.K_f:
                if power >=10:
                    print("noinar")
                    power-=10
                    bullets.append(bulletob(ship.posx+20, ship.posy, "noinar"))
            elif event.key == pygame.QUIT:
                print("over")
                sys.exit(1)
                pygame.quit()
                gameover = True
    if power > 150:
        power = 150
    for missil in missile:
        homing.updatemi(missil)
    for bullet in bullets:
        for enemyi in enemyis:
            if bullet.typa=="noinar":
                if enemyi.eposx in range(bullet.fireposx,bullet.fireposx+192) and enemyi.eposy in range(bullet.fireposy,bullet.fireposy+192):
                    try:
                        explode.append(explodeing(enemyi.eposx, enemyi.eposy, 1))
                        adi.play()
                        bullets.pop(bullets.index(bullet))
                        disp = random.randint(1, 2)
                        if disp == 1:
                            enemyi.left = True
                            enemyi.right = False
                            enemyi.up = False
                            enemyi.down = False
                        elif disp == 2:
                            enemyi.left = False
                            enemyi.right = True
                            enemyi.up = False
                            enemyi.down = False
                        elif disp == 3:
                            enemyi.left = False
                            enemyi.right = False
                            enemyi.up = True
                            enemyi.down = False
                        elif disp == 4:
                            enemyi.left = False
                            enemyi.right = False
                            enemyi.up = False
                            enemyi.down = True
                        enemy.newpos(enemyi)
                        score += 1
                    except:
                        pass
            if bullet.fireposy <= 0 or (bullet.fireposy in range(enemyi.eposy-25, enemyi.eposy+25) and bullet.fireposx in range(enemyi.eposx-25, enemyi.eposx+25)) and bullet.typa!= "noinar":
                try:
                    explode.append(explodeing(enemyi.eposx, enemyi.eposy, 1))
                    adi.play()
                    bullets.pop(bullets.index(bullet))
                    disp = random.randint(1, 2)
                    if disp == 1:
                        enemyi.left = True
                        enemyi.right = False
                        enemyi.up = False
                        enemyi.down = False
                    elif disp == 2:
                        enemyi.left = False
                        enemyi.right = True
                        enemyi.up = False
                        enemyi.down = False
                    elif disp == 3:
                        enemyi.left = False
                        enemyi.right = False
                        enemyi.up = True
                        enemyi.down = False
                    elif disp == 4:
                        enemyi.left = False
                        enemyi.right = False
                        enemyi.up = False
                        enemyi.down = True
                    enemy.newpos(enemyi)
                    score += 1
                except:
                    pass
    '''
    for homissile in missile:
        for enemyi in enemyis:
            if homissile.bposx in range(enemyi.eposx-25, enemyi.eposx+25) and homissile.eposy in range(enemyi.eposy, enemyi.eposy+25):
                try:
                    print("hit")
                    explode.append(explodeing(enemyi.eposx, enemyi.eposy, 1))
                    adi.play()
                    missile.pop(missile.index(homissile))
                    enemy.newpos(enemyi)
                except:
                    pass
    '''
    for enemyi in enemyis:
        if blasta == True:
            if enemyi.eposx+25 in range(ship.posx+14, ship.posx+28) or enemyi.eposx+50 in range(ship.posx+14, ship.posx+28):
                try:
                    explode.append(explodeing(enemyi.eposx, enemyi.eposy, 1))
                    enemy.newpos(enemyi)
                    adi.play()
                    disp = random.randint(1, 2)
                    if disp == 1:
                        enemyi.left = True
                        enemyi.right = False
                        enemyi.up = False
                        enemyi.down = False
                    elif disp == 2:
                        enemyi.left = False
                        enemyi.right = True
                        enemyi.up = False
                        enemyi.down = False
                    elif disp == 3:
                        enemyi.left = False
                        enemyi.right = False
                        enemyi.up = True
                        enemyi.down = False
                    elif disp == 4:
                        enemyi.left = False
                        enemyi.right = False
                        enemyi.up = False
                        enemyi.down = True
                    score += 1
                except:
                    pass
        '''
        if aimbot == True:
            if ship.posx+20 in range(enemyi.eposx, enemyi.eposx+50) and enemyi.par == 1:
                bullets.append(bulletob(enemyi.eposx, ship.posy))
                enemyi.par = 0
        '''
        if len(maoue) < 10:
            yn = random.randint(1, 100)
            if yn == 1:
                maoue.append(maou(enemyi.eposx, enemyi.eposy, "flashing"))
            if yn == 2:
                maoue.append(maou(enemyi.eposx, enemyi.eposy, "snail"))
            if ship.health < 80 and yn == 3:
                maoue.append(maou(enemyi.eposx, enemyi.eposy, "hp"))
            if yn in range(60, 80):
                maoue.append(maou(enemyi.eposx, enemyi.eposy, "ob"))
    for bullet in bullets:
        bullet.fireposy -= 20
        bulletob.fireit(bullet, (255, 0, 0))
        if bullet.fireposy <= 0:
            bullets.pop(bullets.index(bullet))
    for exp in explode:
        if exp.para == 9:
            explode.pop(explode.index(exp))
        exp.para += 1
        explodeing.explodeit(exp)
    watashi.draw(ship)
pygame.quit()
sys.exit(1)