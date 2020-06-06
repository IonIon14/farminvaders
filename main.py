import pygame
import random
import os
import math
import os
import sys

current_diretory=os.getcwd()
def gameplay():
    pygame.init()#in inceput de orice joc(initialize pygame)
    background=pygame.image.load('ferma.png')
    class Player:
        def __init__(self,posX,posY,image):
            self.posX=posX
            self.posY=posY
            self.image=image
        def character(self):
            screen.blit(self.image, (self.posX, self.posY))
    class Enemy(Player):
        def erase_enemy(self):
            global background
            screen.blit(background, (0, 0))
            screen.blit(enemy_image, (200,300))
            pygame.display.update()
        def collision_on_player(self,enemyX,enemyY):
            self.x=enemyX
            self.y=enemyY
            distance = math.sqrt(math.pow((self.x - Player(player_posX,player_posY,player_image).posX), 2) + math.pow((self.y - Player(player_posX,player_posY,player_image).posY), 2))
            if distance<70:
                return True
            else:
                return False
    class Bullet(Enemy):
        def __init__(self,bullet_posX,bullet_posY,bullet_img):
            self.bullet_posX=bullet_posX
            self.bullet_posY=bullet_posY
            self.image=bullet_img
            Enemy.__init__(self,enemy_posX,enemy_posY,enemy_image)
        def isCollision(self,posX,posY):
            Enemy(enemy_posX,enemy_posY,enemy_image).posX=posX
            Enemy(enemy_posX, enemy_posY, enemy_image).posY = posY
            distance = math.sqrt(math.pow((Enemy(enemy_posX,enemy_posY,enemy_posY).posX - self.bullet_posX), 2) + math.pow((Enemy(enemy_posX,enemy_posY,enemy_image).posY - self.bullet_posY), 2))
            if distance < 150:
                return True
            else:
                return False
        def arm_shooting(self):
            global bullet_state
            bullet_state = 'fire'
            screen.blit(bullet_img, (self.bullet_posX + 16, self.bullet_posY - 10))
    #creeam ecranul
    width=800
    height=560
    screen=pygame.display.set_mode((width,height))
    #loop pentru a tine fereasta deschisa pana la un anumit event(game loop)
    distance=[0,70,140,210,280,350]
    #Titlu si iconita
    pygame.display.set_caption("Farm Invaders")
    icon=pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)
    #Player
    player_image=pygame.image.load('player.png')
    player_posX=370
    player_posY=480
    playerX_change=0
    playerY_change=0
    player=Player(player_posX,player_posY,player_image)


    #Enemy
    enemy_image=pygame.image.load('enemy.png')
    enemy_posX=370
    enemy_posY=30
    enemyX_change=3
    enemyY_change=0.05
    enemy=Enemy(enemy_posX,enemy_posY,enemy_image)
    score_value=0
    scor_final=[]
    enemy1=[]
    enemy2=[]
    enemy3=[]
    enemy4=[]
    col_1=[]
    col_2=[]
    col_3=[]
    col_4=[]
    font=pygame.font.Font('freesansbold.ttf',32)
    textX=10
    textY=10
    game_over=pygame.font.Font('freesansbold.ttf',50)
    def show_score(x,y):
        score=font.render("Score :"+str(score_value),True,(200,255,100))
        screen.blit(score,(x,y))
    def game_over_text(x,y):
        go = game_over.render("Game over!", True, (255,0,0))
        screen.blit(go, (x, y))

    #Bullet

    #Ready-you can t see the bullet on the screen
    #Fire-bullet is currently moving
    bullet_img=pygame.image.load('easter-egg.png')
    bullet_posX=0
    bullet_posY=480
    bulletX_change=0
    bulletY_change=10
    bullet=Bullet(bullet_posX,bullet_posY,bullet_img)
    bullet_state='ready'
    enemies=[]
    collision=[]
    collision1=[]
    collision2=[]
    collision3=[]
    distance_between_enemy_and_player = []
    pygame.mixer.music.load('song.wav')
    running=True
    while running:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        #pentru Oy,daca scadem merge in sus,altfel merge in jos
        #pozitia playerului pe axa Ox se incrementeaza continuu in while,facand playerul sa se simte continuu in dreapta
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                print("A keystroke is pressed")# verifica daca o tasta este apasata
                if event.key==pygame.K_LEFT:
                    print("Left arrow is pressed!")
                    playerX_change-=2
                if event.key==pygame.K_RIGHT:
                    print("Right arrow is pressed!")
                    playerX_change+=2
                if event.key==pygame.K_UP:
                    print("Up arrow is pressed!")
                    playerY_change-=2
                if event.key==pygame.K_DOWN:
                    print("Down arrow is pressed!")
                    playerY_change+=2
                if event.key==pygame.K_SPACE:
                    print("Spacebar is pressed!")
                    if bullet_state=='ready':
                        bullet.arm_shooting()
                        bullet.bullet_posX=player.posX

            if event.type==pygame.KEYUP:
                print("A keystroke is released")
                if event.key==pygame.K_LEFT:
                    print("Left arrow is released!")
                    playerX_change=0
                if event.key==pygame.K_RIGHT:
                    print("Right arrow is released!")
                    playerX_change=0
                if event.key==pygame.K_UP:
                    print("Up arrow is released!")
                    playerY_change=0
                if event.key==pygame.K_DOWN:
                    print("Down arrow is released!")
                    playerY_change=0
        #ceva
        #RBG-Red,Green,Blue
        player.character()
        player.posX+=playerX_change
        player.posY+=playerY_change

        if player.posX<0 or player.posX>740 or player.posY<0 or player.posY>495:
            playerX_change=0
            playerY_change=0
        enemy.posX+= enemyX_change
        enemy.posY += enemyY_change

        for i in range(0,len(distance)):
            enemy1.append(Enemy(enemy.posX+distance[i], enemy.posY,enemy_image))
            enemy2.append(Enemy(enemy.posX-distance[i],enemy.posY,enemy_image))
            enemy3.append(Enemy(enemy.posX+distance[i],enemy.posY+80,enemy_image))
            enemy4.append(Enemy(enemy.posX-distance[i],enemy.posY+80,enemy_image))
        for i in range(0,len(distance)):
            enemy1[i]=Enemy(enemy.posX+distance[i], enemy.posY,enemy_image)
            enemy2[i]=Enemy(enemy.posX-distance[i], enemy.posY,enemy_image)
            enemy3[i]=Enemy(enemy.posX+distance[i], enemy.posY+80,enemy_image)
            enemy4[i]=Enemy(enemy.posX-distance[i], enemy.posY+80,enemy_image)
            enemy1[i].character()
            enemy2[i].character()
            enemy3[i].character()
            enemy4[i].character()
            #apelam functia mereu dupa screen.fill
        for i in range(0,len(distance)):
            if enemy1[i].collision_on_player(enemy1[i].posX,enemy1[i].posY)==True or enemy2[i].collision_on_player(enemy2[i].posX,enemy2[i].posY)==True or enemy3[i].collision_on_player(enemy3[i].posX,enemy3[i].posY)==True or enemy4[i].collision_on_player(enemy4[i].posX,enemy4[i].posY)==True:
                for j in range(0,len(distance)):
                    enemy1[j].posY=2000
                    enemy2[j].posY = 2000
                    enemy3[j].posY = 2000
                    enemy4[j].posY = 2000
                game_over_text(250, 280)
                pygame.quit()
                pygame.time.delay(100)
                print("Scorul este:",score_value)
                break

            enemy1[i].posX += enemyX_change
            enemy1[i].posY += enemyY_change
            enemy2[i].posX += enemyX_change
            enemy2[i].posY += enemyY_change
            enemy3[i].posX += enemyX_change
            enemy3[i].posY += enemyY_change
            enemy4[i].posX += enemyX_change
            enemy4[i].posY += enemyY_change
            if enemy1[i].posX <= -500:
                enemyX_change = 3
                enemy1[i].posY += 10
                if enemy1[i].posY > height:
                    enemy1[i].posY = 0
            else:
                if enemy1[i].posX >= 2000:
                    enemyX_change = -3
                    enemy1[i].posY += 10
                    if enemy1[i].posY > height:
                        enemy1[i].posY = 0
            if enemy2[i].posX <= -500:
                enemyX_change = 3
                enemy2[i].posY += 10
                if enemy2[i].posY > height:
                    enemy2[i].posY = 0
            else:
                if enemy2[i].posX >= 2000:
                    enemyX_change = -3
                    enemy2[i].posY += 10
                    if enemy2[i].posY > height:
                        enemy2[i].posY = 0
            if enemy3[i].posX <= -500:
                enemyX_change = 3
                enemy3[i].posY += 10
                if enemy3[i].posY > height:
                    enemy3[i].posY = 0
            else:
                if enemy3[i].posX >= 2000:
                    enemyX_change = -3
                    enemy3[i].posY += 10
                    if enemy3[i].posY > height:
                        enemy3[i].posY = 0
            if enemy4[i].posX <= -500:
                enemyX_change = 3
                enemy4[i].posY += 10
                if enemy4[i].posY > height:
                    enemy4[i].posY = 0
            else:
                if enemy4[i].posX >= 740:
                    enemyX_change = -3
                    enemy4[i].posY += 10
                    if enemy4[i].posY > height:
                        enemy4[i].posY = 0

        if bullet_state=='fire':
            bullet.arm_shooting()
            bullet.bullet_posY-=bulletY_change
            if bullet.bullet_posY<=0:
                bullet_state='ready'
                bullet.bullet_posY=player.posY-10
        for i in range(0, len(distance)):
            collision.append(bullet.isCollision(enemy1[i].posX,enemy1[i].posY))
            collision1.append(bullet.isCollision(enemy2[i].posX,enemy2[i].posY))
            collision2.append(bullet.isCollision(enemy3[i].posX,enemy3[i].posY))
            collision3.append(bullet.isCollision(enemy4[i].posX,enemy4[i].posY))
        for i in range(0,len(distance)):
            collision[i]=bullet.isCollision(enemy1[i].posX,enemy1[i].posY)
            collision1[i]=bullet.isCollision(enemy2[i].posX,enemy2[i].posY)
            collision2[i]=bullet.isCollision(enemy3[i].posX,enemy3[i].posY)
            collision3[i]=bullet.isCollision(enemy4[i].posX,enemy4[i].posY)
        # ciocnirea cu toate tintele
            if collision[i]==True:
                bullet.bullet_posY=player.posY
                bullet_state='ready'
                print("collision!")
                score_value = score_value + 1
                enemy1[i].posX = 1200
                enemy1[i].posY = 1100
                enemy1[i].character()

        else:
                if collision1[i]==True:
                    bullet.bullet_posY = player.posY
                    bullet_state = 'ready'
                    print("collision!")
                    score_value = score_value + 1
                    enemy2[i].posX = 1200
                    enemy2[i].posY = 1100
                    enemy2[i].character()
                else:
                    if collision2[i]==True:
                        bullet.bullet_posY = player.posY
                        bullet_state = 'ready'
                        print("collision!")
                        score_value = score_value + 1
                        enemy3[i].posX = 1200
                        enemy3[i].posY = 1100
                        enemy3[i].character()
                    else:
                        if collision3[i]==True:
                            bullet.bullet_posY = player.posY
                            bullet_state = 'ready'
                            print("collision!")
                            score_value = score_value + 1
                            enemy4[i].posX = 1000
                            enemy4[i].posY = 2000
                            enemy4[i].character()
        show_score(textX,textY)
        pygame.display.update()

        #mereu trebuie sa existe aceasta linie de cod
