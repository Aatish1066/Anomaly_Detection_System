import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext
class OutputPage(ctk.CTkToplevel):
    def __init__(self,index, input_text):
        ctk.CTkToplevel.__init__(self)
        self.title("Output")

        # Create a Text widget
        self.textbox1 = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.textbox1.pack(expand=tk.YES, fill=tk.BOTH)

        # Insert input_text into the CTkScrolledText widget
        self.textbox1.insert(index, input_text)

        # Disable editing in the CTkScrolledText widget
        self.textbox1.config(state=ctk.DISABLED)


