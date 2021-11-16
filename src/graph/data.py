import pandas as pd

def process(csv_file: str):
    df = pd.read_csv(csv_file)
    header = df.columns.to_numpy()
    data_size = [10000, 30000, 50000, 100000, 300000, 500000]
    sort_algo = df[header[0]].tolist()
    data = {}
    data['size'] = data_size
    for i in range(len(df)):
        time_list, comp_list = [], []
        for col in header:
            if 'time' in col:
                time_list.append(df[col][i]/1000) # convert to second
            elif 'comp' in col:
                comp_list.append(df[col][i])
        data[sort_algo[i] + '-time'] = time_list
        data[sort_algo[i] + '-comp'] = comp_list
    new_df = pd.DataFrame(data)
    return new_df