import customtkinter as ctk
import os

class Cryptic(ctk.CTk):
    """
    encryption window
    """
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Cryptic")
        self.mainloop()



# test = Cryptic()
# test