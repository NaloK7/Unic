import pygame


class MorpionSprite(pygame.sprite.Sprite):
    def __init__(self, image_path: str, pos_x: int, pos_y: int, max_size: int, rotate=0, type_is="player"):
        """
        create a sprite white a path, coord x, y, size of board, rotation, personal type(line/restart/player)
        """
        super().__init__()
        # load image
        self.image = pygame.image.load(image_path)
        if type_is == "player":
            length = max_size//3
            # resize image
            image_size = (length-50, length-50)
            self.image = pygame.transform.scale(self.image, image_size)
            # associate rect to image
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x * length + length // 2, pos_y * length + length // 2]

        elif type_is == "line":
            length = max_size//3
            self.image = pygame.transform.rotate(self.image, rotate)
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x * length + length // 2, pos_y * length + length // 2]

        elif type_is == "restart":
            length = max_size // 2
            image_size = (length, length)
            self.image = pygame.transform.scale(self.image, image_size)
            self.rect = self.image.get_rect()
            self.rect.center = [length, length]
