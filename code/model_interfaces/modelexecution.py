import pandas as pd
import numpy as np
import tensorflow as tf
from pre_prediction import preprocess_input
model = tf.keras.models.load_model('C:/Users/aatis/PycharmProjects/pythonProject1/model_interfaces/model.h5')
def csv_to_string(file_path, delimiter=',', encoding='utf-8'):
    try:
        # Load the CSV file into a pandas data frame
        df = pd.read_csv(file_path, delimiter=delimiter, encoding=encoding)

        # Convert the data frame to a string and return it
        return df.to_string(index=False)
    except Exception as e:
        print('Error:', str(e))
        return None

def load():

    # Load new data from a CSV file
    new_data =preprocess_input.preprocess()
    # Convert the data type of the NumPy array to a supported type
    new_data = new_data.astype(np.float32)
    # Make predictions on the new data
    y_pred = model.predict(new_data)
    # Convert the NumPy array to a Pandas DataFrame
    new_data = pd.DataFrame(new_data)
    # Convert probabilities to binary predictions using a threshold
    y_pred_binary = (y_pred > 0.2).astype('int32')
    # Create a new column in the data frame with predicted labels
    new_data['predicted_label'] = y_pred_binary

    # Create two separate data frames for positive and negative predictions
    impFeatures = ['Init Bwd Win Byts', 'Fwd Pkt Len Max', 'Bwd IAT Min', 'Fwd IAT Min', 'Subflow Fwd Byts',
                   'TotLen Fwd Pkts', 'Fwd Pkt Len Min', 'Bwd Blk Rate Avg', 'Pkt Size Avg',
                   'Down/Up Ratio']
    new_data.columns = impFeatures + ['predicted_label']
    positive_df = new_data[new_data['predicted_label'] == 1]
    negative_df = new_data[new_data['predicted_label'] == 0]

    # Save the two data frames to separate CSV files
    positive_df.to_csv('positive_predictions.csv', index=False)
    negative_df.to_csv('negative_predictions.csv', index=False)

    # Convert the positive and negative CSV files to strings
    positive_csv_string = csv_to_string('positive_predictions.csv')
    negative_csv_string = csv_to_string('negative_predictions.csv')

    return positive_csv_string,negative_csv_string


def print_raw_record(preprocessed_record):
    # Load the preprocessed data from disk
    df = pd.read_csv('preprocessed_data.csv')

    # Select the important features for the classification
    impFeatures = ['Init Bwd Win Byts', 'Fwd Pkt Len Max', 'Bwd IAT Min', 'Fwd IAT Min', 'Subflow Fwd Byts',
                   'TotLen Fwd Pkts', 'Fwd Pkt Len Min', 'Bwd Blk Rate Avg', 'Pkt Size Avg', 'Down/Up Ratio']

    # Filter the DataFrame to match the preprocessed record
    matches = (df[impFeatures] == preprocessed_record).all(axis=1)

    # Get the raw record that matches the preprocessed record
    raw_record = df.loc[matches]

    # Print the raw record
    print(raw_record.to_string(index=False))
