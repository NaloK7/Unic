import pygame


class MorpionSprite(pygame.sprite.Sprite):
    def __init__(self, image_path: str, pos_x: int, pos_y: int, max_size: int):
        """
        create a sprite white a path, a mouse's coord and size of board
        """
        super().__init__()
        # load image
        self.image = pygame.image.load(image_path)
        length = max_size//3
        # resize image
        image_size = (length-50, length-50)
        self.image = pygame.transform.scale(self.image, image_size)
        # associate rect to image
        self.rect = self.image.get_rect()

        self.rect.center = [pos_x*length + length//2, pos_y*length + length//2]