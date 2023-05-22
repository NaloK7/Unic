import tkinter as tk
import game_window as gm
from cryptic import Cryptic


class MasterWindow(tk.Tk):
    """
    Main window of project
    """

    def __init__(self):
        # create a tkinter object
        super().__init__()
        # self.eval('tk::PlaceWindow . center')
        # size and placement on screen
        self.geometry("700x500")
        # self.resizable(width=False, height=False)
        # window's name
        self.title("Unique")

        # menu bar object
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        # menu "aide"
        # under menu "about unique"
        about = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Aide", menu=about)
        about.add_command(label="about Unique")  # ADD COMMAND TO DISPLAY "ABOUT"
        # frame: titre
        self.frame_title = tk.Frame(self)
        self.frame_title.pack()

        self.label_title = tk.Label(
            self.frame_title, text="Bienvenue sur:\nUnique",
            font=("Reem Kufi", 20)
        )
        self.label_title.pack()

        # frame button
        self.frame_button = tk.Frame(self)
        self.frame_button.pack()
        # button JEU
        self.button_game = tk.Button(
            self.frame_button, text="JEU", command=self.display_window_game
        )
        self.button_game.pack(side="left")
        # crypto button
        self.button_crypt_file = tk.Button(
            self.frame_button, text="Cryptage",
            command=self.display_encryption
        )
        self.button_crypt_file.pack(side="left")

        self.mainloop()

    def display_window_game(self):
        game_win = gm.GameChoiceWindow(self)
        return game_win

    def display_encryption(self):
        crypt_win = Cryptic()
        return crypt_win
