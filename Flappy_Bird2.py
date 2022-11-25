import pygame
import os

pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Flappy Bird')

start_time = 0

start_active = False

player_gravity = 0  

score = 0

black = pygame.Surface((1000,600))
black.fill('Black')
background = pygame.image.load(os.path.join('background.webp')).convert_alpha()
background_rect = background.get_rect(bottomright = (1000,600))
#'/home/sandeep/nothing/Day5 /background.webp'

base = pygame.image.load(os.path.join('base.png')).convert_alpha()
base2 = pygame.transform.scale(base,(1200 ,100))
base_rect = base2.get_rect(topleft = (0,500))

tunnel = pygame.image.load(os.path.join('pipe.png')).convert_alpha()
tunnel_up = pygame.transform.rotate(tunnel,180)

test_font = pygame.font.Font(None, 70)
click_text = test_font.render("Double Click On Your Mouse To Play",False,'Black')
click_rect = click_text.get_rect(center = (500,500) )


tunnel_rect_6 = tunnel.get_rect(topleft = (300,350))
tunnel_rect_up_6 = tunnel_up.get_rect(bottomleft = (300,tunnel_rect_6.y -150 ))

tunnel_rect_7 = tunnel.get_rect(topleft = (450,425))
tunnel_rect_up_7 = tunnel_up.get_rect(bottomleft = (450,tunnel_rect_7.y -150 ))

tunnel_rect_1 = tunnel.get_rect(topleft = (600,400))
tunnel_rect_up_1 = tunnel_up.get_rect(bottomleft = (600,tunnel_rect_1.y -150 ))

tunnel_rect_2 = tunnel.get_rect(topleft = (750,305))
tunnel_rect_up_2 = tunnel_up.get_rect(bottomleft = (750,tunnel_rect_2.y -150 ))

tunnel_rect_3 = tunnel.get_rect(topleft = (900,225))
tunnel_rect_up_3 = tunnel_up.get_rect(bottomleft = (900,tunnel_rect_3.y -150 ))

tunnel_rect_4 = tunnel.get_rect(topleft = (1050,350))
tunnel_rect_up_4 = tunnel_up.get_rect(bottomleft = (1050,tunnel_rect_4.y -150 ))

tunnel_rect_5 = tunnel.get_rect(topleft = (1200,250))
tunnel_rect_up_5 = tunnel_up.get_rect(bottomleft = (1200,tunnel_rect_5.y -150 ))

flappy_bird = pygame.image.load(os.path.join('bird.png')).convert_alpha()
bird_rect = flappy_bird.get_rect(center = (100,250))
bird_size = pygame.transform.scale(flappy_bird, (400,300))
bird_size_rect = bird_size.get_rect(center = (500,250))


def collision(tunnel_rect, tunnel_rect_up):
    if bird_rect.colliderect(tunnel_rect):
        return False
    elif bird_rect.colliderect(tunnel_rect_up):
        return False
    else:
        return  True

