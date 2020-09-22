import pygame
x=pygame.init()
# creating game window
gameWindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("My first game")

#game specific variables
exit_game=False
game_over=False

#creating a game loop

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("Right")


pygame.quit()
quit()