import tkinter as tk
from tkinter import Toplevel


class Morpion(Toplevel):
    def __init__(self, game_master):
        Toplevel.__init__(self, game_master)
        self.game_master = game_master
        # cache la fenetre principale
        self.game_master.withdraw()
        # si la fenetre est ferme declenche la func
        self.bind("<Destroy>", self.on_destroy)

        self.geometry("500x200+600+400")
        # titre
        self.title("Morpion")
        self.frame_title = tk.Frame(self)
        self.frame_title.pack()
        self.label_title = tk.Label(
            self.frame_title, text="Morpion", font=("Reem Kufi", 20)
        )
        self.label_title.pack()

    def on_destroy(self, event):
        """
        lorsque la fenetre courante est fermée
        affiche a la fenetre principale
        """
        if event.widget == self:
            self.master.deiconify()
