# Instance-picker
Python module to help you pick the cheapest and the best performant instance any where across the globe on any cloud provider

### Introduction
Data Science training is a computationally expensive job. With each computataionally expensive job, comes exponential costs. This repo is for Data Scientists to understand in real time to understand the best instance at any point in time which fits the exact need for the dataset and training job they have across any cloud provider

### V0 (suggest.py)

Python Module which takes 
 1. Instance Name
 2. Cloud Provider
 3. Region

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
 1. Framework (MXNet, Tensorflow, PyTorch)
 2. Network
 3. Dataset 

and outputs
 1. Similar instances across different cards
 2. Fastest instance on all cards
 3. Cheapest instance on all cards

#### Default arguments
 1. Framework : Tensorflow
 2. Network : ResNet-50 v1.5
 3. Dataset : ImageNet2012
 
### How To Use

***Requires basic Python packages like numpy, pandas, sys, argparse preinstalled***

To run this project, clone the repository and follow below steps.

```
$ cd Instance-picker
$ python3 instance-suggestor.py #run V1 with default arguments
$ python3 instance-suggestor.py -i [input-file-name] -f [framework] -n [network] -d [dataset] #to run custom V1
$ python3 suggest.py #to run V0 with default arguments
$ python3 suggest.py -i [input-file-name] -ins [instance-name] -p [provider] -r [region] #to run custom V0
```

### Example Runs

> V1

![Screenshot 2022-03-04 at 4 17 48 PM](https://user-images.githubusercontent.com/30073239/156749629-bc1119bd-75f5-4441-9887-c2aa76a81180.png)

> V0

![Screenshot 2022-03-04 at 4 27 55 PM](https://user-images.githubusercontent.com/30073239/156751131-4da9d119-51c4-4e5c-bbda-7072fe527883.png)

### Project Status
 Ongoing
