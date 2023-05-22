import customtkinter as ctk
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

        self.file_menu = FileMenu(self)


class FileMenu:
    """
    Menu "Fichier"
    """

    def __init__(self, master):
        # menu bar
        self.menu_frame = ctk.CTkFrame(master,
                                       height=20,
                                       corner_radius=0,
                                       fg_color=("white", "black"))  # color of menu frame TODO
        self.menu_frame.place(relx=0,
                              rely=0,
                              relwidth=1)
        # help menu
        self.menu_bar = ctk.CTkOptionMenu(self.menu_frame,
                                          width=55,
                                          height=20,
                                          corner_radius=0,
                                          # dropdown_fg_color="white",
                                          # button_color=self.menu_frame.cget("fg_color"),
                                          # button_hover_color=("blue"),
                                          values=["Light", "Dark", "Aide"],
                                          command=self.optionmenu_callback,
                                          )
        self.menu_bar.place(x=0,
                            y=0, )
        self.menu_bar.set("Fichier")

    def optionmenu_callback(self, choice):
        if choice == "Light" or "Dark":
            self.change_appearance_to_light(choice)

    def change_appearance_to_light(self, choice):
        ctk.set_appearance_mode(choice)
        self.menu_bar.set("Fichier")


test = WUnique()
test.mainloop()
