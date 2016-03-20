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
for p in p_length:
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
i = 0 #reset count
for feature in features:
	print("Petal Length:"+str(feature[2])+" Actual Type:"+target_names[target[i]]+" Guessed Type:"+ "setosa" if feature[2]<2 else "Petal Length:"+str(feature[2])+" Actual Type:"+target_names[target[i]]+" Guessed Type:"+ "non-setosa");
	i=i+1

