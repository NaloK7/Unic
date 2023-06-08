# coding: utf-8

import customtkinter as ctk
import pygame
from Morpion import MorpionGame as mg
from Puissance_4 import Puissance4Game as pg
from file_menu import FileMenu
from game_panel import GamePanel
from encryption_panel import EncryptionPanel
from PIL import ImageTk, Image
import sys, os


class UnicApp(ctk.CTk):
    """
    encryption window
    """

    def __init__(self):
        super().__init__()
        # size
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        # window name
        self.title("Unique")

        self.text_color = "white" #E0E0E0"
        self.font_button = ("default", 12, "bold")

        # MENU
        self.file_menu = FileMenu(self, 20)

        # LOGO
        light = self.resource(f"{os.getcwd()}\img\logo_light.png")
        light_logo = Image.open(light)
        dark = self.resource(f"{os.getcwd()}\img\logo_dark.png")
        dark_logo = Image.open(dark)

        self.img_logo = ctk.CTkImage(light_image=light_logo,
                                     dark_image=dark_logo,
                                     size=(450, 178))
        self.img_label = ctk.CTkLabel(self, image=self.img_logo, text="")
        self.img_label.place(anchor="n", relx=0.5, rely=0.07)

        # GAME PANEL
        self.game_panel = GamePanel(self, 1.0, 0.55, self.font_button, self.text_color)

        # ENCRYPTION PANEL
        self.encryption_panel = EncryptionPanel(self, 1.0, 0.55, self.font_button, self.text_color)

        # main game button
        self.button = ctk.CTkButton(self,
                                    text="Game",
                                    text_color=self.text_color,
                                    font=self.font_button,
                                    # fg_color="#808080",
                                    border_width=1,
                                    border_color=("#DDDDDD", "black"),
                                    command=self.move_game_panel)

        self.button.place(relx=0.25,
                          rely=0.45,
                          anchor="center")
        # encrypted button
        self.button = ctk.CTkButton(self,
                                    text="Cryptage",
                                    text_color=self.text_color,
                                    font=self.font_button,
                                    # fg_color="#808080",
                                    border_width=1,
                                    border_color=("#DDDDDD", "black"),
                                    command=self.move_encryption_panel)

        self.button.place(relx=0.75,
                          rely=0.45,
                          anchor="center")

    def resource(self, relative_path):
        base_path = getattr(
            sys,
            '_MEIPASS',
            os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def reset_encryption_panel(self):
        self.encryption_panel.destroy()
        self.encryption_panel = EncryptionPanel(self, 1.0, 0.5, self.font_button, self.text_color)
        self.move_encryption_panel()

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


