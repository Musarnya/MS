import pygame
pygame.init()
w=2048
h=1233
screen=pygame.display.set_mode((w,h))
pg1=pygame.image.load('pg1.png')

pg1 = pygame.transform.scale(pg1,(w,h))
background=pg1
pc2=pygame.image.load('bgf.png')
pc2=pygame.transform.scale(pc2,(w,h))
start=pygame.image.load('plstar.png') 
start = pygame.transform.scale(start,(512,200))
start_hitbox=start.get_rect()
start_hitbox.center=(w/2,h/2)

gg=pygame.image.load("thogh.png")
gg_hitbox=gg.get_rect()
gg_hitbox.center=(1024,615)
def lore():
    screen.blit(gg, gg_hitbox)

loreactive=False
loreshow=False
show_start=True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_hitbox.collidepoint(event.pos):
                #screen.fill("black")
                background=pc2
                loreactive=True
                show_start=False
            if loreactive==True:
                loreshow=True
    screen.blit(background,(0,0))
    if show_start:
        screen.blit(start,start_hitbox)
    if loreshow:
        screen.blit(gg,gg_hitbox)
    pygame.display.update()
pygame.quit()
