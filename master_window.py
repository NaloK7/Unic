import tkinter as tk
import game_window as gm


class Master_win(tk.Tk):
    """
    fenetre principal du projet Unique
    """

    def __init__(self):
        # creer un objet Tk
        super().__init__()
        # taille de la fenetre
        self.geometry("500x500")
        # nom de la fenetre
        self.title("Unique")

        # bar de menu principal
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        # sous-menu "aide" cascade:
        # "about unique"
        about = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Aide", menu=about)
        about.add_command(label="about Unique")
        # frame: titre
        self.frame_title = tk.Frame(self)
        self.frame_title.pack()
        # contenu
        self.label_title = tk.Label(
            self.frame_title, text="Bienvenue sur Unique", font=("Reem Kufi", 20)
        )
        self.label_title.pack()

        # bouton de jeu
        self.frame_button_game = tk.Frame(self)
        self.frame_button_game.pack()

        self.button_game = tk.Button(
            self.frame_button_game, text="JEU", command=self.display_window_game
        )
        self.button_game.pack()
        self.mainloop()

    def display_window_game(self):
        self.window_game = gm.game_window(self)
