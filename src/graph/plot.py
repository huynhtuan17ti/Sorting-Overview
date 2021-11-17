import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
import seaborn as sns
sns.set_theme(style="whitegrid")
from .data import line_process, bar_process

def line(csv_file: str, graph_name: str, output_name: str):
    rcParams['figure.figsize'] = 16, 10
    df = line_process(csv_file)
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

    plt.savefig(f'plot/{output_name}_line.png')

def bar(csv_file: str, graph_name: str, output_name: str):
    rcParams['figure.figsize'] = 20, 10
    fig, ax = plt.subplots()
    df = bar_process(csv_file)
    sns.barplot(data = df, x = 'sort', y = 'iter', hue='size', palette="magma", errcolor='0.5', ax = ax)
    ax.set_yscale("log")
    ax.set_title(graph_name)
    ax.set_ylabel('Number of comparisions')
    ax.set_xlabel('Sort algorithm')
    ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)

    plt.savefig(f'plot/{output_name}_bar.png')