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
red=(255, 0, 0)
boids=pygame.sprite.Group()
left=False
right=False
up=False
down=False
boid_img=pygame.image.load("")
class Boid(pygame.sprite.Sprite):
    def __init__(self, img, screen_height, screen_width, color):
        super().__init__()
        self.width=width
        self.height=height
        self.screen_height=screen_height
        self.screen_width=screen_width
        self.start_x=random.randrange(0, self.screen_width)
        self.start_y=random.randrange(0, self.screen_height)
        self.rect=pygame.Rect((self.start_x, self.start_y), (self.width, self.height))
        self.start_angle=random.randrange(0, 360)
        self.x_update=0
        self.y_update=0
        self.color=color
    def draw(self, screen):
        self.rect.centerx+=self.x_update
        self.rect.centery+=self.y_update
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.left=left
        self.right=right
        self.up=up
        self.down=down
for i in range (2):
    boids.add(Boid(30, 20, height, width, red))
while run:
    screen.fill(black)
    clock.tick(fps)
    for boid in boids:
        boid.draw(screen)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            break
    pygame.display.update()        
            
pygame.quit()