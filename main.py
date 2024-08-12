import pygame
pygame.init()
w=2048
h=1233
screen=pygame.display.set_mode((w,h))
pc1=pygame.image.load('pc1.png')

pc1 = pygame.transform.scale(pc1,(w,h))
background=pc1
pc2=pygame.image.load('pc2.png')
pc2=pygame.transform.scale(pc2,(w,h))
start=pygame.image.load('START.png') 
start = pygame.transform.scale(start,(w,h))
start_hitbox=start.get_rect()
start_hitbox.center=(w/2,h/2)
show_start=True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_hitbox.collidepoint(event.pos):
                background=pc2
                show_start=False
    screen.blit(background,(0,0))
    if show_start:
        screen.blit(start,start_hitbox)
    pygame.display.update()
pygame.quit()
