import customtkinter

from browse_window import BrowseWindow


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x320")
        self.title("Anomaly Detection System")

        # Add widgets to app
        self.label = customtkinter.CTkLabel(self, text="Anomaly Detection System", text_color="light blue",
                                            anchor="n", font=("Helvetica", 14, "bold"))
        self.label.grid(row=0, column=6, padx=20, pady=10)
        self.textbox = customtkinter.CTkTextbox(master=self, width=600, corner_radius=0)
        self.textbox.grid(row=2, column=6, pady=10)
        self.textbox.insert("0.0", "Anomaly Detection System for HTTP Flow Data\n"
                                   "This system aims to detect anomalies in"
                                   " HTTP flow data, which includes capturing\n"
                                   " and analyzing network traffic to identify "
                                   "abnormal patterns or behaviors that could\n"
                                   " indicate potential security threats or"
                                   " suspicious activities.\nWith the increasing"
                                   " reliance on web applications and the\n"
                                   " ever-evolving landscape of cyber threats, effective anomaly detection is crucial\n"
                                   " for proactive threat detection and prevention. to process and analyze large\n"
                                   " volumes of HTTP flow data."
                                   "\nLeveraging historical traffic"
                                   "patterns and baselines, it identifies deviations\n"
                                   " and anomalies that may signify "
                                   "malicious activities, such as network scans,\n"
                                   " intrusion attempts, or data "
                                   "exfiltration."
                                   "\nDetected anomalies are flagged, and alerts or notifications are "
                                   "generated for further investigation and\n response by security teams."
                                   "The system "
                                   "\nemploys advanced machine learning algorithms, statistical"
                                   " analysis, and data \n"
                                   "visualization techniques The system's modular and extensible design allows for easy\n"
                                   " customization and integration with existing security infrastructure, making it \n"
                                   "scalable and adaptable to different network environments and security requirements.\n"
                                   "\nIt provides a valuable tool for enhancing network security posture and mitigating \n"
                                   "potential security risks by proactively identifying and responding to anomalous\n"
                                   " behaviors in HTTP flow data.\nAuthor: [Aatish Sharma , Animesh]\nRoll Numbers: [201536 ,201567]\n")
        self.button = customtkinter.CTkButton(self, text="OK", command=self.button_click, hover_color="crimson")
        self.button.grid(row=6, column=6, padx=20, pady=10)

    def button_click(self):
        app.destroy()
        browse_window = BrowseWindow()
        browse_window.mainloop()


# Create app window
app = App()
try:
    # Run the main event loop

    app.mainloop()

except KeyboardInterrupt:
    # Handle keyboard interrupt
    app.destroy()
