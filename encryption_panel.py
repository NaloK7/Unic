import os
import random
import string
import tkinter.filedialog as fd
import customtkinter as ctk
from slide_panel import SlidePanel
import tkinter as tk
from cryptic import Encryption
from CTkMessagebox import CTkMessagebox


class EncryptionPanel(SlidePanel):
    def __init__(self, master, start, end, font, color):
        super().__init__(master, start, end)

        # encrypt button
        self.open_file_button = ctk.CTkButton(self,
                                              text='1. Open',
                                              text_color=color,
                                              font=font,
                                              fg_color="#A52D24",  # red ok #B53127 /
                                              corner_radius=5,
                                              width=140,
                                              height=28,
                                              hover_color="green",
                                              command=self.popup_open_file)
        self.open_file_button.place(anchor="n", relx=0.5, rely=0.1)

        # make frame to englobe next widgets
        # "Fichier entré"
        self.path_label = ctk.CTkLabel(self,
                                       text="Fichier: ")
        self.path_label.place(anchor="n", relx=0.2, rely=0.25)

        self.path_var = tk.StringVar(value="Chemin du fichier")
        # call func if string is modify
        self.path_var.trace("w", self.check_path)

        self.path_entry = ctk.CTkEntry(self,
                                       textvariable=self.path_var,
                                       )
        self.path_entry.place(anchor="n", relx=0.5, rely=0.25, relwidth=0.5)

        # "Clé
        self.key_label = ctk.CTkLabel(self,
                                      text="Clé: ")
        self.key_label.place(anchor="n", relx=0.2, rely=0.40)

        self.key_var = tk.StringVar(value=self.set_key())
        # call func if string is modify
        self.key_var.trace("w", self.check_key)

        self.key_entry = ctk.CTkEntry(self,
                                      textvariable=self.key_var,
                                      )

        self.key_entry.place(anchor="n", relx=0.475, rely=0.40, relwidth=0.45)
        self.generate_button = ctk.CTkButton(self,
                                             text=u"\U000027F2",  # loop arrow
                                             text_color=("black", "white"),
                                             fg_color="transparent",
                                             hover_color="green",
                                             border_width=1,
                                             font=("default", 15, "bold"),
                                             width=30,
                                             command=self.update_key_entry)
        self.generate_button.place(anchor="n", relx=0.725, rely=0.40)

        # "Chiffrer"
        self.encrypt_button = ctk.CTkButton(self,
                                            text='2. Chiffrer',
                                            text_color=color,
                                            font=font,
                                            fg_color="#A52D24",  # red ok #B53127 /
                                            corner_radius=5,
                                            width=120,
                                            height=28,
                                            hover=False,
                                            hover_color="green",
                                            state="disabled",
                                            command=self.encrypt_file)

        self.encrypt_button.place(anchor="n", relx=0.335, rely=0.55)

        # label between buttons
        self.or_label = ctk.CTkLabel(self,
                                     text="OU")
        self.or_label.place(anchor="n", relx=0.5, rely=0.55)
        # "Déchiffrer"
        self.decrypt_button = ctk.CTkButton(self,
                                            text='2. Déchiffrer',
                                            text_color=color,
                                            font=font,
                                            fg_color="#A52D24",  # red ok #B53127 /
                                            corner_radius=5,
                                            width=120,
                                            height=28,
                                            hover=False,
                                            hover_color="green",
                                            state="disabled",
                                            command=self.decrypt_file, )

        self.decrypt_button.place(anchor="n", relx=0.665, rely=0.55)

        # label output
        self.path_label = ctk.CTkLabel(self,
                                       text="Sortit: ")
        self.path_label.place(anchor="n", relx=0.2, rely=0.7)

        # "Fichier sortit"
        self.output_path_var = tk.StringVar(value="Chemin de sortit du fichier")
        self.output_path_entry = ctk.CTkEntry(self,
                                              textvariable=self.output_path_var,
                                              )
        self.output_path_entry.place(anchor="n", relx=0.475, rely=0.7, relwidth=0.45)

        # preview button
        self.preview_button = ctk.CTkButton(self,
                                            text=u"\U0001F441",  # œil
                                            text_color=("black", "white"),
                                            fg_color="transparent",
                                            hover_color="green",
                                            border_width=1,
                                            font=("default", 15, "bold"),
                                            width=30,
                                            command=self.display_popup_preview)
        self.preview_button.place(anchor="n", relx=0.725, rely=0.7)

        # save
        self.save_button = ctk.CTkButton(self,
                                         text='3. Sauvegarder',
                                         text_color=color,
                                         font=font,
                                         fg_color="#A52D24",  # red ok #B53127 /
                                         corner_radius=5,
                                         width=120,
                                         height=28,
                                         hover_color="green",
                                         command=self.save)

        self.save_button.place(anchor="n", relx=0.5, rely=0.85)

        self.file = Encryption(self, self.path_var.get(), self.key_var.get())

        self.preview_popup = None

    def encrypt_file(self):

        self.file.output_txt = self.file.encryption()
        self.output_path_var.set(self.file.generate_output_path())
        self.encrypt_button.configure(fg_color="green")
        self.path_entry.configure(state="disabled")
        self.key_entry.configure(state="disabled")
        self.decrypt_button.configure(state="disabled")
        # enable view end of string in entry
        i = len(self.output_path_var.get())
        self.output_path_entry.xview(i)

    def decrypt_file(self):

        # self.file = Encryption(self, self.path_var.get(), self.key_var.get())
        self.file.output_txt = self.file.encryption(reverse=True)
        self.output_path_var.set(self.file.generate_output_path(encrypt=False))
        self.decrypt_button.configure(fg_color="green")
        self.key_entry.configure(state="disabled")
        self.path_entry.configure(state="disabled")
        self.encrypt_button.configure(state="disabled")
        # enable view end of string in entry
        i = len(self.output_path_var.get())
        self.output_path_entry.xview(i)

    def display_popup_preview(self):
        """
        NEED CHECK IF BETTER SOLUTION IS FOUND TO DISPLAY POPUP IN TOPLEVEL
        """

        if self.file.state:
            if self.preview_popup is None or not self.preview_popup.winfo_exists():
                self.preview_popup = ctk.CTkToplevel(self)
                self.preview_popup.title("Preview")
                self.preview_popup.geometry("800x600")
                self.preview_popup.attributes("-topmost", True)
                self.preview_popup.after(20, self.preview_popup.focus_force)
                self.preview_popup.focus()
            else:
                self.preview_popup.attributes("-topmost", True)
                self.preview_popup.after(20, self.preview_popup.focus_force)
                self.preview_popup.focus()

            text = ctk.CTkTextbox(self.preview_popup,
                                  wrap="none")
            text.insert(1.0, self.file.output_txt)
            text.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            CTkMessagebox(self,
                          cancel_button="none",
                          title="OUPS",
                          message="CRYPTER ou DECRYPTER\navant de visualiser le résultat",
                          option_1="OK")

    # noinspection PyUnusedLocal
    def check_to_enable_button(self, *args):
        valide_key = len(self.key_var.get()) > 0
        valide_path = os.path.exists(self.path_var.get())
        if valide_key and valide_path:
            self.decrypt_button.configure(state="normal",
                                          hover=True,
                                          hover_color="green")

            self.encrypt_button.configure(state="normal",
                                          hover=True,
                                          hover_color="green")

        else:
            self.decrypt_button.configure(state="disabled")
            self.encrypt_button.configure(state="disabled")

    @staticmethod
    def set_key():
        """
        generate random encryption key of 10 upper letters
        """
        new_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))

        return new_key

    def update_key_entry(self):
        self.key_var.set(self.set_key())

    # noinspection PyUnusedLocal
    def check_key(self, *args):
        key = self.key_var.get()
        new_key = ""
        if len(key) > 0:
            if "La cle ne peu pas être vide" in key:
                key = key.replace("La cle ne peu pas être vide", "")
            for elem in key:
                if elem.isalpha():
                    new_key += elem.upper()
                else:
                    new_key += elem
            key = new_key
            self.key_entry.configure(border_color="green")
        else:
            if key == "":
                key = "La cle ne peu pas être vide"
                self.key_entry.configure(border_color="red")

        self.key_var.set(key)
        self.file.configure(key=self.key_var.get())

        self.check_to_enable_button()

    # noinspection PyUnusedLocal
    def check_path(self, *args):
        """
        check validity of path
        enable/disable "encrypt"/"decrypt" buttons depending on validity

        """
        path = self.path_var.get()
        path_exist = os.path.exists(path)

        if not path_exist:
            if path == "":
                path = "Aucun fichier sélectionner"
            elif "Aucun fichier sélectionner" in path:
                path = path.replace("Aucun fichier sélectionner", "")
            self.path_entry.configure(border_color="red")
        else:
            self.path_entry.configure(border_color="green")

        self.path_var.set(path)
        # enable view end of string in entry
        i = len(self.path_var.get())
        self.path_entry.xview(i)

        self.file.configure(input_path=path)
        self.check_to_enable_button()

    def popup_open_file(self):
        """
        open current directory by default
        return file path
        """
        path = fd.askopenfilename(initialdir=f"{os.getcwd()}",  # "/" means root directory
                                  title="Selection file",
                                  filetypes=[("Text files", "*.txt")])
        # set chosen path to text variable
        self.path_var.set(path)
        # check validity of path
        self.check_path(path)
        self.check_key()

    def show_checkmark(self):
        # Show some positive message with the checkmark icon
        CTkMessagebox(cancel_button="none",
                      message="Le fichier a été sauvegardé avec succès",
                      icon="check",
                      option_2="Thanks")

    def save(self):
        self.show_checkmark()
        self.file.save()
