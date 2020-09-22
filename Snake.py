import pygame
import random
import os
pygame.init()
pygame.mixer.init()

#colours
white=(225,225,225)
red=(225,0,0)
black=(0,0,0)

#game Window
gameWindow=pygame.display.set_mode((900,600))

# backgroundimage
bgimg=pygame.image.load("bimg.png")
bgimg=pygame.transform.scale(bgimg ,(900,600)).convert_alpha()

#game title
pygame.display.set_caption("Snakes With Sanskar")
pygame.display.update()

# with open ("highscore.txt","r") as f:
#     highscore=f.read()

font=pygame.font.SysFont(None,55)
clock=pygame.time.Clock()


def text_screen(text,colour,x,y):
    screen_text= font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,black,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((230,200,100))
        text_screen("Welcome to Python Game", black,260,250)
        text_screen("Press Space To Continue", black, 250, 290)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load("bgm.mp3")
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)
    #creating a game winndow and game loop
def gameloop():
    # game specific variables
    exit_game = False
    game_quit = False
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 20
    fps = 60
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, 900 / 2)
    food_y = random.randint(20, 600 / 2)
    score = 0
    snk_list = []
    snk_length = 1

    # creating high score file if not exist
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill((230,200,100))
            text_screen("Game Over! Press enter to continue",red,100,250)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0

                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0

            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                # print("Score=",score*10)
                food_x = random.randint(20, 900 / 2)
                food_y = random.randint(20, 600 / 2)
                snk_length+=5
                if score>int(highscore):
                    highscore=score

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen ("Score: " + str(score), red, 5, 5)
            text_screen("Highscore: " + str(highscore), red, 628, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>600:
                game_over=True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()


            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()