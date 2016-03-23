#FILE_NO:2
#FILE NAME:iris_dataset_classification_algorithm.py
#WRITTEN BY: Sarvesh Chitko (exploringML)
#VERSION:1.1 DATE:20160316
import scipy as sp
from sklearn.datasets import load_iris
data=load_iris()
features=data['data'] #this contains actual measurements of the various params (petal length, sepal length etc.)
feature_names=data['feature_names'] #this contains names of the features, can be used as a key to the features array
target=data['target'] # this contains information on which feature element is what type of flower
target_names=data['target_names'] #names of the flower, can be used as key to the target array and the features array in turn.
#So, based on our intial observation in Program #2, we see that the petal length is an ideal parameter to separate atleast the iris setosa flower
#from the versicolor and virginica flowers. So, now, we will find the max of the setosa petal length and the min of the others, giving us a basis
#of classification. Doing that...
p_length = features[:,2] #sorting out petal length for all the features.
s_p_length = sp.array([]) #array to store the setosa petal length
ns_p_length = sp.array([]) #array to store all other petal length values
i=0 #counter variable
for p in p_length: #Now, this is an extremely crude way to do the sorting. I will use a better way below.
	if(target_names[target[i]]=='setosa'):
		s_p_length = sp.append(s_p_length,p)
	else:
		ns_p_length = sp.append(ns_p_length,p)
	i=i+1

print("Max of the setosa:"+str(s_p_length.max())) #Max of setosa:1.9
print("Min of non-setosa:"+str(ns_p_length.min())) #Min of non-setosa:3.0
#Now, we have min and max values according to the data. An assumption that we can safely make at this point is that, any petal length < 2
#is an iris setosa. So then, now we a re going to run a small test, where we will check the petal length in the features array
#and make it guess what type of flower that is.
i = 0 #reset counter
for feature in features:
	print(str(i+1)+". Petal Length:"+str(feature[2])+" Actual Type:"+target_names[target[i]]+" Guessed Type:"+ "setosa" if feature[2]<2 else str(i+1)+". Petal Length:"+str(feature[2])+" Actual Type:"+target_names[target[i]]+" Guessed Type:"+ "non-setosa") #fear my python-fu, mortal!
	i=i+1
#That shows that our classification algorithm worked for the setosa flowers. I know that algorithm is nothing great, if petal length is less that 2, its a setosa.
#Concept: In this example, we chose that the petal length is the best fit, but that gave us only part of the solution. So, machine learning will happen
#when our algorithm will choose the best way to classify data, ALL BY ITSELF.
#Lets see if we can achieve that...
#The better way to sort the data as promised above:
is_setosa=(target_names[target]=='setosa') #Now,this will classify the flowers based on their names, ex. just do  a features[is_setosa] to select all setosa flowers.
is_versicolor=(target_names[target]=='versicolor')
is_virginica=(target_names[target]=='virginica')
#Now, we will filter out the setosa flowers from our dataset as we exactly know how to identify them, so, taking into consideration only the non-setosa flowers...
ns_features=features[~is_setosa] #Yup, that simple!!!
#Now, lets run a small snippet which will find the best fit for the versicolor and the viginica flowers.
best_acc=-1.0 #Setting the best fit to -1.
for fi in xrange(ns_features.shape[1]):
	#lets generate all possible thresholds for this feature.
	thresh=ns_features[:,fi].copy()
	thresh.sort()
	for t in thresh:
		pred=(features[:,fi]>t)
		acc=(pred==is_virginica).mean() #This accuracy is nothing but the fraction of the examples the algorithm classifies correctly.
		if acc>best_acc:
			best_acc=acc
			best_fi=fi
			best_t=t
print("#Best Accuracy:"+str(best_acc)+"\n#Best Feature:"+str(feature_names[best_fi])+"\n#Best Threshold:"+str(best_t)) #There, you have it! Best accuracy, best feature and best threshold, all by itself!
#What this basically means is that, our mini ML Algorithm here just found out that feature No.3 is the best feature to use.
#Now, to test the accuracy of the algorithm outside the test data, we need a sample.
example = sp.array([5.3,2.9,5.4,1.4]) #Le wild flower appears!
#Now, our first classification algorithm:
print("Example Data is:")
i=0
for e in example:
	print("***"+feature_names[i]+":"+str(e))
	i=i+1
if example[best_fi]>best_t:
	print "This is an Iris Virginica Flower"
else:
	print "This is an Iris Versicolor Flower"
#TADA!!!



