import pygame, random


background_colour=(255,255,255)
(width,height)=(500,400)

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Coin Flip")
screen.fill(background_colour)
button=pygame.Rect(50,50,20,20)
pygame.display.flip()
image0  = pygame.image.load("C:\\Users\\49179\\Desktop\\mypyprojects\\pSpiel\\Heads.jpg").convert()
image0  = pygame.transform.scale(image0,(150,150))
image1 = pygame.image.load("C:\\Users\\49179\Desktop\mypyprojects\pSpiel\Tails.jpg").convert()
image1=pygame.transform.scale(image1,(150,150))

def coinfliip():
    heads=0
    tails=1
    flip=random.randint(0,1)
    if (flip==0):
        r=image0.get_rect()
        r.center=screen.get_rect().center
        screen.blit(image0,r)
    else:
        r=image1.get_rect()
        r.center=screen.get_rect().center
        screen.blit(image1,r)


  
running=True

while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False


        if event.type == pygame.MOUSEBUTTONDOWN:
            
            mouse_pos = event.pos  # gets mouse position
            
                # checks if mouse position is over the button

            if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                coinfliip()
                print('button was pressed at {0}'.format(mouse_pos))


    pygame.draw.rect(screen, [255, 0, 0], button)  # draw button
    pygame.display.flip()
