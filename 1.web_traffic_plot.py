#FILE_NO:1
#FILE NAME:web_traffic_plot.py
#WRITTEN BY: Sarvesh Chitko (exploringML)
#VERSION:1.0 DATE:20160314
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

#functions
def error(f,x,y):
	return sp.sum((f(x)-y)**2)
#end functions

data=sp.genfromtxt("resources/web_traffic.tsv",delimiter="\t")
x=data[:,0] #separating x axis data (hours)
y=data[:,1] #separating y axis data (hits/hr)
# we also need to check if our y-axis data has any NaN (null) characters, we dont want them messing up our graph. Here we go!
#we are going to execute the logic to cleanse the NaN without any code to check if nulls exist.
y=y[~sp.isnan(y)] # the 'tilda' (~) in this case acts like the 'negate' (!) operator in other high-level languages like Java/PHP etc. But, Python is old school cool!
x=x[~sp.isnan(y)] # sample processing for x, because, duh! we dont want row counts to differ for x and y!
#Now that we have the cleansed data, creating a scatter-plot for the x and y axis data...
print("Displaying original data...");
plt.title("Web Traffic data")
plt.xlabel("Weeks")
plt.xticks([w*7*24 for w in range(10)],["Week %i" % w for w in range(10)]) #Showing this data in hourly fashion can be lengthy and difficult to understand, so converting it to weeks made sense.
plt.ylabel("Hits/Hr")
plt.scatter(x,y)
plt.show()
#Now, towards getting a degree 1 polynomial fitted through this data.
print("Fitting a 1st Degree Polynomial over the existing data...")
fp1,residuals,rank,sv,rcond=sp.polyfit(x,y,1,full=True) #full=False will return only the params of the fitted model, whereas, full=True will return additional info about the fitting process.
print("Best straight line fit for the data is: f(x)="+str(fp1[0])+" * x"+" + "+str(fp1[1]))
f1=sp.poly1d(fp1)
err = error(f1,x,y)
print("Current Error:"+str(err))
fx = sp.linspace(0,x[-1],1000) #generating equidistant x-values for plotting, x[-1] will give the last value of x
plt.title("Web Traffic data with fitted 1st order polynomial.")
plt.xlabel("Weeks")
plt.xticks([w*7*24 for w in range(10)],["Week %i" % w for w in range(10)]) #Showing this data in hourly fashion can be lengthy and difficult to understand, so converting it to weeks made sense.
plt.ylabel("Hits/Hr")
plt.scatter(x,y)
plt.plot(fx,f1(fx),linewidth=2,color='r')
plt.show()
#The fitted polynomial looks good, but is that the best fit for the data? Lets find out! Now, We fit 2nd, 10th and 100th order polynomials in the data.
fp2=sp.polyfit(x,y,2) #Not using full=True this time, I dont need the additional fitting process data now. Sigh! Maybe some day.
f2=sp.poly1d(fp2)
print("Error for 2nd order polynomial:"+str(error(f2,x,y)))
fp10=sp.polyfit(x,y,10) # yup, changing that one integer value does the trick! All hail Python and scipy.
f10=sp.poly1d(fp10)
print("Error for 10th order polynomial:"+str(error(f10,x,y)))
fp100=sp.polyfit(x,y,100)
f100=sp.poly1d(fp100)
print("Error for 100th order polynomial:"+str(error(f100,x,y)))
plt.title("Web Traffic data with fitted 1st/2nd/10th & 100th order polynomials.")
plt.xlabel("Weeks")
plt.xticks([w*7*24 for w in range(10)],["Week %i" % w for w in range(10)]) #Showing this data in hourly fashion can be lengthy and difficult to understand, so converting it to weeks made sense.
plt.ylabel("Hits/Hr")
plt.scatter(x,y)
plt.plot(fx,f1(fx),linewidth=2,label="Order=1")
plt.plot(fx,f2(fx),linewidth=2,label="Order=2")
plt.plot(fx,f10(fx),linewidth=2,label="Order=10")
plt.plot(fx,f100(fx),linewidth=2,label="Order=100")
plt.legend()
plt.show()
#Notice that the error values keep decreasing, but from a fururistic point of view, least errors will not be the best way to go. We need predictability,
#So,some degree of error is required. So, the best fit in this condition will be the 2nd order. But, is that enough? Lets implement another idea,
# we break the data in 2 parts, looking at the data we see a significant rise in the Hits/Hr count somewhere around week 3~4 (Assume, week 3.5).
# We fit pre-week 3.5 and post-week 3.5 data separately.
inflection=3.5*7*24 #find the hour at 3.5 week, this is our separation point.
#separating pre and post inflection data
xa=x[:inflection]
ya=y[:inflection]
xb=x[inflection:]
yb=y[inflection:]
#fitting 1st order polys on the newly separated data.
fa=sp.poly1d(sp.polyfit(xa,ya,1))
fb=sp.poly1d(sp.polyfit(xb,yb,1))
#Take a look at the error values, even a 1st order poly has lower error than a 100th order one. Statistics B**ch!
print("Error for fa:"+str(error(fa,xa,ya)))
print("Error for fb:"+str(error(fb,xb,yb)))
#Plotting these new polys.
plt.title("Web Traffic data with 2 separate polynomials")
plt.xlabel("Weeks")
plt.xticks([w*7*24 for w in range(10)],["Week %i" % w for w in range(10)]) #Showing this data in hourly fashion can be lengthy and difficult to understand, so converting it to weeks made sense.
plt.ylabel("Hits/Hr")
plt.scatter(x,y)
fax = sp.linspace(0,xa[-1],100)
fbx = sp.linspace(0,xb[-1],100)
plt.plot(fax,fa(fax),linewidth=2,label="Pre-Inflection Point",color="r")
plt.plot(fbx,fb(fbx),linewidth=2,label="Post-Inflection Point",color="g");
plt.legend()
plt.show()
#See that, two polyfits and better predictability. I think switching between order 1 & 2 on lines 76 & 77 will fine tune the results in the future.