#install library pip install wfdb
import wfdb
import pandas as pd
import os


data_path = r'database/'


record = wfdb.rdrecord(os.path.join(data_path, '100'))
annotation = wfdb.rdann(os.path.join(data_path, '100'), 'atr')


signals = pd.DataFrame(record.p_signal, columns=record.sig_name)
signals['Time'] = [i / record.fs for i in range(len(signals))]


ann_df = pd.DataFrame({
    'Sample': annotation.sample,
    'Symbol': annotation.symbol,
    'SubType': annotation.subtype,
    'Channel': annotation.chan,
    'Num': annotation.num,
    'AuxNote': annotation.aux_note
})



signals.to_csv('mitbih_100_signals.csv', index=False)
ann_df.to_csv('mitbih_100_annotations.csv', index=False)


