# Sorting-Overview
An overview of several sorting algorithms

## About
This is my project on Data structure and Algorithm class. If you are going to refer this repo, please go ahead, you're welcome. And don't forget to read my [document/paper](docs/report.pdf) and give me a review XD.

## Prerequisite
```
    python
    seaborn
    matplotlib
    pandas
    g++
    gcc
```
## How to run
To run all sorting algorithms and get the experimental results:  
```bash
$user cd src/
$user make
$user ./main -exp
```
It's will be taking much time to run the experiment.  
If you are looking for a simple comparison or experiment only one algorithm, you may want to read this [doc](docs/Lab%203.pdf) (in section `2. Submission`).

To covert running result into bar chart and line plot:  
```bash
# you can skip this if you are already in src/
$user cd src/
$user python generate_graph.py
```