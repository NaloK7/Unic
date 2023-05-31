# coding: utf-8

import customtkinter as ctk
import pygame
from Morpion import MorpionGame as mg
from Puissance_4 import Puissance4Game as pg
from file_menu import FileMenu
from game_panel import GamePanel
from encryption_panel import EncryptionPanel


class UniqueApp(ctk.CTk):
    """
    encryption window
    """

    def __init__(self):
        super().__init__()
        # size
        self.geometry("800x600")
        # self.resizable(width=False, height=False)
        # window name
        self.title("Unique")

        self.text_color = "#E0E0E0"
        self.font_button = ("default", 12, "bold")

        # MENU
        self.file_menu = FileMenu(self, 20)

        # GAME PANEL
        self.game_panel = GamePanel(self, 1.0, 0.6, self.font_button, self.text_color)

        # ENCRYPTION PANEL
        self.encryption_panel = EncryptionPanel(self, 1.0, 0.5, self.font_button, self.text_color)

        # main game button
        self.button = ctk.CTkButton(self,
                                    text="Game",
                                    text_color=self.text_color,
                                    font=self.font_button,
                                    # fg_color="#808080",
                                    border_width=2,
                                    border_color=("black", "#DDDDDD"),
                                    command=self.move_game_panel)

        self.button.place(relx=0.25,
                          rely=0.4,
                          anchor="center")
        # encrypted button
        self.button = ctk.CTkButton(self,
                                    text="Cryptage",
                                    text_color=self.text_color,
                                    font=self.font_button,
                                    # fg_color="#808080",
                                    border_width=2,
                                    border_color=("black", "#DDDDDD"),
                                    command=self.move_encryption_panel)

        self.button.place(relx=0.75,
                          rely=0.4,
                          anchor="center")

        self.reset_button = ctk.CTkButton(self,
                                          text=u"\U000027F2",
                                          width=30,
                                          command=self.reset_encryption_panel)
        self.reset_button.place(relx=0.88
                                ,
                                rely=0.4,
                                anchor="center")

    def reset_encryption_panel(self):
        self.encryption_panel.destroy()
        self.encryption_panel = EncryptionPanel(self, 1.0, 0.5, self.font_button, self.text_color)

    def move_game_panel(self):
        if not self.encryption_panel.is_hide:
            self.encryption_panel.move_panel()
        self.game_panel.tkraise(self.encryption_panel)
        self.game_panel.move_panel()

    def move_encryption_panel(self):
        if not self.game_panel.is_hide:
            self.game_panel.move_panel()
        self.encryption_panel.tkraise(self.game_panel)
        self.encryption_panel.move_panel()

    def run_morpion(self):
        pygame.init()
        game = mg.Game(self)
        game.run()

    def run_puissance4(self):
        pygame.init()
        game = pg.GamePuissance4(self)
        game.run()


test = UniqueApp()
test.mainloop()
