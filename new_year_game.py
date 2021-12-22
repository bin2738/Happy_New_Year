import pygame
import sys
from Backgraund import Background
import random
from os import path

class Snow(pygame.sprite.Sprite):
    def __init__(self,width, height) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > self.height + 10:
            self.rect.x = random.randrange(self.width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class New_game:
    def __init__(self) -> None:
        self.WIDTH = 1280
        self.HEIGHT = 800
        pygame.init()
        img_dir = path.join(path.dirname(__file__), 'img')
        self.background = pygame.image.load(path.join(img_dir, 'fon.jpg'))
        self.background_rect = self.background.get_rect()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snow")
        self.clock = pygame.time.Clock()
        self.all_snow = pygame.sprite.Group()
        self.__get_snow(1000)
        self.run() 
       
    def __get_snow(self,number):
        for i in range(number):
            self.snow = Snow(self.WIDTH, self.HEIGHT)
            self.all_snow.add(self.snow)


    def run(self):
        while True:
            self.clock.tick(25)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass
                
            self.all_snow.update()
            self.screen.fill(color=(32, 178, 170))
            self.screen.blit(self.background, self.background_rect)
            self.all_snow.draw(self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    New_game()
    