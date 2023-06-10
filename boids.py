import pygame
import random
pygame.init()
#variables
width, height=700, 600
screen=pygame.display.set_mode((width, height))
run=True
clock=pygame.time.Clock()
fps=60
black=(0, 0, 0)
red=(255, 0, 0)
boids=pygame.sprite.Group()
left=False
right=False
up=False
down=False
img=pygame.image.load("imgs/Boid.png")
class Boid(pygame.sprite.Sprite):
    def __init__(self, img, screen_height, screen_width):
        super().__init__()
        self.width=width
        self.height=height
        self.screen_height=screen_height
        self.screen_width=screen_width
        self.start_angle=random.randrange(0, 360)
        self.x_update=0
        self.y_update=0
        self.image=img
        self.rect=img.get_rect()
        self.rect.centerx=random.randrange(0, self.screen_width)
        self.rect.centery=random.randrange(0, self.screen_height)
        self.angle=random.randrange(0, 360)
    def draw(self, screen):
        self.rect.centerx+=self.x_update
        self.rect.centery+=self.y_update
        self.rotated_image=pygame.transform.rotate(self.image, self.angle)
        self.rect=self.rotated_image.get_rect(center=(self.rect.centerx, self.rect.centery))
        screen.blit(self.rotated_image, self.rect)
    def update(self):
        print(self.angle, self.rect.x, self.rect.y)
        
for i in range (3):
    boids.add(Boid(img, height, width))
while run:
    screen.fill(black)
    clock.tick(fps)
    for boid in boids:
        boid.draw(screen)
        boid.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            break
    pygame.display.update()        
            
pygame.quit()