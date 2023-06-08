import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, path: str, width: int, height: int):
        super().__init__()
        self.image = pygame.image.load(path)
        self.width_max = width
        self.height_max = height


class WinnerSprite(GameSprite):
    """
    restart: True → resize image with length
    used for display in center background / front / restart
    """
    def __init__(self, path: str, width: int, height: int):
        super().__init__(path, width, height)
        self.rect = self.image.get_rect()
        self.rect.center = [self.width_max / 2+3, self.height_max / 4]


class FixedSprite(GameSprite):
    """
    used for display in center background / front / restart
    """
    def __init__(self, path: str, width: int, height: int):
        super().__init__(path, width, height)
        self.rect = self.image.get_rect()
        self.rect.center = [self.width_max // 2, self.height_max // 2]


# puissance 4 token
class Puissance4Sprite(GameSprite):
    """
    resize sprite of token player to scale with window
    """

    def __init__(self, path: str, width: int, height: int, x: int, y_max: int):
        super().__init__(path, width, height)
        self.to_update = True
        self.rect = self.image.get_rect()
        self.x = ((self.width_max/7) * x) + (self.width_max / 14)
        self.y_max = ((self.height_max/6)*y_max) + (self.height_max/12)
        self.y = 0
        self.rect.center = [self.x, self.y]

    def update(self):
        speed = 30
        if self.y < self.y_max and self.to_update:
            self.y += speed
            if self.y > self.y_max:
                self.y = self.y_max
                self.to_update = False
            self.rect = self.image.get_rect()
            self.rect.center = [self.x, self.y]


class MouseSprite(GameSprite):
    def __init__(self, path, width, height):
        super().__init__(path, width, height)
        self.width = (self.width_max // 7) - 20
        self.height = (self.height_max // 6) - 20
        self.image = self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self, path):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect.center = pygame.mouse.get_pos()