def display_score():
    current_time = int(round((pygame.time.get_ticks() - start_time)/1000,0))
    score_surf = test_font.render(f'{current_time}', False , (64,64,64))
    score_rect = score_surf.get_rect(center = (500,50))
    screen.blit(score_surf,score_rect)
    return current_time

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if start_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_gravity = -10
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -10
        else:   
            if event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                 game_active = True         
            start_time = pygame.time.get_ticks()


    if start_active:
        screen.blit(black,(0,0))
        screen.blit(background, background_rect)

        player_gravity += 1
        bird_rect.y += player_gravity 
        screen.blit(flappy_bird,bird_rect)

        tunnel_rect_up_6.x -= 4
        tunnel_rect_6.x -= 4
        if tunnel_rect_up_6.right <= 0 : 
            tunnel_rect_6.left =1000
            tunnel_rect_up_6.left = 1000
        
        screen.blit(tunnel , tunnel_rect_6)
        screen.blit(tunnel_up, tunnel_rect_up_6)

        tunnel_rect_up_7.x -= 4
        tunnel_rect_7.x -= 4
        if tunnel_rect_up_7.right <= 0 : 
            tunnel_rect_7.left =1000
            tunnel_rect_up_7.left = 1000
        screen.blit(tunnel , tunnel_rect_7)
        screen.blit(tunnel_up, tunnel_rect_up_7)


        tunnel_rect_up_1.x -= 4
        tunnel_rect_1.x -= 4
        if tunnel_rect_up_1.right <= 0 : 
            tunnel_rect_1.left =1000
            tunnel_rect_up_1.left = 1000
        screen.blit(tunnel , tunnel_rect_1)
        screen.blit(tunnel_up, tunnel_rect_up_1)
        
        tunnel_rect_up_2.x -= 4
        tunnel_rect_2.x -= 4
        if tunnel_rect_up_2.right <= 0 : 
            tunnel_rect_2.left =1000
            tunnel_rect_up_2.left = 1000
        screen.blit(tunnel , tunnel_rect_2)
        screen.blit(tunnel_up, tunnel_rect_up_2)
        
        tunnel_rect_up_3.x -= 4
        tunnel_rect_3.x -= 4
        if tunnel_rect_up_3.right <= 0 : 
            tunnel_rect_3.left =1000
            tunnel_rect_up_3.left = 1000
        screen.blit(tunnel , tunnel_rect_3)
        screen.blit(tunnel_up, tunnel_rect_up_3)
        
        tunnel_rect_up_4.x -= 4
        tunnel_rect_4.x -= 4
        if tunnel_rect_up_4.right <= 0 : 
            tunnel_rect_4.left =1000
            tunnel_rect_up_4.left = 1000
        screen.blit(tunnel , tunnel_rect_4)
        screen.blit(tunnel_up, tunnel_rect_up_4)

        tunnel_rect_up_5.x -= 4
        tunnel_rect_5.x -= 4
        if tunnel_rect_up_5.right <= 0 : 
            tunnel_rect_5.left =1000
            tunnel_rect_up_5.left = 1000
        screen.blit(tunnel , tunnel_rect_5)
        screen.blit(tunnel_up, tunnel_rect_up_5)

        # # if start_active == True:
        # # elif start_active == True:
        # # elif start_active == True:
        # # elif start_active == True:
        # # elif start_active == True:
        # # elif start_active == True:
        # # elif start_active == True:

        if collision(tunnel_rect_6,tunnel_rect_up_6) == False:
           start_active = False   
        elif collision(tunnel_rect_7,tunnel_rect_up_7) == False:
            start_active = False
        elif collision(tunnel_rect_1,tunnel_rect_up_1) == False:
            start_active = False
        elif collision(tunnel_rect_2,tunnel_rect_up_2) == False:
            start_active = False
        elif collision(tunnel_rect_3,tunnel_rect_up_3) == False:
            start_active = False
        elif collision(tunnel_rect_4,tunnel_rect_up_4) == False:
            start_active = False
        elif collision(tunnel_rect_5,tunnel_rect_up_5) == False:
            start_active = False
        if bird_rect.colliderect(base_rect) :
            start_active = False
        score = display_score()
        screen.blit(base2 , base_rect)
        if start_active == False:  
            player_gravity = 0 
            bird_rect = flappy_bird.get_rect(center = (100,250))

            tunnel_rect_6 = tunnel.get_rect(topleft = (300,350))
            tunnel_rect_up_6 = tunnel_up.get_rect(bottomleft = (300,tunnel_rect_6.y -150 ))

            tunnel_rect_7 = tunnel.get_rect(topleft = (450,425))
            tunnel_rect_up_7 = tunnel_up.get_rect(bottomleft = (450,tunnel_rect_7.y -150 ))

            tunnel_rect_1 = tunnel.get_rect(topleft = (600,400))
            tunnel_rect_up_1 = tunnel_up.get_rect(bottomleft = (600,tunnel_rect_1.y -150 ))

            tunnel_rect_2 = tunnel.get_rect(topleft = (750,305))
            tunnel_rect_up_2 = tunnel_up.get_rect(bottomleft = (750,tunnel_rect_2.y -150 ))

            tunnel_rect_3 = tunnel.get_rect(topleft = (900,225))
            tunnel_rect_up_3 = tunnel_up.get_rect(bottomleft = (900,tunnel_rect_3.y -150 ))

            tunnel_rect_4 = tunnel.get_rect(topleft = (1050,350))
            tunnel_rect_up_4 = tunnel_up.get_rect(bottomleft = (1050,tunnel_rect_4.y -150 ))

            tunnel_rect_5 = tunnel.get_rect(topleft = (1200,250))
            tunnel_rect_up_5 = tunnel_up.get_rect(bottomleft = (1200,tunnel_rect_5.y -150 ))
            pygame.display.update()
        pygame.display.update()

    else:
        score_text = test_font.render(f"Your Score {score}", False , "Black")
        score_rect = score_text.get_rect(center = (500,550))
        surf = pygame.Surface((1000,600))
        surf.fill('Green')
        screen.blit(surf,(0,0))
        screen.blit(bird_size, bird_size_rect)
        screen.blit(click_text, click_rect)
        screen.blit(score_text, score_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_active = True
        start_time = pygame.time.get_ticks()
        pygame.display.update()
        clock.tick(30)
