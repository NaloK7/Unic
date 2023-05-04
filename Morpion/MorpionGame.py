import pygame
import sys
from Morpion.Sprite import MorpionSprite as ms
import os

class Game:
    def __init__(self, master):
    # def __init__(self):
        self.current_path = os.getcwd()
        self.master = master
        self.master.withdraw()
        self.color_line = "grey"
        self.size = 600
        self.width = self.size
        self.height = self.size
        self.third_width = int(self.size // 3)
        self.third_height = int(self.size // 3)
        self.screen = pygame.display.set_mode((self.width, self.height))

        # groupe de sprite
        self.sprite_group = pygame.sprite.Group()

        self.running = True
        self.clock = pygame.time.Clock()

        # game himself
        self.counter = 0
        self.player_X = ("X", f"{self.current_path}\Morpion\crossWhite.png")
        self.player_O = ("O", f"{self.current_path}\Morpion\circleWhite.png")
        self.current_player = self.player_O
        self.game_matrice = self.newMatrix()

        self.end_game = False

        # self.run()

    def manageEvents(self):
        """
        check if event append
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                # self.master.deiconify()
                # pygame.quit()

            # left click on mouse
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # get mouse's position
                mouse_pos = pygame.mouse.get_pos()
                # real pos
                mouse_x, mouse_y = mouse_pos
                # convert pos
                mouse_x = mouse_x//self.third_width
                mouse_y = mouse_y//self.third_width
                self.checkInputPos(mouse_x, mouse_y)

                if self.end_game:
                    self.restart()

    def checkInputPos(self, x: int, y: int):
        """
        y: line
        x: column
        """

        if self.game_matrice[y][x] is None:
            self.game_matrice[y][x] = self.current_player[0]
            self.sprite(x, y)
            self.counter += 1
        else:
            pass

    def newMatrix(self):
        return [[None] * 3 for _ in range(3)]

    def restart(self):
        self.end_game = False
        self.counter = 0
        self.sprite_group.empty()
        self.screen.fill("black")
        self.game_matrice = self.newMatrix()

    def checkVictory(self):
        return (
                self.horizontal_win()
                or self.vertical_win()
                or self.diagonal_win()
        )

    def win_line(self, line: list):
        """
        take a liste in argument
        check if all element are the same and not empty
        return a boolean
        """
        if None in line:
            return False

        ref = line[0]

        for elem in line:
            if elem != ref:
                return False
        return True

    def horizontal_win(self):
        """
        check line victory in matrix
        """
        for line in self.game_matrice:
            if self.win_line(line):
                return True
        return False

    def vertical_win(self):
        """
        check column victory in matrix
        """
        for i in range(len(self.game_matrice)):
            column_check = []
            for line in self.game_matrice:
                column_check.append(line[i])
            if self.win_line(column_check):
                return True
        return False

    def diagonal_win(self):
        """
            take a matrix in argument
            check if diagonal contains the same element
            """
        diag_1 = []
        diag_2 = []
        for i in range(len(self.game_matrice)):
            # par de coin haut gauche et descend en diag
            diag_1.append(self.game_matrice[i][i])

            # par du coin haut droit et descend en diag
            diag_2.append(self.game_matrice[i][-i - 1])
        if self.win_line(diag_1) or self.win_line(diag_2):
            return True
        return False

    def sprite(self, pos_x, pos_y):
        new_sprite = ms(self.current_player[1], pos_x, pos_y, self.size)
        self.sprite_group.add(new_sprite)

    def grid(self):
        """
        draw grid line
        """
        for x in range(0, 4):
            pygame.draw.line(self.screen, self.color_line,
                             (0, x * self.third_width),
                             (self.width, x * self.third_width), 10)

            pygame.draw.line(self.screen, self.color_line,
                             (x * self.third_height, 0),
                             (x * self.third_height, self.height), 10)

    def display(self):
        """
        update display board
        """
        self.grid()
        self.sprite_group.draw(self.screen)
        self.sprite_group.update()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.manageEvents()
            if self.checkVictory():
                self.end_game = True

            if self.counter % 2 == 0:
                self.current_player = self.player_O
            else:
                self.current_player = self.player_X
            self.display()
            self.clock.tick(60)

        if not self.running:
            self.master.deiconify()
            pygame.quit()

