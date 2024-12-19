import pygame 
import random 
import math 

#constants

fps = 60
width,height = 1000,800
paddle_width = 10
paddle_height = 150
background_color = (0,0,0)
paddle_color = (255,255,255)
paddle1_x = width - paddle_width*4 #960
paddle1_y = height//2-paddle_height//2 
paddle2_x = paddle_width*3
paddle2_y = height//2-paddle_height//2
ball_side = 10
x = width//2-ball_side//2
ball_color = paddle_color
paddles_speed = 10
score_right = 0
score_left = 0
ball_speed = 7
ball_x = x
ball_y = random.randint(0,height)
ball_x_speed = 7
ball_y_speed = 7
prev_ball_y = 0
prev_ball_x=0
x1,x2,y2,x3,x4= 1,1,1,1,1   
y1 = 1
pause = False


#pygame starts

pygame.init()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong!")
clock = pygame.time.Clock()


#pygame fonts

pygame.font.init()
font1 = pygame.font.Font(None,50)  
font2 = pygame.font.Font(None,50)
font3 = pygame.font.Font(None,75)


#game loop

run = True
while run:
    clock.tick(fps)
    
    #getting key info
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause

    window.fill(background_color)

    #drawing the paddles and the ball
    pygame.draw.rect(window,paddle_color,(paddle1_x,paddle1_y,paddle_width,paddle_height))
    pygame.draw.rect(window,paddle_color,(paddle2_x,paddle2_y,paddle_width,paddle_height))
    pygame.draw.rect(window,ball_color,(ball_x,ball_y,ball_side,ball_side))

    #drawing the middle borders - 

    for i in range(0,height,ball_side*2):
        pygame.draw.rect(window,ball_color,(x,i,ball_side,ball_side))

    #paddle movement (right)
    if not pause:
        if key[pygame.K_UP] and paddle1_y > 0:
            paddle1_y-=paddles_speed
        if key[pygame.K_DOWN] and paddle1_y <= height-paddle_height:
            paddle1_y+=paddles_speed
    

    #paddle movement (left)
       
        if paddle2_y > ball_y+ball_side and paddle2_y>=0:
            paddle2_y -= paddles_speed
        if paddle2_y+paddle_height < ball_y and paddle2_y+paddle_height<=height:
            paddle2_y+= paddles_speed
    
   #****************ball movement/generation******************
    
    #*****paddle 1*****-
    if ball_x+ball_side >= paddle1_x+paddle_width//2 and paddle1_y<=ball_y<=paddle1_y+paddle_height:
          ball_x_speed*=-1 

   #**********left paddle***********
    if ball_x <= paddle2_x+paddle_width//2 and paddle2_y<=ball_y<=paddle2_y+paddle_height:  
         ball_x_speed*=-1 
         
    #borders
    if ball_y+ball_side >= height or ball_y<= 0:
        ball_y_speed*=-1

   #regenerating after it crosses vertical borders

    if ball_x > width:
        score_left += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_x_speed = ball_speed*random.choice([1,-1])
        ball_y_speed = ball_speed*random.choice([1,-1])
    if ball_x + ball_side < 0:
        score_right += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_x_speed = ball_speed*random.choice([1,-1])
        ball_y_speed = ball_speed*random.choice([1,-1])



    if not pause:   
        # updating the ball's position
        ball_x += ball_x_speed
        ball_y += ball_y_speed

    #score font 
    right = font1.render((f'Score: {score_right}'),True,(255,255,255))
    window.blit(right, (800,100))

    left = font2.render((f'Score: {score_left}'),True,(255,255,255))
    window.blit(left, (200,100))

    if pause:
        pause_text = font3.render((f'PAUSED'),True,(255,255,255))
        window.blit(pause_text,(400,300))
   
    pygame.display.update()


pygame.quit()