from slide_panel import SlidePanel
import customtkinter as ctk


class GamesButton(SlidePanel):
    def __init__(self, master, start, end, font, text_color):
        super().__init__(master, start, end)
        # morpion button
        self.morpion_button = ctk.CTkButton(self,
                                            text='Morpion',
                                            text_color=text_color,
                                            font=font,
                                            fg_color="#A52D24",  # red ok #B53127 /
                                            corner_radius=5,
                                            width=140,
                                            height=28,
                                            hover_color="green",
                                            command=master.run_morpion,
                                            )
        self.morpion_button.place(anchor="n", relx=0.18, rely=0.1)
        # puissance 4 button
        self.puissance_button = ctk.CTkButton(self,
                                              text='Puissance 4',
                                              text_color=text_color,
                                              font=font,
                                              fg_color="#A52D24",
                                              corner_radius=5,
                                              width=140,
                                              height=28,
                                              hover_color="green",
                                              command=master.run_puissance4,
                                              )
        self.puissance_button.place(anchor="n", relx=0.5, rely=0.1)
        # snake button ICW
        self.snake_button = ctk.CTkButton(self,
                                          text='Snake',
                                          text_color=text_color,
                                          font=font,
                                          fg_color="#A52D24",
                                          corner_radius=5,
                                          width=140,
                                          height=28,
                                          hover_color="green",
                                          command=master.run_morpion,
                                          )
        self.snake_button.place(anchor="n", relx=0.82, rely=0.1)