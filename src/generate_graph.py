from graph import line

inputOrders = ['nsorted', 'rand', 'rev', 'sorted']
nameGraphs = ['Near sorted input', 'Randomized input', 'Reversed input', 'Sorted input']

for inputOrder, nameGraph in zip(inputOrders, nameGraphs):
    csv_file = 'data/result_' + inputOrder + '.csv'
    line.plot(csv_file, nameGraph, inputOrder)