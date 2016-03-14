#FILE_NO:2
#FILE NAME:iris_dataset_all_combinations.py
#WRITTEN BY: Sarvesh Chitko (exploringML)
#VERSION:1.1 DATE:20160314
import numpy as np;
import scipy as sp;
from matplotlib import pyplot as plt;
from sklearn.datasets import load_iris;
import itertools;
#MAIN PROGRAM
data=load_iris() #getting the data from the sklean toolkit
features=data['data'];
feature_names=data['feature_names']
target=data['target']
fcom=set(itertools.combinations(feature_names,2)) #getting all possible combinations for nC2 (where n is the number of features)
for j in fcom:
	print("Current Combination: "+j[0]+" vs."+j[1])
	for t,marker,c in zip(xrange(3),">ox","rgb"):
		x=feature_names.index(j[0])
		y=feature_names.index(j[1])
		plt.xlabel(feature_names[x])
		plt.ylabel(feature_names[y])
		plt.scatter(features[target==t,x],features[target==t,y],marker=marker,c=c)
	plt.show()

#Based on the above graphs, we can make certain conclusions. Petal length can distinguish between Iris Setosa (>) from the remaining
#Iris Versicolor and Iris Virginica. So, lets find the differntiating point between iris setosa and the others.

