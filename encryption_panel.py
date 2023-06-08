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
        self.win = master
        self.open_file_button = ctk.CTkButton(self,
                                              text='1. Open',
                                              text_color=color,
                                              font=font,
                                              fg_color="#A52D24",
                                              corner_radius=5,
                                              width=140,
                                              height=28,
                                              hover_color="#82231C",
                                              command=self.popup_open_file)
        self.open_file_button.place(anchor="n", relx=0.5, rely=0.1)

        # INPUT PATH
        self.path_label = ctk.CTkLabel(self,
                                       text="Fichier: ")
        self.path_label.place(anchor="n", relx=0.2, rely=0.25)

        self.path_var = tk.StringVar(value="Chemin du fichier")

        self.path_entry = ctk.CTkEntry(self,
                                       textvariable=self.path_var,
                                       )
        self.path_entry.place(anchor="n", relx=0.5, rely=0.25, relwidth=0.5)

        self.path_var.trace("w", self.check_path)

        # KEY
        self.key_label = ctk.CTkLabel(self,
                                      text="Clé: ")
        self.key_label.place(anchor="n", relx=0.2, rely=0.40)

        self.key_var = tk.StringVar(value=self.set_key())

        self.key_entry = ctk.CTkEntry(self,
                                      textvariable=self.key_var,
                                      )

        self.key_entry.place(anchor="n", relx=0.475, rely=0.40, relwidth=0.45)

        self.key_var.trace("w", self.check_key)
        # GENERATE KEY
        self.generate_button = ctk.CTkButton(self,
                                             text=u"\U000027F2",  # loop arrow
                                             text_color=("black", "#E0E0E0"),
                                             fg_color="transparent",
                                             hover_color="green",
                                             border_width=1,
                                             font=("default", 15, "bold"),
                                             width=30,
                                             command=self.update_key_entry)
        self.generate_button.place(anchor="n", relx=0.725, rely=0.40)

        # CRYPT
        self.encrypt_button = ctk.CTkButton(self,
                                            text='2. Chiffrer',
                                            text_color=color,
                                            font=font,
                                            fg_color="#A52D24",
                                            corner_radius=5,
                                            width=120,
                                            height=28,
                                            hover=False,
                                            hover_color="#82231C",
                                            state="disabled",
                                            command=self.encrypt_file)

        self.encrypt_button.place(anchor="n", relx=0.335, rely=0.55)

        # OR
        self.or_label = ctk.CTkLabel(self,
                                     text="OU")
        self.or_label.place(anchor="n", relx=0.5, rely=0.55)

        # "DECRYPT"
        self.decrypt_button = ctk.CTkButton(self,
                                            text='2. Déchiffrer',
                                            text_color=color,
                                            font=font,
                                            fg_color="#A52D24",  # red ok #B53127 /
                                            corner_radius=5,
                                            width=120,
                                            height=28,
                                            hover=False,
                                            hover_color="#82231C",
                                            state="disabled",
                                            command=self.decrypt_file)

        self.decrypt_button.place(anchor="n", relx=0.665, rely=0.55)

        # LABEL OUTPUT
        self.path_label = ctk.CTkLabel(self,
                                       text="Sortit: ")
        self.path_label.place(anchor="n", relx=0.2, rely=0.7)

        # OUTPUT PATH
        self.output_path_var = tk.StringVar(value="Chemin générer par défaut")
        self.output_path_entry = ctk.CTkEntry(self,
                                              textvariable=self.output_path_var,
                                              )
        self.output_path_entry.place(anchor="n", relx=0.475, rely=0.7, relwidth=0.45)

        # PREVIEW BUTTON
        self.preview_button = ctk.CTkButton(self,
                                            text=u"\U0001F441",  # œil
                                            text_color=("black", "#E0E0E0"),
                                            fg_color="transparent",
                                            hover_color="green",
                                            border_width=1,
                                            font=("default", 15, "bold"),
                                            width=30,
                                            command=self.display_popup_preview)
        self.preview_button.place(anchor="n", relx=0.725, rely=0.7)

        # SAVE
        self.save_button = ctk.CTkButton(self,
                                         text='3. Sauvegarder',
                                         text_color=color,
                                         font=font,
                                         fg_color="#A52D24",  # red ok #B53127 /
                                         corner_radius=5,
                                         width=120,
                                         height=28,
                                         hover_color="#82231C",
                                         state="disabled",
                                         command=self.popup_save)

        self.save_button.place(anchor="center", relx=0.5, rely=0.9)

        # RESET
        self.reset = ctk.CTkButton(self,
                                   text='Reset',
                                   text_color=("black", "#E0E0E0"),
                                   font=font,
                                   hover_color="green",
                                   border_width=1,
                                   fg_color="transparent",  # red ok #B53127 /
                                   corner_radius=5,
                                   width=20,
                                   height=28,
                                   command=self.win.reset_encryption_panel,
                                   )
        self.reset.place(anchor="center", relx=0.725, rely=0.9)

        # CRYPT OBJECT
        self.file = Encryption(self, self.path_var.get(), self.key_var.get())
        # WINDOW PREVIEW
        self.preview_popup = None

    def encrypt_file(self):
        """
        generate new path
        if potential error, open popup for user to choose
        cancel: don't do anything
        valid: encrypt file + freeze entry and button
        """
        output_path = self.file.generate_output_path()
        if output_path is not None:
            self.output_path_var.set(output_path)
            self.file.output_txt = self.file.encryption()
            self.change_state_after_crypt()

    def decrypt_file(self):
        """
        generate new path
        if potential error, open popup for user to choose
        cancel: don't do anything
        valid: decrypt file + freeze entry and button
        """
        output_path = self.file.generate_output_path(encrypt=False)
        if output_path is not None:
            self.output_path_var.set(output_path)
            self.file.output_txt = self.file.encryption(reverse=True)
            self.change_state_after_crypt()

    def change_state_after_crypt(self):
        """
        DISABLE:
        path_entry
        key_entry
        crypt button
        decrypt button
        ENABLE:
        save button
        """
        self.key_entry.configure(state="disabled")
        self.path_entry.configure(state="disabled")
        self.output_path_entry.configure(state="disabled")
        self.encrypt_button.configure(state="disabled")
        self.decrypt_button.configure(state="disabled")
        self.save_button.configure(state="normal")

        # focus end of string in entry
        i = len(self.output_path_var.get())
        self.output_path_entry.xview(i)

    def display_popup_preview(self):
        """
        display popup preview with new text
        !!! "bug" with top level: don't display in front properly !!!
        !!! check update !!!
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
        """
        check strings to enable encrypt and decrypt buttons
        """
        valide_key = len(self.key_var.get()) > 0
        valide_path = os.path.exists(self.path_var.get())
        if valide_key and valide_path:
            self.encrypt_button.configure(state="normal",
                                          hover=True,
                                          hover_color="green")

            self.decrypt_button.configure(state="normal",
                                          hover=True,
                                          hover_color="green")

        else:
            self.decrypt_button.configure(state="disabled")
            self.encrypt_button.configure(state="disabled")

    @staticmethod
    def set_key():
        """
        generate random encryption key with 10 upper letters
        """
        new_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))

        return new_key

    def update_key_entry(self):
        self.key_var.set(self.set_key())

    # noinspection PyUnusedLocal
    def check_key(self, *args):
        """
        check validity of key every time there is a change in text entry
        """
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

        if new_key != key:
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
        self.check_key()
        self.check_to_enable_button()

    def popup_open_file(self):
        """
        open current directory by default
        return file path
        """
        path = fd.askopenfilename(initialdir=f"{os.getcwd()}",  # "/" means root directory
                                  title="Selection file",
                                  filetypes=[("Text files", "*.txt")])

        self.path_var.set(path)

    @staticmethod
    def popup_warning(option):
        if option == "crypt":
            msg = "Le fichier semble:\n DEJA CRYPTER\n\n êtes vous sur de vouloir continuer?"
        elif option == "decrypt":
            msg = "Le fichier semble:\n DEJA DECRYPTER\n\n êtes vous sur de vouloir continuer?"
        elif option == "not":
            msg = "Le fichier ne semble:\n PAS CRYPTER\n\n êtes vous sur de vouloir continuer?"
        else:
            msg = "erreur fatal, relancer l'application"

        msg = CTkMessagebox(title="Warning",
                            message=msg,
                            icon="warning",
                            option_1="Annuler",
                            option_2="Continuer",
                            cancel_button="none")

        if msg.get() == "Annuler":
            return False
        if msg.get() == "Continuer":
            return True

    def popup_save(self):
        """
        popup window to choose directory and file name just before saving
        """
        path = os.getcwd().replace("\\", "/")
        file_name = self.file.output_path.replace(path, "").replace("/", "").replace(".txt", "")
        path = fd.asksaveasfilename(initialdir=f"{os.getcwd()}",  # "/" means root directory
                                    initialfile=file_name,
                                    filetypes=[("Text files", "*.txt")],
                                    title="Sauvegarde")

        if path:
            self.file.save()
