import customtkinter as ctk
import pygame
from Morpion import MorpionGame as mg
from Puissance_4 import Puissance4Game as pg


# import tkinter as tk


# import os


class WUnique(ctk.CTk):
    """
    encryption window
    """

    def __init__(self):
        super().__init__()
        # size
        self.geometry("700x500")
        # window name
        self.title("Unique")

        self.file_menu = FileMenu(self, 20)
        # game slide
        self.game_panel = SlidePanel(self, -0.3, 0.0)
        self.morpion_button = ctk.CTkButton(self.game_panel,
                                            text='Morpion',
                                            corner_radius=5,
                                            command=self.run_morpion)

        self.morpion_button.pack(padx=5,
                                 pady=5,
                                 )

        # main game button
        self.button = ctk.CTkButton(self,
                                    text="Game",
                                    command=self.game_panel.move_panel)

        self.button.place(relx=0.5,
                          rely=0.5,
                          anchor="center")

    def run_morpion(self):
        pygame.init()
        game = mg.Game(self)
        game.run()

    def run_puissance4(self):
        pygame.init()
        game = pg.GamePuissance4(self)
        game.run()


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        self.start_pos = start_pos  # -x
        self.end_pos = end_pos  # 0
        self.width = abs(start_pos - end_pos) + 0.03

        self.pos = self.start_pos
        self.is_hide = True
        self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
        self.arrow = ctk.CTkButton(self,
                                   text=">",
                                   width=20,
                                   corner_radius=0,
                                   height=self.cget("height"),
                                   fg_color="transparent",
                                   hover_color="#444444",
                                   command=self.move_panel)
        self.arrow.pack(side="right", fill="y")

    def move_panel(self):
        if self.is_hide:
            self.move_to_right()
        else:
            self.move_to_left()

    def move_to_left(self):
        if self.pos > self.start_pos:
            self.pos -= 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.move_to_left)
            self.arrow.configure(text=">")
        else:
            self.is_hide = True

    def move_to_right(self):
        if self.pos < self.end_pos:
            self.pos += 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.move_to_right)
            self.arrow.configure(text="<")
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
                                         )  # put self.options.set("   Fichier") in callback function
        self.options.place(x=0,
                           y=0,
                           )
        # "title" menu
        self.options.set("   Fichier")

        # appearance menu
        self.appearance_option = ctk.CTkOptionMenu(self.menu_frame,
                                                   width=110,
                                                   height=20,
                                                   corner_radius=0,
                                                   values=["Light", "Dark"],
                                                   # fg_color=("white", "black"),
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
        self.menu_frame.place(x=156,
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
