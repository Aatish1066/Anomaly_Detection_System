import pandas as pd
import os


folder_path = os.path.join("C:","Users","aatis","PycharmProjects","pythonProject1", "Dataset", "input", "data")
all_data = pd.DataFrame()  # Create an empty DataFrame to store concatenated data

for filename in os.listdir("C:/Users/aatis/PycharmProjects/pythonProject1/Dataset/input/data"):
    if filename.endswith(".csv"):
        file_path = os.path.join("C:/Users/aatis/PycharmProjects/pythonProject1/Dataset/input/data", filename)
        # Create the full file path
        data = pd.read_csv(file_path)  # Read CSV file
        all_data = pd.concat([all_data, data], ignore_index=True)  # Concatenate data to the main DataFrame
        #os.remove(file_path)

folder_path_processed=os.path.join("C:/Users/aatis/PycharmProjects/pythonProject1/Dataset/preprocessed_input")
# Save preprocessed data to a new CSV file
preprocessed_file_path = os.path.join(folder_path_processed, "preprocessed_data.csv")
all_data.to_csv(preprocessed_file_path, index=False)
