import pygame 
import os 
pygame.init() 
def file_path(filename): 
    folder = os.path.abspath(file + "/..") 
    path = os.path.join(folder, filename) 
    return path 
WIN_WIDTH = 900 
WIN_HEIGHT = 600 
FPS = 60 

pygame.mixer.music.load(file_path(r"music\Rick Astley - Never Gonna Give You Up.mp3"))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

fon = pygame.image.load(file_path(r"images/rick.png")) 
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT)) 

image_viktory = pygame.image.load(file_path(r"images/win.png"))
image_viktory = pygame.transform.scale(image_viktory, (WIN_WIDTH, WIN_HEIGHT))

image_lose = pygame.image.load(file_path(r"images\lose.jpg"))
image_lose = pygame.transform.scale(image_lose, (WIN_WIDTH, WIN_HEIGHT))

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) 
clock = pygame.time.Clock() 

class GameSprite(pygame.sprite.Sprite): 
    def init(self, x, y, width, height, image): 
        super().init() 
        self.rect = pygame.Rect(x, y, width, height) 
        self.image = pygame.image.load(file_path(image)) 
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite): 
    def init(self, x, y, width, height, image, speed_x, speed_y): 
        super().init(x, y, width, height, image) 
        self.speed_x = speed_x 
        self.speed_y = speed_y 
 
    def update(self): 
        if self.speed_x < 0 and self.rect.left > 0 or self.speed_x > 0 and self.rect.right < WIN_WIDTH: 
            self.rect.x += self.speed_x 
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_x > 0:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left)
        if self.speed_x < 0:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)

        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y

        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_y < 0:
            for wall in walls_touched:
                self.rect.top = max(self.rect.top, wall.rect.bottom)
        if self.speed_y > 0:
            for wall in walls_touched:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)

class Enemy(GameSprite):
    def init(self, x, y, width, height, image, direction, min_coord, max_coord, speed):
        super().init(x, y, width, height, image)
        self.direction = direction
        self.min_coord = min_coord
        self.max_coord = max_coord
        self.speed = speed

        if self.direction == "right":
            self.image_r = self.image
            self.image_l = pygame.transform.flip(self.image, True, False)
        elif self.direction == "left": 
            self.image_l = self.image
            self.image_r = pygame.transform.flip(self.image, True, False)

    def update(self):
        if self.direction == "left" or self.direction == "right":
            if self.direction == "left":
                self.rect.x -= self.speed
            elif self.direction == "right":
                self.rect.x += self.speed

            if self.rect.right >= self.max_coord:
                self.direction = "left"
                self.image = self.image_l
            if self.rect.left <= self.min_coord:
                self.direction = "right"
                self.image = self.image_r
        elif self.direction == "up" or self.direction == "down":
            if self.direction == "up":
                self.rect.y -= self.speed
            elif self.direction == "down":
                self.rect.y += self.speed

            if self.rect.top <= self.min_coord:
                self.direction = "down"
            if self.rect.bottom >= self.max_coord: