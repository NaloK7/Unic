import pygame
from Morpion.morpion_sprite import MorpionSprite as ms
from player import Player
import sys, os


class Game:
    def __init__(self, master):
        # self.master.withdraw()
        self.current_path = os.getcwd()
        self.master = master

        # window
        self.size = 600
        self.width = self.size
        self.height = self.size

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Morpion")
        # sprite groupe
        self.sprite_group = pygame.sprite.Group()

        self.running = True
        self.clock = pygame.time.Clock()
        self.counter = 0

        # player
        cross = self.resource(f"{self.current_path}\img\crossWhite.png")
        self.player_X = Player("X", cross)
        circle = self.resource(f"{self.current_path}\img\circleWhite.png")
        self.player_O = Player("O", circle)
        self.current_player = self.player_O

        self.game_matrice = self.matrixMorpion()
        self.win_line = ""

        restart = self.resource(f"{self.current_path}\img\\restart.png")
        self.restart_image_path = restart
        line = self.resource(f"{self.current_path}\img\greenLine.png")
        self.win_line_path = line
        self.reset = False

    def resource(self, relative_path):
        base_path = getattr(
            sys,
            '_MEIPASS',
            os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def manageEvents(self):
        """
        check QUIT / mouse click / restart
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # left click on mouse
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and not self.reset:
                # get mouse's position
                mouse_pos = pygame.mouse.get_pos()
                # real pos
                mouse_x, mouse_y = mouse_pos
                # convert pos to 0 / 1
                mouse_x = mouse_x//(self.width//3)
                mouse_y = mouse_y//(self.height//3)
                self.checkInputPos(mouse_x, mouse_y)

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] and self.reset:
                self.restart()

    # noinspection PyTypeChecker
    def checkInputPos(self, x: int, y: int):
        """
        y: line
        x: column
        check input validity and victory or end
        """
        if self.game_matrice[y][x] is None:
            self.game_matrice[y][x] = self.current_player.symbole
            self.sprite(self.current_player.pict_path, x, y)
            self.counter += 1
            self.endDisplay()
        else:
            pass

    def endDisplay(self):
        """
        display win line and/or restart image
        """
        if self.checkVictory() or self.counter == 9:
            if self.checkVictory():
                self.EndLineSprite()
            self.sprite(self.restart_image_path, 1, 1, 0, "restart")
            self.reset = True
        else:
            pass

    def matrixMorpion(self):
        """
        create an empty matrix 3x3
        """
        return [[None] * 3 for _ in range(3)]

    def restart(self):
        """
        reset variable and board to make a new game
        """
        self.reset = False
        self.counter = 0
        self.sprite_group.empty()
        self.screen.fill("black")
        self.game_matrice = self.matrixMorpion()

    def checkVictory(self):
        return (self.checkHorizontal()
                or self.checkVertical()
                or self.diagonal_win())

    def checkLine(self, line: list):
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

    def checkHorizontal(self):
        """
        check line victory in matrix
        """
        for i in range(len(self.game_matrice)):
            if self.checkLine(self.game_matrice[i]):
                self.win_line = f"L{i}"
                return True
        return False

    def checkVertical(self):
        """
        check column victory in matrix
        """
        for i in range(len(self.game_matrice)):
            column_check = []
            for line in self.game_matrice:
                column_check.append(line[i])
            if self.checkLine(column_check):
                self.win_line = f"C{i}"
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
        if self.checkLine(diag_1):
            self.win_line = "D1"
            return True
        if self.checkLine(diag_2):
            self.win_line = "D2"
            return True
        return False

    # noinspection PyTypeChecker
    def EndLineSprite(self):

        if self.win_line == "L0":
            x, y, r = 1, 0, 90
        elif self.win_line == "L1":
            x, y, r = 1, 1, 90
        elif self.win_line == "L2":
            x, y, r = 1, 2, 90
        elif self.win_line == "C0":
            x, y, r = 0, 1, 0
        elif self.win_line == "C1":
            x, y, r = 1, 1, 0
        elif self.win_line == "C2":
            x, y, r = 2, 1, 0
        elif self.win_line == "D1":
            x, y, r = 1, 1, 45
        else:
            x, y, r = 1, 1, -45  # d2

        self.sprite(self.win_line_path, x, y, r, "line")

    def sprite(self, path: str, pos_x: int, pos_y: int, r=0, type_is="player"):
        """
        create a sprite with: path, x, y, rotation, personal type(line/restart/player)
        """
        new_sprite = ms(path, pos_x, pos_y, self.size, r, type_is)
        self.sprite_group.add(new_sprite)

    def grid(self):
        """
        draw grid line
        """
        color_line = "grey"
        for x in range(0, 4):
            pygame.draw.line(self.screen, color_line,
                             (0, x * (self.width//3)),
                             (self.width, x * (self.height//3)), 10)

            pygame.draw.line(self.screen, color_line,
                             (x * (self.width//3), 0),
                             (x * (self.height//3), self.height), 10)

    def display(self):
        """
        update display board
        """
        self.grid()
        self.sprite_group.draw(self.screen)
        pygame.display.flip()

    def run(self):
        self.master.withdraw()
        while self.running:
            self.manageEvents()
            if self.counter % 2 == 0:
                self.current_player = self.player_O
            else:
                self.current_player = self.player_X
            self.display()
            self.clock.tick(60)

        if not self.running:
            self.master.deiconify()
            pygame.quit()
