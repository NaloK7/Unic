import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

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
                                         values=["About"],
                                         text_color="white",
                                         command=self.optionmenu_callback,
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
            self.change_appearance(choice)
        if choice == "About":
            self.options.set("   Fichier")
            self.popup_about()

    def change_appearance(self, choice):
        ctk.set_appearance_mode(choice)
        self.appearance_option.set("   Apparence")

    def popup_about(self):
        msg = CTkMessagebox(title="About",
                            message="V0.2",
                            cancel_button="none")
        msg.button_1.grid(row=2, column=2, sticky="news", padx=(0,10), pady=10)
