#install library pip install wfdb
import wfdb
import pandas as pd

noise_class = {
    'em': 3,
    'ma': 2,
    'bw': 1
}

all_data = []

for noise_type, label in noise_class.items():
    record = wfdb.rdrecord(noise_type)

    df = pd.DataFrame(record.p_signal, columns=record.sig_name)
    df['Time (s)'] = [i / record.fs for i in range(len(df))]
    
    df['type'] = noise_type
    
    
    all_data.append(df)


combined_df = pd.concat(all_data, ignore_index=True)


combined_df.to_csv('nstdb.csv', index=False)

