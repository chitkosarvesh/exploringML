#FILE_NO:2
#FILE NAME:iris_dataset_all_combinations.py
#WRITTEN BY: Sarvesh Chitko (exploringML)
#VERSION:1.0 DATE:20160314
import numpy as np;
import scipy as sp;
from matplotlib import pyplot as plt;
from sklearn.datasets import load_iris;
import itertools;
#MAIN PROGRAM
data=load_iris()
features=data['data'];
feature_names=data['feature_names']
target=data['target']
fcnt=[0,1,2,3]
fcom=set(itertools.combinations(fcnt,2));
for j in fcom:
	for t,marker,c in zip(xrange(3),">ox","rgb"):
		x=j[0]
		y=j[1]
		plt.xlabel(feature_names[x])
		plt.ylabel(feature_names[y])
		plt.scatter(features[target==t,x],features[target==t,y],marker=marker,c=c)
	plt.show()
