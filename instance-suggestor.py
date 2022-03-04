#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import sys
import argparse

def get_similar_instances(df, framework, network, dataset):
	print("\n \n ----------- Instance Benchmarks -------- \n")
	df3 = df[(df['Framework']==framework) & (df['Network'] == network) & (df['Dataset'] == dataset)]
	print("\n" + df3.iloc[:, :-1].to_string(index = False) + "\n")
	return df3

def get_fastest_instance(df):
	print("\n \n ----------- Fastest Instance -------- \n")
	fi = df['TimetoTrain_mins_'].min()
	gpu_inf = df.loc[df['TimetoTrain_mins_'].isin([fi])]
	print("\n" + gpu_inf.iloc[:, :-1].to_string(index = False) + "\n")

def get_cheapest_instance(df):
	print("\n \n ----------- Cheapest Instance -------- \n")
	fi = df['Cost To Train'].min()
	gpu_inf = df.loc[df['Cost To Train'].isin([fi])]
	print("\n" + gpu_inf.iloc[:, :-1].to_string(index = False) + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'An Instance Suggestor')
    parser.add_argument('--input_file', "-i", help = "Input file for project", default="data/benchmarks.csv")
    parser.add_argument('--framework', "-f", help = "Framework (eg. MXNet, PyTorch, Tensorflow)", default = 'Tensorflow')
    parser.add_argument('--network', "-n", help = "Network", default="ResNet-50 v1.5")
    parser.add_argument('--dataset', '-d', help = 'Dataset you are working on', default = "ImageNet2012")
    args = parser.parse_args()

    df = pd.read_csv(args.input_file)
    df[['TimetoTrain_mins_', 'Cost To Train']] = df[['TimetoTrain_mins_', 'Cost To Train']].apply(pd.to_numeric, errors= 'coerce')

    df3 = get_similar_instances(df, args.framework, args.network, args.dataset)

    get_fastest_instance(df3)

    get_cheapest_instance(df3)


