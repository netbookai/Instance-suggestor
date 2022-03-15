#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/NetBook-ai/Instance-suggestor/main/data/benchmarks.csv"
df = pd.read_csv(URL)
df[['TimetoTrain_mins_', 'Cost To Train']] = df[['TimetoTrain_mins_', 'Cost To Train']].apply(pd.to_numeric, errors= 'coerce')

def get_similar_instances(df=df, framework='Tensorflow', network='ResNet-50 v1.5', dataset='ImageNet2012'):
	"""
	Get similar instance benchmarks based on framework, network and dataset

	:param df: Source data
	:param framework: MXNet, PyTorch, Tensorflow etc
	:param network: Architecture/Network name
	:param dataset: Name of dataset to run your network on

	:return: dataframe

	"""
	
	df3 = df[(df['Framework']==framework) & (df['Network'] == network) & (df['Dataset'] == dataset)]
	return df3.iloc[:, :-1]

def get_fastest_instance(df=df, framework='Tensorflow', network='ResNet-50 v1.5', dataset='ImageNet2012'):
	'''
	Get fastest instance based on framework, network and dataset

	:param df: Source data
	:param framework: MXNet, PyTorch, Tensorflow etc
	:param network: Architecture/Network name
	:param dataset: Name of dataset to run your network on

	:return: dataframe

	'''
	df3 = df[(df['Framework']==framework) & (df['Network'] == network) & (df['Dataset'] == dataset)]
	fi = df3['TimetoTrain_mins_'].min()
	gpu_inf = df3.loc[df3['TimetoTrain_mins_'].isin([fi])]
	return gpu_inf.iloc[:, :-1]

def get_cheapest_instance(df=df, framework='Tensorflow', network='ResNet-50 v1.5', dataset='ImageNet2012'):
	'''
	Get cheapest instance based on framework, network and dataset
	
	:param df: Source data
	:param framework: MXNet, PyTorch, Tensorflow etc
	:param network: Architecture/Network name
	:param dataset: Name of dataset to run your network on

	:return: dataframe

	'''
	df3 = df[(df['Framework']==framework) & (df['Network'] == network) & (df['Dataset'] == dataset)]
	fi = df3['Cost To Train'].min()
	gpu_inf = df3.loc[df3['Cost To Train'].isin([fi])]
	return gpu_inf.iloc[:, :-1]