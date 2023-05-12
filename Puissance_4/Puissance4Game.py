import pygame as pg
import os
from player import Player
import game_sprite as gs


class GamePuissance4:
    def __init__(self, master):
        self.current_path = os.getcwd()
        self.master = master

        self.width = 933
        self.height = 800
        self.screen = pg.display.set_mode((self.width, self.height))

        self.sprite_group = pg.sprite.Group()

        self.bg_sprite = gs.FixedSprite(f"{self.current_path}\Puissance_4\\background.png", self.width, self.height)
        self.front_sprite = gs.FixedSprite(f"{self.current_path}\Puissance_4\\blue_grid.png", self.width, self.height)
        self.restart_sprite = gs.FixedSprite(f"{self.current_path}\\restart.png", self.width, self.height, restart=True)

        self.player_y = Player("y", f"{self.current_path}\Puissance_4\yellow_token.png")
        self.player_r = Player("r", f"{self.current_path}\Puissance_4\\red_token.png")
        self.current_player = self.player_y

        self.game_matrix = self.matrixPuissance()
        self.counter = 0
        self.counter_max = 42  # Modify
        self.running = True
        self.reset = False
        self.delay = 0
        self.clock = pg.time.Clock()

    # noinspection PyMethodMayBeStatic
    def matrixPuissance(self):
        """
        create an empty matrix for puissance 4 game 6x7
        """
        return [[None] * 7 for _ in range(6)]

    def addSpriteToGroup(self, path, x, y_max):

        sprite = gs.Puissance4Sprite(path, self.width, self.height, x, y_max)
        # noinspection PyTypeChecker
        self.sprite_group.add(sprite)

    def manageEvents(self):
        """
        check QUIT / mouse click / restart
        """

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            # left click on mouse
            if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0] and not self.reset:
                # get mouse's position
                mouse_pos = pg.mouse.get_pos()
                # real pos
                mouse_x, mouse_y = mouse_pos
                # convert pos to 0 / 1
                mouse_x = mouse_x // (self.width // 7)
                # mouse_y = mouse_y // (self.height // 6)
                self.checkInputPos(mouse_x)

                if self.counter >= self.counter_max:
                    self.reset = True

            if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[2] and self.reset:
                self.restart()

    def checkInputPos(self, x: int):
        """
        y: line
        x: column
        check input validity and victory or end
        """
        if self.ColumnIsNotFull(x):  # Modify: you can click on token to put yours on top if there is space above
            # put y in last possible position
            y_max = self.lowestLevelIn(x)
            # add player symbol to matrix
            self.set_token(y_max, x)
            # add sprite to group
            self.addSpriteToGroup(self.current_player.pict_path, x, y_max)  #
            self.counter += 1

            matrix = self.reduce_board()

            if self.victory(matrix):
                self.reset = True
            # self.endDisplay()  ##
        else:
            pass

    def set_token(self, y: int, x: int):
        # add player symbol to matrix
        # noinspection PyTypeChecker
        self.game_matrix[y][x] = self.current_player.symbole

    def victory(self, matrix):
        """
        Reduce matrix and check victory
        """

        return (self.line_win(matrix)
                or self.columnWim(matrix)
                or self.diagonal_win(matrix))

    @staticmethod
    def reduce_column(matrix):
        copy_board = []
        for i in range(len(matrix[0])):
            column = []
            for j in range(len(matrix)):
                column.append(matrix[j][i])
            if set(column) is not None:
                copy_board.append(column)
        return copy_board

    def reduce_line(self):
        copy_board = []
        for ligne in self.game_matrix:
            if set(ligne) is not None:
                copy_board.append(ligne[:])
        return copy_board

    def reduce_board(self):
        copy_board = self.reduce_line()
        copy_board = self.reduce_column(copy_board)
        for x in range(len(copy_board)):
            for y in range(len(copy_board[x])):
                if copy_board[x][y] is None:
                    copy_board[x][y] = " "
        return copy_board

    def line_win(self, matrix):
        for line in matrix:
            if self.current_player.symbole * 4 in "".join(line):
                return True
        return False

    def columnWim(self, matrix):
        for i in range(len(matrix[0])):
            column = []
            for j in range(len(matrix)):
                column.append(matrix[j][i])
            if self.current_player.symbole * 4 in "".join(column):
                return True
        return False

    def diagonal_win(self, matrix):
        """
        check diagonal win in matrix
        """
        for j in range(
                round(len(matrix[0]) / 2)):  # boucle sur une longueur de ligne / 2
            d1 = []
            d2 = []
            for i in range(len(matrix)):  # colonne
                if i + j < len(matrix[0]):
                    # part du coin haut gauche et descend en diag
                    d1.append(matrix[i][i + j])
                    # part du coin haut droit et descend en diag
                    d2.append(matrix[i][-(i + j) - 1])
            if self.line_win([d1, d2]):
                return True

        for j in range(1, round(len(matrix) / 3)):
            d3 = []
            d4 = []
            for i in range(len(matrix[0])):
                if i + j < len(matrix):
                    d3.append(matrix[j + i][i])
                    d4.append(matrix[j + i][-i - 1])
            if self.line_win([d3, d4]):
                return True

        return False

    def ColumnIsNotFull(self, x):
        """
        return boolean state of column fullness
        """
        if self.game_matrix[0][x] is None:
            return True
        else:
            return False

    def lowestLevelIn(self, x):
        """
        return last pos possible in column
        """
        y_max = 0
        for i in range(len(self.game_matrix)):
            # si la case regarder est vide, on garde l'index en memoire
            if self.game_matrix[i][x] is None:
                y_max = i
            else:
                break

        return y_max

    def restart(self):
        self.reset = False
        self.counter = 0
        self.sprite_group.empty()
        self.screen.blit(self.bg_sprite.image, self.bg_sprite.rect)
        self.screen.blit(self.front_sprite.image, self.front_sprite.rect)
        self.game_matrix = self.matrixPuissance()

    def displayRestartImage(self):
        self.screen.blit(self.restart_sprite.image, self.restart_sprite.rect)

    # noinspection PyMethodMayBeStatic
    def display(self):

        # background
        self.screen.blit(self.bg_sprite.image, self.bg_sprite.rect)
        # token group

        for sprite in self.sprite_group:

            sprite.update()
        self.sprite_group.draw(self.screen)
        # blue grid image
        self.screen.blit(self.front_sprite.image, self.front_sprite.rect)
        if self.reset:
            self.delay += 1
            if self.delay >= 30:
                self.displayRestartImage()
        pg.display.flip()

    def run(self):
        self.master.withdraw()
        while self.running:
            self.manageEvents()
            if self.counter % 2 == 0:
                self.current_player = self.player_y
            else:
                self.current_player = self.player_r
            self.display()
            self.clock.tick(60)

        if not self.running:
            self.master.deiconify()
            pg.quit()
