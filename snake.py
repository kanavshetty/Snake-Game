import pygame                                      #importing the pygame module
import random                                      #importing this module to make the food appear randomly
import time                                        #importing this module to control the sleep time of the program

pygame.init()                                      # Initializing the pygame game environment

#Initializing all the variables ahead of usign them later in the program

screen_height = 500
screen_width = 500
run = True 
snake_x_coordinates, snake_y_coordinates = 250,250 # Initializing the starting coordinates of the snake in the center of the screen
change_in_snake_x_coordinates, change_in_snake_y_coordinates = 10, 0 #Initializing the starting change in coordinates. So the snake starts intially moving to the right 1 unit at a time
clock = pygame.time.Clock()                        # This helps us to control the frame rate of the game
food_x_coordinates, food_y_coordinates = random.randrange(0,screen_width)//10*10, random.randrange(0,screen_height)//10*10  # Initialzing the rnadom coordiantes for the food of the snake
snake_body_list_of_coordinates = [(snake_x_coordinates,snake_y_coordinates)]     # We store the coordinates of each segment of the body of the snake in tuples like (x,y) and store these tuples in a list
game_over = False
font = pygame.font.SysFont("calibri",25)            # This is the font style and size with which I wanted my text displayed
                               
game_screen = pygame.display.set_mode((screen_width,screen_height)) #Initialized the game screen with dimensions 500x500
pygame.display.set_caption("Snake Game")     # Set the title of the game

def snake():
    global snake_x_coordinates, snake_y_coordinates,food_x_coordinates,food_y_coordinates, game_over    #Declaring that these variables are global so that the function knows that they have been previously declared and initialized and to use those values for the variable
    snake_x_coordinates = (snake_x_coordinates + change_in_snake_x_coordinates) % screen_width          # The whole reason I used the modulus fucntion was to make sure that if the snake left on end of the border of the game screen it would come out the other side. So if the snake leaves from the top, it comes back from the bottom of the screen towards the center of the game screen
    snake_y_coordinates = (snake_y_coordinates + change_in_snake_y_coordinates) % screen_height


    snake_body_list_of_coordinates.append((snake_x_coordinates,snake_y_coordinates))                    # We append each item in the list with the new x and y coordinates of snake segment to keep track of the changes
    
    if(snake_body_list_of_coordinates[-1] in snake_body_list_of_coordinates[0:-1]):                     # This if statement basically checks if the head of the snake which is the last element(coordinates) of the list, is already in the rest of the list. If it is already there in the list, this means that head of the snake has crashed into its body
        game_over = True                                                                                # If the snake has collided with its own body, the game obviously ends there.
        return

    if (food_x_coordinates == snake_x_coordinates and food_y_coordinates == snake_y_coordinates):       # This if statement checks if the snake eats the food or not by matching the coordinates of the head of the snake with the coordiantes of the food
        while((food_x_coordinates, food_y_coordinates) in snake_body_list_of_coordinates):              # This while statement means that while the coordinates of the food do nto belong in the list of the snake body parts, we can exit the loop and the food coordinates are stored in new random coordinates, but if our new rnadom coorinates happen to lie within the snake's bpdy parts, this while loop ensures that we do not exit the loop until we find coordiantes for the food where it does not belong in the body of the snake
            food_x_coordinates, food_y_coordinates = random.randrange(0,screen_width)//10*10, random.randrange(0,screen_height)//10*10
    else:
        del snake_body_list_of_coordinates[0]                                                           # After we have appended a new segment to the body of the snake based on the direction of the snake movement, we can now delete the frist segment which is the oldest segment since we do not need it and need to keep the size of the snake the same when it does not eat food. It is important to remember that this does not run when the snake eats food, and that is how the snake grows larger by 1 unit when it eats food.

    
    game_screen.fill((173,204,96))                                                                       # We fill the game screen with a green color
    score = font.render("Score: " + str(len(snake_body_list_of_coordinates)), True, (255,255,0))         # We render a score for the user based on the length of the snake
    game_screen.blit(score,[0,0])                                                                        # We print the score to the screen on the top left
    pygame.draw.rect(game_screen,(255,0,0),[food_x_coordinates,food_y_coordinates,10,10])                # We now draw a rectangle in red tp depict the food
    for (i,j) in snake_body_list_of_coordinates:                                                         # Now for each tuple in the list of snake segments, we draw a rectnagle of dark green color on the screen
        pygame.draw.rect(game_screen,(43,51,24),[i,j,10,10])
    pygame.display.update()                                                                              # To make the rectnagle we drew above actually apear on the game screen we need to call it

while run:                                   # We are setting the game loop here
    if(game_over):                           # This is the if statement for when game is over
        game_screen.fill((0,0,0))            # We fill the screen with a black color and a print the score and Game Over! message
        score = font.render("Score: " + str(len(snake_body_list_of_coordinates)), True, (255,255,0))
        game_screen.blit(score,[0,0])
        msg = font.render("GAME OVER!", True, (255,255,255))
        game_screen.blit(msg,[screen_width/3,screen_height/2])
        pygame.display.update()
        time.sleep(5)                       # We freeze the screen for 5 seconds here to give the user some time to soak in their loss and score and then we close the program automatically
        pygame.quit()
        quit()
    events = pygame.event.get()              # Each event like a mouse click is stored in this list
    for event in events:                     # Iterating through each event in the list
        if(event.type == pygame.QUIT):       # If the event is closing the game window
            pygame.quit()                    # Closing the pygame game environment
            quit()                           # Exiting the program
        if(event.type == pygame.KEYDOWN):    # This checks for if any kind fo keyboard ker=y is pressed like w, a or d
            if(event.key == pygame.K_w):     # We check for w and if w is pressed, we check if the key pressed before w was not s, and if it wasn't we change the direction of the snake accordingly
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
            else:                  # If the key pressed is neither of these, we just continue and execute the snake function
                continue
            snake()
    if(not events):               # If no button is clicked on no event or input is given by the user, we still want the game to go on and snake function to run
        snake()    
    clock.tick(20)                # This statement helps us control the frame rate of the game. If we want to increase the difficulty we can definitely do so by changing the framerate.

