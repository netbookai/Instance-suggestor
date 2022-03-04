#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import sys
import argparse


def predictor_sameRegion(df, gput, gpum):
	print("\n \n ----------- Alternate Instances across different cloud providers same region -------- \n")
	df2 = df[(df['GPU Type'] == gput) & (df['GPU memory'] == gpum)]
	print("\n" + df2[cols].to_string(index=False) + "\n")


def predictor_sameRegion2(df, gput, gpum, prov, reg):
	print("\n \n ----------- Alternate cheapest instance on the same provider same region -------- \n")
	df2 = df[(df['GPU Type'] == gput) & (df['GPU memory'] == gpum)]
	mp = df2[df2['Provider'] == prov]
	print("\n" + mp[mp[reg] == mp[reg].min()][cols].to_string(index=False) + "\n")


def predictor_anyRegion(df, gput, gpum, prov, reg):
	print("\n \n ----------- Alternate cheapest instance on the same provider any region -------- \n")
	df2 = df[(df['GPU Type'] == gput) & (df['GPU memory'] == gpum)]
	mp = df2[df2['Provider'] == prov]
	mpr = mp[cols1].min().min()
	print(mp[(mp[cols1[0]] == mpr) | (mp[cols1[1]] == mpr) | (mp[cols1[2]] == mpr) | (mp[cols1[3]] == mpr)].to_string(index = False))

def predictor_cheapest(df, gput, gpum, reg):
	print("\n \n ----------- Cheapest Instance across any cloud provider same region -------- \n")
	df2 = df[(df['GPU Type'] == gput) & (df['GPU memory'] == gpum)]
	print(df2[df2[reg] == df2[reg].min()][cols].to_string(index = False))


def predictor_cheapest2(df, gput, gpum):
	print("\n \n ----------- Cheapest Instance across any cloud provider any region -------- \n")
	df2 = df[(df['GPU Type'] == gput) & (df['GPU memory'] == gpum)]
	mpr = df2[cols1].min().min()
	print(df2[(df2[cols1[0]] == mpr) | (df2[cols1[1]] == mpr) | (df2[cols1[2]] == mpr) | (df2[cols1[3]] == mpr)].to_string(index = False) + "\n")


def input_data(df, instance):
	gpu_type = str(df['GPU Type'].values[df['Instance Name']==instance][0])
	gpu_memory = df['GPU memory'].values[df['Instance Name']==instance][0]
	return (gpu_type, gpu_memory)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'A Basic Instance Suggestor')
    parser.add_argument('--input_file', "-i", help = "Input file for project", default="pricing.csv")
    parser.add_argument('--instance', "-ins", help = "Instance Name", default = 'p3.16xlarge')
    parser.add_argument('--provider', "-p", help = "Provider name", default="AWS")
    parser.add_argument('--region', '-r', help = 'Region', default = "Price_US_East1")
    args = parser.parse_args()

    df = pd.read_csv(args.input_file)
    gpu_type, gpu_memory = input_data(df, args.instance)

    global cols, cols1

    cols = df.columns[:8].values
    np.append(cols, args.region)
    cols1 = df.columns[7:]

    predictor_sameRegion(df, gpu_type, gpu_memory)

    predictor_sameRegion2(df, gpu_type, gpu_memory, args.provider, args.region)

    predictor_anyRegion(df, gpu_type, gpu_memory, args.provider, args.region)

    predictor_cheapest(df, gpu_type, gpu_memory, args.region)

    predictor_cheapest2(df, gpu_type, gpu_memory)






