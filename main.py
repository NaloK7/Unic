# coding: utf-8

import customtkinter as ctk
import pygame
import tkinter.filedialog as fd
import tkinter as tk
from Morpion import MorpionGame as mg
from Puissance_4 import Puissance4Game as pg
from file_menu import FileMenu
from slide_panel import SlidePanel
import string
import random
import os


# import tkinter as tk


# import os


class WUnique(ctk.CTk):
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

        self.file_menu = FileMenu(self, 20)

        # GAME PANEL
        self.game_panel = SlidePanel(self, 1.0, 0.6)

        # morpion button
        self.morpion_button = ctk.CTkButton(self.game_panel,
                                            text='Morpion',
                                            font=("default", 12, "bold"),
                                            fg_color="#A52D24",  # red ok #B53127 /
                                            corner_radius=5,
                                            width=140,
                                            height=28,
                                            hover_color="green",
                                            command=self.run_morpion).place(anchor="n", relx=0.18, rely=0.1)
        # puissance 4 button
        self.puissance_button = ctk.CTkButton(self.game_panel,
                                              text='Puissance 4',
                                              font=("default", 12, "bold"),
                                              fg_color="#A52D24",
                                              corner_radius=5,
                                              width=140,
                                              height=28,
                                              hover_color="green",
                                              command=self.run_puissance4).place(anchor="n", relx=0.5, rely=0.1)
        # snake button ICW
        self.snake_button = ctk.CTkButton(self.game_panel,
                                          text='Snake',
                                          font=("default", 12, "bold"),
                                          fg_color="#A52D24",
                                          corner_radius=5,
                                          width=140,
                                          height=28,
                                          hover_color="green",
                                          command=self.run_morpion).place(anchor="n", relx=0.82, rely=0.1)

        # ENCRYPTION PANEL
        self.encryption_panel = SlidePanel(self, 1.0, 0.5)
        # encrypt button
        self.open_file_button = ctk.CTkButton(self.encryption_panel,
                                              text='1. Open',
                                              font=("default", 12, "bold"),
                                              fg_color="#A52D24",  # red ok #B53127 /
                                              corner_radius=5,
                                              width=140,
                                              height=28,
                                              hover_color="green",
                                              command=self.popup_askopenfilename)
        self.open_file_button.place(anchor="n", relx=0.5, rely=0.1)

        # make frame to englobe next widgets
        # "Fichier entré"
        self.file_label = ctk.CTkLabel(self.encryption_panel,
                                       text="Fichier: ")
        self.file_label.place(anchor="n", relx=0.2, rely=0.25)

        self.file_path = tk.StringVar(value="Chemin du fichier")

        self.file_entry = ctk.CTkEntry(self.encryption_panel,
                                       textvariable=self.file_path,
                                       validate="key",
                                       )
        self.file_entry.place(anchor="n", relx=0.5, rely=0.25, relwidth=0.5)

        # bind any key release to check validity textvariable in file_entry
        self.file_entry.bind("<KeyRelease>", self.check_path)

        # "Clé
        self.key_label = ctk.CTkLabel(self.encryption_panel,
                                      text="Clé: ")
        self.key_label.place(anchor="n", relx=0.2, rely=0.40)

        self.key_var = tk.StringVar(value=self.set_key())

        self.key_entry = ctk.CTkEntry(self.encryption_panel,
                                      textvariable=self.key_var,
                                      )

        self.key_entry.place(anchor="n", relx=0.475, rely=0.40, relwidth=0.45)
        # self.key_entry.bind("<KeyRelease>", self.key_not_empty)
        self.generate_button = ctk.CTkButton(self.encryption_panel,
                                             text=u"\U000027F2",  # loop arrow
                                             fg_color="transparent",
                                             hover_color="green",
                                             border_width=1,
                                             font=("default", 15, "bold"),
                                             width=30,
                                             command=self.update_key_entry)
        self.generate_button.place(anchor="n", relx=0.725, rely=0.40)

        # "Chiffrer"
        self.encrypt_button = ctk.CTkButton(self.encryption_panel,
                                            text='2. Chiffrer',
                                            font=("default", 12, "bold"),
                                            fg_color="#A52D24",  # red ok #B53127 /
                                            corner_radius=5,
                                            width=120,
                                            height=28,
                                            hover_color="green",
                                            state="disabled",
                                            command=self.popup_askopenfilename)

        self.encrypt_button.place(anchor="n", relx=0.335, rely=0.55)

        # label between buttons
        self.or_label = ctk.CTkLabel(self.encryption_panel,
                                     text="OU")
        self.or_label.place(anchor="n", relx=0.5, rely=0.55)
        # "Déchiffrer"
        self.decrypt_button = ctk.CTkButton(self.encryption_panel,
                                            text='2. Déchiffrer',
                                            font=("default", 12, "bold"),
                                            fg_color="#A52D24",  # red ok #B53127 /
                                            corner_radius=5,
                                            width=120,
                                            height=28,
                                            hover_color="green",
                                            state="disabled",
                                            command=self.popup_askopenfilename)

        self.decrypt_button.place(anchor="n", relx=0.665, rely=0.55)

        # label output
        self.file_label = ctk.CTkLabel(self.encryption_panel,
                                       text="Sortit: ")
        self.file_label.place(anchor="n", relx=0.2, rely=0.7)

        # "Fichier sortit"
        self.output_path = ctk.CTkEntry(self.encryption_panel)
        self.output_path.place(anchor="n", relx=0.475, rely=0.7, relwidth=0.45)

        # preview button
        self.preview_button = ctk.CTkButton(self.encryption_panel,
                                            text=u"\U0001F441",  # œil
                                            fg_color="transparent",
                                            hover_color="green",
                                            border_width=1,
                                            font=("default", 15, "bold"),
                                            width=30,
                                            command=self.update_key_entry)
        self.preview_button.place(anchor="n", relx=0.725, rely=0.7)

        # save
        self.save_button = ctk.CTkButton(self.encryption_panel,
                                         text='3. Sauvegarder',
                                         font=("default", 12, "bold"),
                                         fg_color="#A52D24",  # red ok #B53127 /
                                         corner_radius=5,
                                         width=120,
                                         height=28,
                                         hover_color="green",
                                         command=self.popup_askopenfilename)

        self.save_button.place(anchor="n", relx=0.5, rely=0.85)

        # main game button
        self.button = ctk.CTkButton(self,
                                    text="Game",
                                    font=("default", 12, "bold"),
                                    # fg_color="#808080",
                                    # border_width=1,
                                    # border_color=("black", "white"),
                                    command=self.move_game_panel)

        self.button.place(relx=0.25,
                          rely=0.4,
                          anchor="center")
        # encrypted button
        self.button = ctk.CTkButton(self,
                                    text="Cryptage",
                                    font=("default", 12, "bold"),
                                    # fg_color="#808080",
                                    # border_width=1,
                                    # border_color=("black", "white"),
                                    command=self.move_encryption_panel)

        self.button.place(relx=0.75,
                          rely=0.4,
                          anchor="center")
        # check path file
        self.file_entry.configure(validate="key",
                                  validatecommand=(self.encryption_panel.register(self.check_path)),
                                  )

        # check key
        self.key_entry.configure(validate="key",
                                 validatecommand=(self.encryption_panel.register(self.key_not_empty)),
                                 )

    def are_both_valide(self):
        if self.key_not_empty() and self.check_path():
            self.decrypt_button.configure(state="enabled")
            self.encrypt_button.configure(state="enabled")
        else:
            self.decrypt_button.configure(state="disabled")
            self.encrypt_button.configure(state="disabled")
    def set_key(self):
        """
        generate random encryption key of 10 upper letters
        """
        new_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))

        return new_key

    def update_key_entry(self):
        self.key_var.set(self.set_key())

    def key_not_empty(self):
        if self.key_entry.get() != "":
            print("key not empty")
            return True
        else:
            print("key empty")
            return False

    def check_path(self, *path):
        """
        check validity of path
        enable/disable "encrypt"/"decrypt" buttons depending on validity
        change "open" button colour depending on validity
        """
        path = self.file_entry.get()
        path_exist = os.path.exists(path)
        if path_exist:
            # validation mark instead of green button ?

            self.open_file_button.configure(fg_color="green")

            path = self.file_path.get()
            self.file_path.set(path)
            print("path valid")
            return True

        elif self.file_path.get() == "":
            path = "Aucun fichier sélectionner"
            self.file_path.set(path)
        else:
            path = self.file_path.get()
            self.file_path.set(path)
        print('path not valid')
        return False

    def popup_askopenfilename(self):
        """
        open current directory by default
        return file path
        """
        path = fd.askopenfilename(initialdir=f"{os.getcwd()}",  # "/" means root directory
                                  title="Selection file",
                                  filetypes=[("Text files", "*.txt")])
        # set choose path to text variable
        self.file_path.set(path)
        # check validity of path
        self.check_path(path)
        self.are_both_valide()

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


test = WUnique()
test.mainloop()
