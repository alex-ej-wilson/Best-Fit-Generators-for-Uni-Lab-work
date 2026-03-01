import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy.misc as sim
xmin=0
xmax=15
ymin=0
ymax=15
x   = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
y   = np.array([2.7, 3.9, 5.5, 5.8, 6.5, 6.3, 7.7, 8.5, 8.7])
sig = np.array([0.3, 0.5, 0.7, 0.6, 0.4, 0.3, 0.7, 0.8, 0.5])
x_= np.linspace(xmin,xmax,num=100)
'''
=-=-=-=
Maths
=-=-=-=
'''
M=3
def func(x,*theta):
    '''
    Inputs: x, *theta
    * denotes vector
    Output: linear function using parameters theta0 and theta1
    '''
    if M==3:
        theta0, theta1,theta2,theta3= theta
        return theta0 +theta1*x +theta2*x**2 + +theta3*x**3
    elif M==2:
        theta0, theta1,theta2= theta
        return theta0 +theta1*x +theta2*x**2
    elif M==1:
        theta0, theta1= theta
        return theta0 +theta1*x
p0 = np.ones(M+1)#initial guess for paramaters theta0 and theta1
thetahat,cov = curve_fit(func, x, y,p0 , sig, absolute_sigma=True)
#print(thetahat)

def StDev(x,cov):
    k=[]
    z=[]
    for i in range(M+1):
        for j in range(M+1):
            k.append(x**(i+j)*cov[i,j])
    return (np.sqrt(sum(k)))
'''
=-=-=-=
Plots
=-=-=-=
'''
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1,1,1)

ax.plot(x,y,'o',color='black',label='data')
ax.errorbar(x,y,yerr=sig,fmt='o',color='black')
ax.plot(x_,func(x_,*thetahat),color='tab:red',label='fit')

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')



ax.fill_between(x_,func(x_,*thetahat)+StDev(x_,cov), func(x_,*thetahat)-StDev(x_,cov), color='lightblue', zorder=-1000)

ax.legend(frameon='true',edgecolor='black',loc='lower right')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.set_title(r'$Fitted$ $Plot$')
plt.tight_layout()

fig.savefig("Fitted Plot "+str(M)+".pdf", format='pdf')