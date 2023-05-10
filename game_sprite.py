import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, path, width, height):
        super().__init__()
        self.image = pygame.image.load(path)
        self.width_max = width
        self.height_max = height

# background / restart


class FixedSprite(GameSprite):
    def __init__(self, path, width, height, restart=False):
        super().__init__(path, width, height)
        if restart:
            length = 250
            self.image = pygame.transform.scale(self.image, (length, length))
        else:
            # image scale to max size of window
            self.image = pygame.transform.scale(self.image, (self.width_max, self.height_max))

        self.rect = self.image.get_rect()

        # center of image is center of window
        self.rect.center = [self.width_max//2, self.height_max//2]


# puissance 4 token
class Puissance4Sprite(GameSprite):
    def __init__(self, path, width, height, x, y):
        super().__init__(path, width, height)
        # A REVOIR
        width = self.width_max // 7
        height = self.height_max // 6
        self.image = pygame.transform.scale(self.image, (width - 20, height - 20))

        self.rect = self.image.get_rect()

        # center of image is center of window
        x = (x * width + width) // 2
        y = (y * height + height) // 2
        self.rect.center = [x, y]

# class GameSprite(pygame.sprite.Sprite):
#     def __init__(self, path: str, wmax: int, hmax: int, x=0, y=0, r=0):
#         super().__init__()
#         # init picture
#         self.pict = pygame.image.load(path)
#         self.width_max = wmax
#         self.height_max = hmax
#         self.pos_x = x
#         self.pos_y = y
#         self.rotation = r
#
#         # work with
#         self.pict = pygame.transform.scale(self.pict, (self.width_max, self.height_max))
#         self.rect = self.pict.get_rect()
#         self.rect.center = [self.width_max//2, self.height_max//2]
#
