import os
from tkinter import filedialog


# Function to browse and select input file
def browse_input_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Call function to process input file
        process_files(file_path)
        return str(file_path)
    else:
        return "No file "

# Function to process input file
def process_files(file_path):
    # Change directory to "j"
    os.chdir("J:")

    # Construct the path to the batch file
    batch_file_path = os.path.join("bin", "cfm")

    # Construct the path to the CSV output file

    csv_file_path = os.path.join("C:Users/aatis/PycharmProjects/pythonProject1/Dataset/input/data")

    # Run the batch file with the input file as input and the csv file as output
    command = f'{batch_file_path} {file_path} {csv_file_path}'
    os.system(command)
    print("Files processed successfully.")


