# Instance-Suggestor
Python module to help you pick the cheapest and the best performant instance any where across the globe on any cloud provider

### Introduction
Data Science training is a computationally expensive job. With each computataionally expensive job, comes exponential costs. This repo is for Data Scientists to understand in real time to understand the best instance at any point in time which fits the exact need for the dataset and training job they have across any cloud provider

### V0 (suggest.py)

Python Module which takes 
 1. Source data
 2. Instance Name
 3. Cloud Provider
 4. Region

and outputs
 1. Alternate Instances across different cloud providers same region
 2. Alternate cheapest instance on the same provider same region
 3. Alternate cheapest instance on the same provider any region
 4. Cheapest Instance across any cloud provider same region
 5. Cheapest Instance across any cloud provider any region

#### Default arguments
 1. Instance Name : p3.16xlarge
 2. Provider : AWS
 3. Region : Price_US_East1

### V1 (instance-suggestor.py)

Python Module which takes
 1. Source data 
 2. Framework (MXNet, Tensorflow, PyTorch)
 3. Network
 4. Dataset 

and outputs
 1. Similar instances across different cards
 2. Fastest instance on all cards
 3. Cheapest instance on all cards

#### Default arguments
 1. Framework : Tensorflow
 2. Network : ResNet-50 v1.5
 3. Dataset : ImageNet2012
 
### How To Use

***Requires basic Python packages like numpy, pandas preinstalled***

#### Using as a Python Package
**You can also do a pip install of the latest version of InstanceSuggestor**

```
$ pip install InstanceSuggestor
$ python3 #open a python shell
> import InstanceSuggestor as inst
> inst.get_fastest_instance() #outputs result based on default arguments
> inst.get_fastest_instance(url, framework, network, dataset) #to make a custom call to function
> inst.get_similar_instances(url, framework, network, dataset)
> inst.get_cheapest_instance(url, framework, network, dataset)
> inst.predictor_sameRegion(url, instance, region)
> inst.predictor_anyRegion(url, instance, provider, region)
> inst.predictor_cheapest(url, instance, region)
> inst.predictor_cheapest2(url, region)
> inst.predictor_sameRegion2(url, instance, provider, region)
```


### Example Runs

> get_similar_instances()

![get_similar](./images/get_similar.png)

> predictor_cheapest() : input shows an AWS instance and the suggestor provides a cheaper instance on GCP.

![get_cheapest](./images/get_cheapest.png)

### Project Status
 Ongoing
