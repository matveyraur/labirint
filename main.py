import pygame 
import os 
pygame.init() 
def file_path(filename): 
    folder = os.path.abspath(__file__ + "/..") 
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

image_viktory = pygame.image.load(file_path(r"images/rick.png"))
image_viktory = pygame.transform.scale(image_viktory, (WIN_WIDTH, WIN_HEIGHT))

image_lose = pygame.image.load(file_path(r"images\lose.jpg"))
image_lose = pygame.transform.scale(image_lose, (WIN_WIDTH, WIN_HEIGHT))
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) 
clock = pygame.time.Clock() 

class GameSprite(pygame.sprite.Sprite): 
    def __init__(self, x, y, width, height, image): 
        super().__init__() 
        self.rect = pygame.Rect(x, y, width, height) 
        self.image = pygame.image.load(file_path(image)) 
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite): 
    def __init__(self, x, y, width, height, image, speed_x, speed_y): 
        super().__init__(x, y, width, height, image) 
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

player = Player(20, 10, 75, 75, r"images\player.png",0, 0) 
enemy = GameSprite(350, 250, 100, 150, r"images\enemy.png") 
finish = GameSprite(330, 150, 100, 100, r"images\finish.png") 
 
fakewalls = pygame.sprite.Group() 
walls = pygame.sprite.Group() 
wall1 = GameSprite(150, 0, 20, 500, r"images\wall.jpg") 
walls.add(wall1) 
 
wall2 = GameSprite(300, 200, 20, 300, r"images\wall.jpg") 
walls.add(wall2) 
 
wall3 = GameSprite(300, 100, 500, 20, r"images\wall.jpg") 
walls.add(wall3) 
 
wall4 = GameSprite(450, 200, 20, 300, r"images\wall.jpg") 
walls.add(wall4) 
 
wall5 = GameSprite(450, 250, 350, 20, r"images\wall.jpg") 
walls.add(wall5) 
 
wall6 = GameSprite(300, 120, 20, 100, r"images\wall.jpg") 
fakewalls.add(wall6) 
 
wall7 = GameSprite(450, 120, 20, 150, r"images\wall.jpg") 
fakewalls.add(wall7) 
 
 
level = 1 
game = True 
while game: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            game = False 
        if level == 1: 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                    player.speed_x = -5 
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                    player.speed_x = 5 
                if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                    player.speed_y = 5  
                if event.key == pygame.K_UP or event.key == pygame.K_w: 
                    player.speed_y = -5 
 
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                    player.speed_x = 0 
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                    player.speed_x = 0 
                if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                    player.speed_y = 0 
                if event.key == pygame.K_UP or event.key == pygame.K_w: 
                    player.speed_y = 0                                     
            
    if level == 1: 
        window.blit(fon, (0, 0)) 
        walls.draw(window) 
        fakewalls.draw(window) 
        player.show() 
        player.update() 
        enemy.show() 
        finish.show() 
 
        if pygame.sprite.collide_rect(player, finish):
            level = 10
            pygame.mixer.music.stop()
            pygame.mixer.music.load(file_path(r"music\Rick Astley - Together Forever.mp3"))
            pygame.mixer.music.play(-1)
    elif level == 10:
        window.blit(image_viktory,(0, 0))
    clock.tick(FPS) 
    pygame.display.update()