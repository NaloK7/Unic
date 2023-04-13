import tkinter as tk

import game_window as gm


class Master_win(tk.Tk):
    """
    fenetre principal du projet Unique
    """

    def __init__(self):
        # creer un objet Tk
        super().__init__()
        # self.eval('tk::PlaceWindow . center')
        # taille de la fenetre
        self.geometry("500x200+600+400")

        # nom de la fenetre
        self.title("Unique")

        # bar de menu principal
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        # sous-menu "aide" cascade:
        # "about unique"
        about = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Aide", menu=about)
        about.add_command(label="about Unique")  # AJOUT COMMANDE AFFICHE INFO
        # frame: titre
        self.frame_title = tk.Frame(self)
        self.frame_title.pack()
        # contenu
        self.label_title = tk.Label(
            self.frame_title, text="Bienvenue sur:\nUnique",
            font=("Reem Kufi", 20)
        )
        self.label_title.pack()

        # frame bouton
        self.frame_button = tk.Frame(self)
        self.frame_button.pack()
        # bouton JEU
        self.button_game = tk.Button(
            self.frame_button, text="JEU", command=self.display_window_game
        )
        self.button_game.pack(side="left")
        # boutton cryptage
        self.button_crypt_file = tk.Button(
            self.frame_button, text="Cryptage",
            command=self.display_window_game
        )
        self.button_crypt_file.pack(side="left")

        self.mainloop()

    def display_window_game(self):
        self.window_game = gm.Game_window(self)
