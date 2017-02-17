#scikit-learn numpy pandas
#look at what linear regression can bring us first

import numpy as np
import mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import sklearn 

plt.close('all') #close all plot windows
NP=2 #number of predictors
k=200 #number of observations

X=np.zeros((k,NP))
Y=np.zeros((k))
w=np.zeros((3))

xmin=0.0
xmax=1.0
x[:,0]=np.random.rand(k) #creating the first column predictor's data 
x[:,1]=np.random.rand(k)
XF=np.insert(x,NP,values=1,axis=1
w[0]=0.85,w[1]=0.7,w[2]=0.5
Y=XF*dot(w)

#add noise
var=0.01
mu,sigma=0.0,np.sqrt(var)
g=mu+sigma*np.random.rand(k)
Y=Y+g
