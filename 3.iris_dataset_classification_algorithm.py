import scipy as sp
from sklearn.datasets import load_iris
data=load_iris()
features=data['features'] #this contains actual measurements of the various params (petal length, sepal length etc.)
feature_names=data['feature_names'] #this contains names of the features, can be used as a key to the features array
target=data['target'] # this contains information on which feature element is what type of flower
target_names=data['target_names'] #names of the flower, can be used as key to the target array and the features array in turn.
#So, based on our intial observation in Program #2, we see that the petal length is an ideal parameter to separate atleast the iris setosa flower
#from the versicolor and virginica flowers. So, now, we will find the max of the setosa petal length and the min of the others, giving us a basis
#of classification. Doing that...
plength = features[:,2] #sorting out petal length for all the features.

