import pandas as pd


def preprocess():
    # collective dataset that stores the data in a single file format.
    df = pd.read_csv("C:/Users/aatis/PycharmProjects/pythonProject1/Dataset/preprocessed_input/preprocessed_data.csv")
    # preprocessing input record
    impFeatures = ['Init Bwd Win Byts', 'Fwd Pkt Len Max', 'Bwd IAT Min', 'Fwd IAT Min', 'Subflow Fwd Byts',
                   'TotLen Fwd Pkts', 'Fwd Pkt Len Min', 'Bwd Blk Rate Avg', 'Pkt Size Avg',
                   'Down/Up Ratio']
    X = df[impFeatures]
    X=X.dropna()
    from sklearn.preprocessing import MinMaxScaler

    # Normalize the input features
    scaler = MinMaxScaler()
    X = X.values
    X = scaler.fit_transform(X)

    return X
# the translation can be faulty but is manageable

#Flow ID,Src IP,Src Port,Dst IP,Dst Port,Protocol,Timestamp,Flow Duration,Tot Fwd Pkts,Tot Bwd Pkts,
# TotLen Fwd Pkts,TotLen Bwd Pkts,Fwd Pkt Len Max,Fwd Pkt Len Min,Fwd Pkt Len Mean,Fwd Pkt Len Std,
# Bwd Pkt Len Max,Bwd Pkt Len Min,Bwd Pkt Len Mean,Bwd Pkt Len Std,Flow Byts/s,Flow Pkts/s,Flow IAT Mean,
# Flow IAT Std,Flow IAT Max,Flow IAT Min,Fwd IAT Tot,Fwd IAT Mean,Fwd IAT Std,Fwd IAT Max,Fwd IAT Min,
# Bwd IAT Tot,Bwd IAT Mean,Bwd IAT Std,Bwd IAT Max,Bwd IAT Min,Fwd PSH Flags,Bwd PSH Flags,Fwd URG Flags,
# Bwd URG Flags,Fwd Header Len,Bwd Header Len,Fwd Pkts/s,Bwd Pkts/s,Pkt Len Min,Pkt Len Max,Pkt Len Mean,Pkt Len Std,
# Pkt Len Var,FIN Flag Cnt,SYN Flag Cnt,RST Flag Cnt,PSH Flag Cnt,ACK Flag Cnt,URG Flag Cnt,CWE Flag Count,ECE Flag Cnt,
# Down/Up Ratio,Pkt Size Avg,Fwd Seg Size Avg,Bwd Seg Size Avg,Fwd Byts/b Avg,Fwd Pkts/b Avg,
# Fwd Blk Rate Avg,Bwd Byts/b Avg,Bwd Pkts/b Avg,Bwd Blk Rate Avg,Subflow Fwd Pkts,Subflow Fwd Byts,Subflow Bwd Pkts,
# Subflow Bwd Byts,Init Fwd Win Byts,Init Bwd Win Byts,Fwd Act Data Pkts,Fwd Seg Size Min,Active Mean,Active Std
# ,Active Max,Active Min,Idle Mean,Idle Std,Idle Max,Idle Min,Label
