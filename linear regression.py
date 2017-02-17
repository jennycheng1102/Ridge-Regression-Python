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
#test sklearn fit
lmod=sklearn.linear_model.regression()
skfit=lmod.fit(X,Y)
print skfit.coef_,skfit.intercept_
c=skfit.coef_
c=np.append(c,skfit.coef_)    
XF<-np.insert(x,k,values=1,axis=1)
             
             
#least squares solution
x1<-XF.transpose()
x2<-x1.dot(XF)
x3<-np.linalg.inv(x2)
x4<-x3.dot(x1)
betahat<-x3.dot(Y)
print betahat
Ypred=XF.dot(betahat)
residual=Y-Ypred
residmean=np.mean(resid)
residvar=np.var(resid)             
