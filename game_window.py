import tkinter as tk
from tkinter import Toplevel
import morpion as mp


class Game_window(Toplevel):
    """
    lance la fenetre de choix de jeu
    """

    def __init__(self, master):
        # creer une nouvelle fenetre
        Toplevel.__init__(self, master)
        self.master = master
        # cache la fenetre principale
        self.master.withdraw()
        # si la fenetre est ferme declenche la func
        self.bind("<Destroy>", self.on_destroy)

        self.geometry("500x200+600+400")
        # titre
        self.title("Choix du jeu")
        self.frame_title = tk.Frame(self)
        self.frame_title.pack()
        self.label_title = tk.Label(
            self.frame_title, text="Faite votre choix", font=("Reem Kufi", 20)
        )
        self.label_title.pack()

        # boutton
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
        lorsque la fenetre courante est fermée
        affiche a la fenetre principale
        """
        if event.widget == self:
            self.master.deiconify()

    def display_morpion(self):
        self.window_game = mp.Morpion(self)
