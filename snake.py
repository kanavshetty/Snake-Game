import pygame #importing the pygame module
import random
import time

pygame.init()                                # Initializing the pygame game environment

screen_height = 500
screen_width = 500
run = True
snake_x_coordinates, snake_y_coordinates = 250,250 # Initializing the starting coordinates of the snake in the center of the screen
change_in_snake_x_coordinates, change_in_snake_y_coordinates = 10, 0
clock = pygame.time.Clock()
food_x_coordiantes, food_y_coordinates = random.randrange(0,screen_width)//10*10, random.randrange(0,screen_height)//10*10
snake_body_list_of_coordinates = [(snake_x_coordinates,snake_y_coordinates)]
game_over = False
font = pygame.font.SysFont("calibri",25)
                               
game_screen = pygame.display.set_mode((screen_width,screen_height)) #Initialized the game screen with dimensions 800x800
pygame.display.set_caption("Snake Game")     # Set the title of the game

def snake():
    global snake_x_coordinates, snake_y_coordinates,food_x_coordiantes,food_y_coordinates, game_over
    snake_x_coordinates = (snake_x_coordinates + change_in_snake_x_coordinates) % screen_width
    snake_y_coordinates = (snake_y_coordinates + change_in_snake_y_coordinates) % screen_height


    snake_body_list_of_coordinates.append((snake_x_coordinates,snake_y_coordinates))
    
    if(snake_body_list_of_coordinates[-1] in snake_body_list_of_coordinates[0:-1]):
        game_over = True
        return

    if (food_x_coordiantes == snake_x_coordinates and food_y_coordinates == snake_y_coordinates):
        while((food_x_coordiantes, food_y_coordinates) in snake_body_list_of_coordinates):
            food_x_coordiantes, food_y_coordinates = random.randrange(0,screen_width)//10*10, random.randrange(0,screen_height)//10*10
    else:
        del snake_body_list_of_coordinates[0]

    
    game_screen.fill((173,204,96))
    score = font.render("Score: " + str(len(snake_body_list_of_coordinates)), True, (255,255,0))
    game_screen.blit(score,[0,0])
    pygame.draw.rect(game_screen,(255,0,0),[food_x_coordiantes,food_y_coordinates,10,10])
    for (i,j) in snake_body_list_of_coordinates:
        pygame.draw.rect(game_screen,(43,51,24),[i,j,10,10])
    pygame.display.update()

while run:                                   # We are setting the game loop here
    if(game_over):
        game_screen.fill((0,0,0))
        score = font.render("Score: " + str(len(snake_body_list_of_coordinates)), True, (255,255,0))
        game_screen.blit(score,[0,0])
        msg = font.render("GAME OVER!", True, (255,255,255))
        game_screen.blit(msg,[screen_width/3,screen_height/2])
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        quit()
    events = pygame.event.get()              # Each event like a mouse click is stored in this list
    for event in events:                     # Iterating through each event in the list
        if(event.type == pygame.QUIT):       # If the event is closing the game window
            pygame.quit()                    # Closing the pygame game environment
            quit()                           # Exiting the program
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_w):
                if(change_in_snake_y_coordinates != 10):
                    change_in_snake_y_coordinates = -10
                    change_in_snake_x_coordinates = 0
            elif(event.key == pygame.K_s):
                if(change_in_snake_y_coordinates != -10):
                    change_in_snake_y_coordinates = 10
                    change_in_snake_x_coordinates = 0
            elif(event.key == pygame.K_a):
                if(change_in_snake_x_coordinates != 10):
                    change_in_snake_x_coordinates = -10
                    change_in_snake_y_coordinates = 0
            elif(event.key == pygame.K_d):
                if(change_in_snake_x_coordinates != -10):
                    change_in_snake_x_coordinates = 10
                    change_in_snake_y_coordinates = 0
            else:
                continue
            snake()
    if(not events):
        snake()    
    clock.tick(20)

