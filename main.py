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
fon = pygame.image.load(file_path(r"images/fon.jpg"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))
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
walls = pygame.sprite.Group()
wall1 = GameSprite(100, 300, 20, 300, r"images\wall.jpg")
walls.add(wall1)
wall2 = GameSprite(300, 300, 300, 20, r"images\wall.jpg")
walls.add(wall2)
wall3 = GameSprite(200, 100, 300, 20, r"images\wall.jpg")
walls.add(wall3)
level = 1
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if level == 1:
        window.blit(fon, (0, 0))
        walls.draw(window)
    clock.tick(FPS)
    pygame.display.update()