import customtkinter as ctk
import pygame
from Morpion import MorpionGame as mg
from Puissance_4 import Puissance4Game as pg
import tkinter.filedialog as fd
import tkinter as tk
# import os


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
        # snake button #TODO
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
        self.encryption_panel = SlidePanel(self, 1.0, 0.6)
        # encrypt button
        self.morpion_button = ctk.CTkButton(self.encryption_panel,
                                            text='Open',
                                            font=("default", 12, "bold"),
                                            fg_color="#A52D24",  # red ok #B53127 /
                                            corner_radius=5,
                                            width=140,
                                            height=28,
                                            hover_color="green",
                                            command=self.get_file_path).place(anchor="n", relx=0.5, rely=0.1)
        # todo make frame to englobe next four widgets
        self.file_label = ctk.CTkLabel(self.encryption_panel, text="Fichier: ").place(anchor="n", relx=0.2, rely=0.35)
        self.file_path = tk.StringVar(value="Chemin du fichier")

        # todo if self.file_path is not "Chemin du fichier": changer couleur bouton ouvrir

        self.file_entry = ctk.CTkEntry(self.encryption_panel, textvariable=self.file_path, state="disabled").place(anchor="n", relx=0.5, rely=0.35, relwidth=0.5)

        self.key_label = ctk.CTkLabel(self.encryption_panel, text="Clé: ").place(anchor="n", relx=0.2, rely=0.50)
        self.key_entry = ctk.CTkEntry(self.encryption_panel).place(anchor="n", relx=0.5, rely=0.50, relwidth=0.5)

        self.output_path = ctk.CTkEntry(self.encryption_panel).place(anchor="n", relx=0.5, rely=0.75, relwidth=0.5)
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

    def get_file_path(self):
        """
        return file path
        """
        path = fd.askopenfilename(initialdir="/",
                                  title="Selection file",
                                  filetypes=[("Text files", "*.txt")])
        self.file_path.set(path)
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


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos: float, end_pos: float):
        super().__init__(master=parent, corner_radius=5, border_width=3, border_color="grey")
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.height = abs(start_pos - end_pos) + 0.01

        self.pos = self.start_pos
        self.is_hide = True

        self.place(rely=self.pos, relx=0.05, relwidth=0.9, relheight=self.height)

    def move_panel(self):
        if self.is_hide:
            self.move_up()
        else:
            self.move_down()

    def move_down(self):
        if self.pos < self.start_pos:
            self.pos += 0.015
            self.place(rely=self.pos, relx=0.05, relwidth=0.9, relheight=self.height)
            self.after(10, self.move_down)

        else:
            self.is_hide = True

    def move_up(self):
        if self.pos > self.end_pos:
            self.pos -= 0.015
            self.place(rely=self.pos, relx=0.05, relwidth=0.9, relheight=self.height)
            self.after(10, self.move_up)
        else:
            self.is_hide = False


class FileMenu:
    """
    Menu "Fichier"
    """

    def __init__(self, master, height):
        # menu frame
        self.menu_frame = ctk.CTkFrame(master,
                                       height=height,
                                       corner_radius=0,
                                       fg_color=("white", "black"))
        self.menu_frame.place(x=0,
                              y=0,
                              relwidth=1)

        # inside menu
        self.options = ctk.CTkOptionMenu(self.menu_frame,
                                         width=85,
                                         height=20,
                                         corner_radius=0,
                                         values=["Aide"],
                                         text_color="white",
                                         )  # put self.options.set("   Fichier") in callback function
        self.options.place(x=0,
                           y=0,
                           )
        # "title" menu
        self.options.set("   Fichier")

        # appearance menu
        self.appearance_option = ctk.CTkOptionMenu(self.menu_frame,
                                                   width=90,
                                                   height=20,
                                                   corner_radius=0,
                                                   values=["Light", "Dark"],
                                                   text_color=("black", "white"),
                                                   fg_color=("white", "black"),
                                                   button_color=("white", "black"),
                                                   button_hover_color=("white", "black"),
                                                   command=self.optionmenu_callback,
                                                   )
        self.appearance_option.place(x=66,
                                     y=0,
                                     )
        self.appearance_option.set("   Apparence")

        # menu frame
        self.menu_frame = ctk.CTkFrame(self.menu_frame,
                                       height=20,
                                       corner_radius=0,
                                       fg_color=("white", "black"))
        self.menu_frame.place(x=145,
                              y=0,
                              relwidth=1)

    def optionmenu_callback(self, choice):
        if choice == "Light" or "Dark":
            self.change_appearance_to_light(choice)

    def change_appearance_to_light(self, choice):
        ctk.set_appearance_mode(choice)
        self.appearance_option.set("   Apparence")


test = WUnique()
test.mainloop()
