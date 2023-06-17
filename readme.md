# Anomaly Detection in PCAP Files with Machine Learning and GUI

Welcome to the Anomaly Detection in PCAP Files project! This project utilizes Python and machine learning techniques to detect anomalies in PCAP files, which are commonly used for network packet captures. With the added benefit of a graphical user interface (GUI), this project provides an intuitive and user-friendly experience for analyzing network traffic and identifying potential anomalies.


## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

Detecting anomalies in network traffic is crucial for identifying potential security threats, performance issues, or unusual behavior. This project leverages machine learning algorithms to analyze PCAP files and highlight any suspicious patterns or deviations from normal network behavior. Additionally, the inclusion of a GUI simplifies the process, enabling users to interactively explore and visualize the detected anomalies.

## Features

- **Anomaly Detection**: The project employs machine learning algorithms to identify anomalies in PCAP files, such as unusual traffic patterns, network attacks, or abnormal behaviors.
- **Interactive GUI**: The graphical user interface provides an intuitive environment to load PCAP files, visualize network traffic, and explore the detected anomalies.
- **Statistical Analysis**: The project performs statistical analysis on network traffic features to establish baseline behavior and identify deviations from it.
- **Customizable Settings**: Users have the flexibility to adjust various settings, including anomaly detection thresholds, feature selection, and visualization preferences.
- **Detailed Reports**: The project generates detailed reports summarizing the detected anomalies, including timestamps, source/destination IP addresses, packet details, and severity levels.

## Installation

To use this project on your local machine, follow these steps:

1. Clone the repository to your desired location:

   ```bash
   git clone https://github.com/your-username/anomaly-detection-pcap.git
   ```

2. Navigate to the project directory:

   ```bash
   cd anomaly-detection-pcap
   ```

3. Install the required dependencies. It is recommended to set up a virtual environment before installing dependencies:

  


4. Download and install the necessary machine learning models if they are not included in the repository. Follow the instructions provided in the `models/README.md` file.

5. Launch the GUI application:

   ```bash
   python main_page.py
   ```

6. The GUI window will open, allowing you to load PCAP files, configure settings, and explore the detected anomalies.

## Usage

1. Launch the GUI application by running `main.py` as mentioned in the installation steps.

2. Click on the "Load PCAP" button to import a PCAP file for analysis.

3. Once the PCAP file is loaded, the application will perform anomaly detection and generate visualizations and reports.

4. Explore the various tabs and options in the GUI to view network traffic statistics, anomaly details, and interactive visualizations.

5. Adjust the settings as needed to customize the anomaly detection process and visualization preferences.

6. Analyze the detected anomalies and use the provided information to investigate potential security threats or abnormal network behaviors.

7. Generate and export detailed reports for further analysis or sharing with relevant stakeholders.

## Contributing

Contributions to this project are highly appreciated. If you have any ideas for improvements, new features, bug fixes, or want to contribute in any other way you are free to do so how ever do leave a star.
## external sources used
This project uses Hikari-2021 dataset for trainig model and it uses CICFlowmeter to capture pcap files.Which are both opensource. 
