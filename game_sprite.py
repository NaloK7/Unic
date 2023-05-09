import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, path: str, wmax: int, hmax: int, x=0, y=0, r=0):
        super().__init__()
        self.pict = pygame.image.load(path)
        self.width_max = wmax
        self.height_max = hmax
        self.pos_x = x
        self.pos_y = y
        self.rotation = r
