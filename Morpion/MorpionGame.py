import pygame


class Game:
    def __init__(self):
        size = 600
        self.width = size
        self.height = size
        self.third_width = int(size / 3)
        self.third_height = int(size / 3)
        self.screen = pygame.display.set_mode((self.width, self.height))


        self.area = pygame.Rect(0, 0, self.third_width-4, self.third_height-4)
        self.area_color = "red"

        self.running = True
        self.clock = pygame.time.Clock()
        self.color_line = "grey"


    def drawHitbox(self):
        pygame.draw.rect(self.screen, self.area_color, self.area)
    def manageEvents(self):
        """
        check if event append
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # add numpad key detector to change display

    def grid(self):
        """
        draw grid line
        """
        for x in range(1, 3):
            pygame.draw.line(self.screen, self.color_line,
                             (0, x * self.third_width),
                             (self.width, x * self.third_width),10)

            pygame.draw.line(self.screen, self.color_line,
                             (x * self.third_height, 0),
                             (x * self.third_height, self.height), 10)

    def display(self):
        """
        update board game
        """
        self.grid()
        self.drawHitbox()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.manageEvents()
            self.display()
            self.clock.tick(60)
