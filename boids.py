import pygame
import random
pygame.init()
#variables
width, height=1000, 1000
screen=pygame.display.set_mode((width, height))
run=True
clock=pygame.time.Clock()
fps=30
black=(0, 0, 0)
boids=pygame.sprite.Group()
class Boid(pygame.sprite.Sprite):
    def __init__(self, width, height, screen_height, screen_width):
        super().__init__()
        self.width=width
        self.height=height
        self.screen_height=screen_height
        self.screen_width=screen_width
        self.start_x=random.randrange(0, self.screen_width)
        self.start_y=random.randrange(0, self.screen_height)
        self.rect=pygame.Rect((self.start_x, self.start_y), (self.width, self.height))
        self.x_update=0
        self.y_update=0
    def draw(self, window):
        self.rect.color=(255, 0, 0)
        self.rect.centerx+=self.x_update
        self.rect.centery+=self.y_update
        window.blit(window, self.rect)
for boid in range(10):
    boids.add(Boid(20, 20, height, width))
while run:
    screen.fill(black)
    clock.tick(fps)
    for boid in boids:
        boid.draw(screen)
    screen.blit(pygame.Rect(0, 0, 100, 100))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            break
    pygame.display.update()        
            
pygame.quit()