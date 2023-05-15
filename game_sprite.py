import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, path: str, width: int, height: int):
        super().__init__()
        self.image = pygame.image.load(path)
        self.width_max = width
        self.height_max = height


# background / restart


class FixedSprite(GameSprite):
    """
    restart: True → resize image with length
    used for background / front / restart
    """
    def __init__(self, path: str, width: int, height: int, restart=False):
        super().__init__(path, width, height)
        if restart:
            length = 250
            self.image = pygame.transform.scale(self.image, (length, length))
        else:
            # image scale to max size of window
            self.image = pygame.transform.scale(self.image, (self.width_max, self.height_max))

        self.rect = self.image.get_rect()

        # center of image is center of window
        self.rect.center = [self.width_max // 2, self.height_max // 2]


# puissance 4 token
class Puissance4Sprite(GameSprite):
    """
    resize sprite of token player to scale with window
    """

    def __init__(self, path: str, width: int, height: int, x: int, y_max: int):
        super().__init__(path, width, height)
        # A REVOIR
        width = self.width_max // 7
        height = self.height_max // 6
        self.y_max = y_max * height + height // 2

        self.image = pygame.transform.scale(self.image, (width - 20, height - 20))

        self.rect = self.image.get_rect()

        # center of image is center of window
        self.x = x * width + width // 2
        self.y = 0
        # y = y * height + height // 2
        self.rect.center = [self.x, self.y]

    def update(self):
        speed = 30
        if self.y < self.y_max:
            self.y += speed
            if self.y > self.y_max:
                self.y = self.y_max
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
