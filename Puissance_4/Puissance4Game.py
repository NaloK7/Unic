import pygame as pg
import os
from player import Player
import game_sprite as gs


class GamePuissance4:
    def __init__(self, master):
        self.current_path = os.getcwd()
        self.master = master

        self.width = 700
        self.height = 600
        self.screen = pg.display.set_mode((self.width, self.height))

        self.sprite_group = pg.sprite.Group()

        self.bg_sprite = gs.FixedSprite(f"{self.current_path}\Puissance_4\\background.png", self.width, self.height)
        self.sprite_group.add(self.bg_sprite)

        self.front_sprite = gs.FixedSprite(f"{self.current_path}\Puissance_4\\blue_grid.png", self.width, self.height)
        self.sprite_group.add(self.front_sprite)

        self.restart_sprite = gs.FixedSprite(f"{self.current_path}\\restart.png", self.width, self.height, restart=True)


        self.player_y = Player("y", f"{self.current_path}\Puissance_4\yellow_token.png")
        self.player_r = Player("r", f"{self.current_path}\Puissance_4\\red_token.png")
        self.current_player = self.player_y

        self.game_matrix = self.matrixPuissance()
        self.counter = 0
        self.counter_max = 42
        self.running = True
        self.reset = False
        self.clock = pg.time.Clock()

    # noinspection PyMethodMayBeStatic
    def matrixPuissance(self):
        """
        create an empty matrix for puissance 4 game 6x7
        """
        return [[None] * 7 for _ in range(6)]

    def addSpriteToGroup(self, path, width, height, x=-1, y=-1, r=0):
        # center by default
        if x == -1:
            x = width // 2
            y = height // 2
        sprite = gs.FixedSprite(path, width, height, x, y, r)
        # noinspection PyTypeChecker
        self.sprite_group.add(sprite)

    def manageEvents(self):
        """
        check QUIT / mouse click / restart
        """

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                # self.master.deiconify()
                # pygame.quit()

            # left click on mouse
            if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0] and not self.reset:
                # # get mouse's position
                # mouse_pos = pg.mouse.get_pos()
                # # real pos
                # mouse_x, mouse_y = mouse_pos
                # # convert pos to 0 / 1
                # mouse_x = mouse_x // (self.width // 3)
                # mouse_y = mouse_y // (self.height // 3)
                # self.checkInputPos(mouse_x, mouse_y)
                self.counter += 10
                if self.counter > self.counter_max:
                    self.reset = True

            if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[2] and self.reset:
                self.restart()

    def restart(self):
        self.reset = False
        self.counter = 0
        self.sprite_group.empty()
        self.screen.fill("black")
        self.game_matrix = self.matrixPuissance()

    # noinspection PyMethodMayBeStatic
    def display(self):
        # background
        self.sprite_group.draw(self.screen)
        # token group
        # blue grid image

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
