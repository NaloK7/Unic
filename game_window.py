import tkinter as tk
from tkinter import Toplevel
import morpion as mp
import pygame
from Morpion import MorpionGame


class GameChoiceWindow(Toplevel):
    """
    Game Choice Window
    """

    def __init__(self, master):
        """
        master: tkinter window
        """
        # new window TopLevel
        Toplevel.__init__(self, master)
        self.master = master
        # hide main window
        self.master.withdraw()
        # associate event with function
        self.bind("<Destroy>", self.on_destroy)

        self.geometry("500x200+600+400")
        # title
        self.title("Choix du jeu")
        self.frame_title = tk.Frame(self)
        self.frame_title.pack()
        self.label_title = tk.Label(
            self.frame_title, text="Faite votre choix", font=("Reem Kufi", 20)
        )
        self.label_title.pack()

        # button
        self.frame_button = tk.Frame(self)
        self.frame_button.pack()

        self.morpion_button = tk.Button(self.frame_button, text="MORPION", command=self.display_morpion)
        self.morpion_button.pack(side="left")

        self.puissance4_button = tk.Button(
            self.frame_button, text="PUISSANCE 4")
        self.puissance4_button.pack(side="left")

        self.motus_button = tk.Button(self.frame_button, text="MOTUS")
        self.motus_button.pack(side="left")

    def on_destroy(self, event):
        """
        re draw the main window
        """
        if event.widget == self:
            self.master.deiconify()

    def display_morpion(self):
        # self.window_game = mp.Morpion(self)
        pygame.init()
        # game_screen = pygame.display.set_mode((600,600))
        game = MorpionGame.Game(self)
        game.run()

        pygame.quit()
