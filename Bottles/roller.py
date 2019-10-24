import time
import json
import os
import pygame
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
Brack=[0,0,0]
White=[255,255,255]
Green=[0,255,0]
width=pygame.display.Info().current_w
height=pygame.display.Info().current_h
height0=int((height-117)/3)
size=(width-67)/20
os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" % (67,height0*2+87)
screen = pygame.display.set_mode((width-67,height0))
screen.fill(Brack)
pygame.display.update()
icon0={'0':'cgq0.jpg','1':'cgq1.jpg'}
icon1={'0':'dj0.jpg','1':'dj1.jpg'}
number0=["传感器0","传感器1","传感器2","传感器3","传感器4","传感器5","传感器6","传感器7"]
number1=["交流电机0","交流电机1","直流电机2","直流电机3","直流电机4","直流电机5","直流电机6"]
number2=["夹紧气缸","移动气缸","夹紧气缸","移动气缸","阻挡气缸","升降气缸","升降气缸(出)"]
pygame.draw.rect(screen,Green,[0,290,size*9,110],5)
pygame.draw.rect(screen,Green,[size*9+10,290,size*4-5,110],5)
pygame.draw.rect(screen,Green,[size*13+15,290,size*4,110],5)
pygame.draw.rect(screen,Green,[size*17+25,290,size*2,110],5)
pygame.draw.rect(screen,Green,[size*11,90,size*5+10,110],5)
pygame.draw.rect(screen,Green,[size*7,90,size*4-10,110],5)
pygame.draw.rect(screen,Green,[size*3-10,90,size*4,110],5)
pygame.display.update()
def Icon_cgq(num,x,y,a):
    img=pygame.image.load(icon0[a])
    img=pygame.transform.smoothscale(img,(int(size),50))
    screen.blit(img,(x,y))
    text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",18)
    text_fmt0=text.render(number0[num],3,White)
    screen.blit(text_fmt0,(x-5,y-25))
    pygame.display.update()
def Icon_dj(num,x,y,a):
    img=pygame.image.load(icon1[a])
    img=pygame.transform.smoothscale(img,(int(size),50))
    screen.blit(img,(x,y))
    text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",18)
    text_fmt0=text.render(number1[num],3,White)
    screen.blit(text_fmt0,(x,y-20))
    pygame.display.update()
def Icon_qg(num,x,y):
    img=pygame.image.load('qg0.jpg')
    img=pygame.transform.smoothscale(img,(int(size),50))
    screen.blit(img,(x,y))
    text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",18)
    text_fmt0=text.render(number2[num],3,White)
    screen.blit(text_fmt0,(x,y-25))
    pygame.display.update()
if __name__ == '__main__':
    while True:
        time.sleep(1)
        response0=urllib.request.urlopen('http://localhost:5000/s/status/')
        html0=response0.read()
        text0=json.loads(html0)
        response1=urllib.request.urlopen('http://localhost:5000/n/status/')
        html1=response1.read()
        text1=json.loads(html1)
        A0=[[0,size,329,text0['sensor0']],[1,size*5,329,text0['sensor1']],[2,size*15-10,329,text0['sensor2']],[3,size*18+20,329,text0['sensor3']],[4,size*18+20,129,text1['sensor4']],[5,size*15-10,129,text1['sensor5']],[6,size*11+10,129,text1['sensor6']],[7,size*3,129,text1['sensor7']]]
        A1=[[0,size*8+10,429,text0['motor0']],[1,size*12,429,text0['motor1']],[2,size*14,429,text0['motor2']],[3,size*17+30,429,text0['motor3']],[4,size*13,20,text1['motor4']],[5,size*10,20,text1['motor5']],[6,size*6,20,text1['motor6']]]
        A2=[[0,0,429],[1,size*2,519],[2,size*4,429],[3,size*4,519],[4,size*7-20,429],[5,size*9+20,329],[6,size*16+10,329]]
        for i in A0:
            Icon_cgq(i[0],i[1],i[2],i[3])
        for v in A1:
            Icon_dj(v[0],v[1],v[2],v[3])
            if int(v[3])==1 and 0<=v[0]<=3:
                img=pygame.image.load('jt0.jpg')
                img=pygame.transform.smoothscale(img,(int(size)-20,40))
                screen.blit(img,(v[1],v[2]-100))
            elif int(v[3])==1 and 4<=v[0]<=6:
                img=pygame.image.load('jt1.jpg')
                img=pygame.transform.smoothscale(img,(int(size)-20,40))
                screen.blit(img,(v[1],v[2]+110))
            else:
                pygame.draw.rect(screen,Brack,[v[1],v[2]-100,int(size)-20,40],0)
                pygame.draw.rect(screen,Brack,[v[1],v[2]+110,int(size)-20,40],0)
        for n in A2:
            Icon_qg(n[0],n[1],n[2])
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            elif event.type == QUIT:
                exit()
