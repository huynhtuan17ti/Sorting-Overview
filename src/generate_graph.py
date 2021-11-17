from graph import plot

inputOrders = ['nsorted', 'rand', 'rev', 'sorted']
nameGraphs = ['Near sorted input', 'Randomized input', 'Reversed input', 'Sorted input']

for inputOrder, nameGraph in zip(inputOrders, nameGraphs):
    csv_file = 'data/result_' + inputOrder + '.csv'
    plot.line(csv_file, nameGraph, inputOrder)
    plot.bar(csv_file, nameGraph, inputOrder)