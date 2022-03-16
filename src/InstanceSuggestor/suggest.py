#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/NetBook-ai/Instance-suggestor/main/data/pricing.csv"

def input_data(url = URL, instance='p3.16xlarge'):
	"""
	utility function
	
	:param url: source file
	:param instance: Instance name

	:return: tuple | (Source Data, GPU Type, GPU Memory)

	"""
	df = pd.read_csv(URL)
	gpu_type = str(df['GPU Type'].values[df['Instance Name']==instance][0])
	gpu_memory = df['GPU memory'].values[df['Instance Name']==instance][0]
	return (df, gpu_type, gpu_memory)

def predictor_sameRegion(url=URL, instance='p3.16xlarge', region='Price_US_East1'):
	"""
	Get Alternate Instances across different cloud providers same region of same GPU Type and same GPU Memory

	:param url: Source file
	:param instance: Instance name of any cloud
	:param region: Region name in format - 'Price_Region_Area'

	:return: dataframe
	
	"""
	df, gpu_type, gpu_memory = input_data(url, instance)
	df2 = df[(df['GPU Type'] == gpu_type) & (df['GPU memory'] == gpu_memory)]
	cols = df.columns[:8].values
	np.append(cols, region)
	return df2[cols]


def predictor_sameRegion2(url=URL, instance='p3.16xlarge', provider='AWS', region='Price_US_East1'):
	"""
	Get Alternate Cheapest Instance on the same provider, same region of same GPU Type and same GPU Memory

	:param url: Source file
	:param instance: Instance name of a cloud provider
	:param provider: Provider name - AWS, GCP, Azure
	:param region: Region name in format - 'Price_Region_Area'

	:return: dataframe
	
	"""
	df, gpu_type, gpu_memory = input_data(url, instance)
	df2 = df[(df['GPU Type'] == gpu_type) & (df['GPU memory'] == gpu_memory)]
	mp = df2[df2['Provider'] == provider]
	cols = df.columns[:8].values
	np.append(cols, region)
	return mp[mp[region] == mp[region].min()][cols]


def predictor_anyRegion(url=URL, instance='p3.16xlarge', provider='AWS', region='Price_US_East1'):
	"""
	Get Alternate Cheapest Instance on the same provider, any region of same GPU Type and same GPU Memory

	:param url: Source file
	:param instance: Instance name of a cloud provider
	:param provider: Provider name - AWS, GCP, Azure
	:param region: Region name in format - 'Price_Region_Area'

	:return: dataframe
	
	"""
	df, gpu_type, gpu_memory = input_data(url, instance)
	df2 = df[(df['GPU Type'] == gpu_type) & (df['GPU memory'] == gpu_memory)]
	cols1 = df.columns[7:]
	mp = df2[df2['Provider'] == provider]
	mpr = mp[cols1].min().min()
	return mp[(mp[cols1[0]] == mpr) | (mp[cols1[1]] == mpr) | (mp[cols1[2]] == mpr) | (mp[cols1[3]] == mpr)]

def predictor_cheapest(url=URL, instance='p3.16xlarge', region='Price_US_East1'):
	"""
	Get Cheapest Instance on any provider, same region of same GPU Type and same GPU Memory

	:param url: Source file
	:param instance: Instance name of a cloud provider
	:param region: Region name in format - 'Price_Region_Area'

	:return: dataframe
	
	"""
	df, gpu_type, gpu_memory = input_data(url, instance)
	df2 = df[(df['GPU Type'] == gpu_type) & (df['GPU memory'] == gpu_memory)]
	cols = df.columns[:8].values
	np.append(cols, region)
	return df2[df2[region] == df2[region].min()][cols]


def predictor_cheapest2(url=URL, instance='p3.16xlarge'):
	"""
	Get Cheapest Instance on any provider, any region of same GPU Type and same GPU Memory

	:param df: Source file
	:param instance: Instance name of a cloud provider

	:return: dataframe
	
	"""
	df, gpu_type, gpu_memory = input_data(url, instance)
	df2 = df[(df['GPU Type'] == gpu_type) & (df['GPU memory'] == gpu_memory)]
	cols1 = df.columns[7:]
	mpr = df2[cols1].min().min()
	return df2[(df2[cols1[0]] == mpr) | (df2[cols1[1]] == mpr) | (df2[cols1[2]] == mpr) | (df2[cols1[3]] == mpr)]
	