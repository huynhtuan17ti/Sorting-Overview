import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
import seaborn as sns
rcParams['figure.figsize'] = 16, 10
from .data import process

def plot(csv_file: str, graph_name: str, output_name: str):
    df = process(csv_file)
    sort_algo = ['bubble-sort',
                'counting-sort',
                'flash-sort',
                'heap-sort',
                'insertion-sort',
                'merge-sort',
                'quick-sort',
                'radix-sort',
                'selection-sort',
                'shaker-sort',
                'shell-sort']
    fig, ax = plt.subplots()
    colors = ['red', 'blue', 'yellow', 'orange', 'green', 'violet', 'purple', 'limegreen', 'navy', 'palegreen', 'coral']
    for idx, sort_name in enumerate(sort_algo):
        y_label = sort_name + '-time'
        sns.pointplot(data = df, y = y_label, x = 'size', markers = '^', ax = ax, color = colors[idx])
    ax.legend(handles = ax.lines[::len(df)+1], labels = sort_algo, loc = 2, bbox_to_anchor = (1,1))
    ax.set_xticklabels([t.get_text().split("T")[0] for t in ax.get_xticklabels()])
    ax.set_title(graph_name)
    ax.set_ylabel('Run time in seconds')
    ax.set_xlabel('Input size')

    plt.savefig(f'plot/{output_name}.png')