# convert information in csv to latex tablular format
import pandas as pd
import os

def convert(name):
    df = pd.read_csv('data/' + name)
    header = df.columns[1:-1]

    f = open('data/' + name[:-3] + "txt", "w")
    for i in range(len(df)):
        convert_line = df['Sort'][i] + " "
        for j in range(len(header)):
            col = header[j]
            if j%2 == 0:
                val = float(df[col][i])
            else:
                val = df[col][i]
            convert_line += str(val)
            if j < len(header) - 1:
                convert_line += " & "
            else:
                convert_line += " \\" + "\\"
        f.write(convert_line + '\n')
    f.close()

if __name__ == '__main__':
    for name in os.listdir('data'):
        if 'csv' in name:
            convert(name)

   