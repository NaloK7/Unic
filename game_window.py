import tkinter as tk
from tkinter import Toplevel


class game_window(Toplevel):
    """
    lance la fenetre principale dedie au jeu
    """

    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.master = master
        self.master.withdraw()
        self.bind("<Destroy>", self.on_destroy)

    def on_destroy(self, event):
        if event.widget == self:
            self.master.deiconify()
