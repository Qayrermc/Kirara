import pygame as pg
import random
pg.font.init()
pg.init()

screen=pg.display.set_mode((400,400))
pg.display.set_caption('Snake')

#Var
score=hightscore=0
snake_part = 20
x=y=200
x_change=y_change=0
body_snake = []
length = 1

#Food

food_x=random.randint(0,19)*snake_part
food_y=random.randint(0,19)*snake_part
#Snake speed
clock=pg.time.Clock()
speed=3
#Def
def check_var():
    if x<0 or x>400 or y<0 or y>400 or (x,y) in body_snake[:-1]:
        return False
    return True
def text():
    font=pg.font.Font(None,32)
    if gameplay:
        score_txt=font.render(f'Score: {score}',True,(255,255,255))
        screen.blit(score_txt,(0,0))
        hscore_txt=font.render(f' High Score: {hightscore}',True,(255,255,255))
        screen.blit(hscore_txt,(170,0))
    else:
        screen.blit(f'nhấn space để chs lại',(0,0))

        

#Game
gameplay=True
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit
    for event in pg.event.get():
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_LEFT:
                x_change-=snake_part
                y_change=0
            elif event.key==pg.K_RIGHT:
                x_change=snake_part
                y_change=0
            elif event.key==pg.K_UP:
                x_change=0
                y_change-=snake_part
            elif event.key==pg.K_DOWN:
                x_change=0
                y_change==snake_part
            elif event.key==pg.K_SPACE:
                gameplay=True

    screen.fill((0,0,0))
    text()
    if gameplay:
        x+=x_change
            
        y+=y_change
        body_snake.append((x,y))
        if score>hightscore:
            hightscore == score
        if len(body_snake) < length:
            del body_snake[0]
        if x == food_x and y == food_y:

            length+=1
            food_x=random.randint(0,19)*snake_part
            food_y=random.randint(0,19)*snake_part
        for x,y in body_snake:
            pg.draw.rect(screen,(255,255,255),(x,y,snake_part,snake_part))
        pg.draw.rect(screen,(255,0,0),(food_x,food_y,snake_part,snake_part))
        clock.tick(speed)
        check_var
    else:
        score=0
        x=y=200
        x_change=y_change=0
        body_snake=[]
        length=1
    pg.display.update()