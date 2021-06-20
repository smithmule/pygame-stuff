##pygame tutorial to bounce a ball around the screen
#import the needed modules
import sys, pygame, time

#call to set up some crap
pygame.init()

#set screen size variables
size = width, height = 960, 540

#set x,y speed vector array table list thingy variable
speed = [2, 2]

#make a colour
black = 0, 0, 0

#create the window
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ball tutorial')

#load ball image into a variable
ball = pygame.image.load("intro_ball.gif")

#create a sprite using ball variable??
ballrect = ball.get_rect()

#load sfx into a variable
effect = pygame.mixer.Sound("beep.wav")

#main game loop
while 1:
    
    #set fps
    pygame.time.Clock().tick(60)
    
    #check for exit button press
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #move the sprite
    ballrect = ballrect.move(speed)
    
    #check for x limits
    if ballrect.left < 0 or ballrect.right > width:
        #reverse x direction and play sound effect
        speed[0] = -speed[0]
        effect.play()
    #check for y limits
    if ballrect.top < 0 or ballrect.bottom > height:
        #reverse y direction
        speed[1] = -speed[1]

    #clear screen
    screen.fill(black)
    #put the sprite into fram buffer??
    screen.blit(ball, ballrect)
    #draw the buffer to the screen??
    pygame.display.flip()
