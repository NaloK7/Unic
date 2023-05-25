import customtkinter as ctk


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos: float, end_pos: float):
        super().__init__(master=parent, corner_radius=5, border_width=3, border_color="grey")
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.offset = 0.006
        self.height = abs(start_pos - end_pos) + self.offset

        self.pos = self.start_pos
        self.is_hide = True
        self.place_()

    def place_(self):
        self.place(rely=self.pos, relx=0.05, relwidth=0.9, relheight=self.height)

    def move_panel(self):
        if self.is_hide:
            self.move_up()
        else:
            self.move_down()

    def move_down(self):
        if self.pos < self.start_pos:
            self.pos += 0.015
            if self.pos > self.start_pos:
                self.pos = self.start_pos
            self.place_()
            self.after(10, self.move_down)

        else:
            self.is_hide = True

    def move_up(self):
        if self.pos > self.end_pos:
            self.pos -= 0.015
            if self.pos < self.end_pos:
                self.pos = self.end_pos
            self.place_()
            self.after(10, self.move_up)
        else:
            self.is_hide = False
