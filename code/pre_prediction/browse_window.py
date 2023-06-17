import customtkinter
from tkinter import END
from cmand_interface import browse_input_file
from post_prediction.processing_window import ResultWindow
class BrowseWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Anomaly Detection")

        # Create a label
        label = customtkinter.CTkLabel(self, text="Select File .pcap file for  analysis:",text_color="light blue",font=("Helvetica", 14, "normal"))
        label.grid(row=0, column=0, sticky="w", padx=20, pady=10)

        # Create a button to open file dialog
        button = customtkinter.CTkButton(self, text="Browse", command=self.on_browse_button_click, hover_color="crimson")
        button.grid(row=1, column=0, sticky="w", padx=20)

        # Report window
        label1 = customtkinter.CTkLabel(self, text="Report:", text_color="light blue", anchor="w",font=("Helvetica", 14, "normal"))
        label1.grid(row=2, column=0, sticky="w", padx=20, pady=10)
        self.textbox1 = customtkinter.CTkTextbox(self, width=600, corner_radius=0)
        self.textbox1.configure(state="disabled")
        self.textbox1.grid(row=3, column=0, sticky="w", padx=20)
        # Detect button
        button_detect = customtkinter.CTkButton(self, text="Detect", command=self.on_detect_button_click, hover_color="green")
        button_detect.grid(row=4, column=0, sticky="e", padx=20,pady=20)

        # Clear button
        button_clear = customtkinter.CTkButton(self, text="Clear", command=self.clear_report, hover_color="red")
        button_clear.grid(row=4, column=0, sticky="w", padx=20,pady=20)

    def on_browse_button_click(self):
        # Function to handle Browse button click event
        file_path = browse_input_file()
        # Update the report text box with the selected file path
        self.textbox1.configure(state='normal')
        self.textbox1.insert(END, file_path+'has been added and processed\n')
        self.textbox1.configure(state='disabled')

    def on_detect_button_click(self):
        # Function to handle Detect button click event
        # Add your detection logic here
        result= ResultWindow()
        self.destroy()
        result.mainloop()

       # result.update()

    def clear_report(self):
        self.textbox1.configure(state='normal')
        self.textbox1.delete(1.0, END)
        self.textbox1.configure(state='disabled')


