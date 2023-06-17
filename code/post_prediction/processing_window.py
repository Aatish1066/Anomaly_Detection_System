import customtkinter
from model_interfaces import modelexecution
from tkinter import END, scrolledtext
import tkinter as tk

from model_interfaces.modelexecution import load
from post_prediction import output_page


class ResultWindow(customtkinter.CTk):
    def on_predict_normal(self):
        input_text_a, input_text_n = load()  # Assuming load() returns a tuple of strings
        return input_text_n

    def on_predict_anomaly(self):
        input_text_a, input_text_n = load()  # Assuming load() returns a tuple of strings
        return input_text_a

    def __init__(self):
        super().__init__()
        self.title("Anomaly Detection")
        self.geometry("600x600")

        # Report window
        label1 = customtkinter.CTkLabel(self, text="Results: anomalous", text_color="light blue", anchor="w",
                                        font=("Helvetica", 14, "normal"))
        label1.pack()
        self.textbox1 = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.textbox1.configure(foreground="red")
        self.textbox1.pack(expand=tk.YES, fill=tk.BOTH)

        # Insert input_text into the CTkScrolledText widget
        self.textbox1.insert(END, self.on_predict_anomaly())

        # Report window
        label2 = customtkinter.CTkLabel(self, text="Results: normal", text_color="light blue", anchor="w",
                                        font=("Helvetica", 14, "normal"))
        label2.pack()

        # Disable editing in the CTkScrolledText widget
        self.textbox1.config(state=tk.DISABLED)
        self.textbox2 = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.textbox2.configure(foreground="green")
        self.textbox2.pack(expand=tk.YES, fill=tk.BOTH)

        # Insert input_text into the CTkScrolledText widget
        self.textbox2.insert(END, self.on_predict_normal())

        # Disable editing in the CTkScrolledText widget
        self.textbox2.config(state=tk.DISABLED)




