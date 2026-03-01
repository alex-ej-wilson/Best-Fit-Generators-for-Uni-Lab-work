'''
=-=-=-=-=-=-=-=
  Exercise 2
=-=-=-=-=-=-=-=
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2
xmin=0
xmax=1500
ymin=0
ymax=2000
h   = np.array([1000, 828,  800,  600,  300])
d   = np.array([1500, 1340, 1328, 1172, 800])
sig = np.array([15,   15,   15,   15,   15])
x_= np.linspace(xmin,xmax,num=100)
'''
=-=-=-=-=-=
Equation 1
=-=-=-=-=-=
'''
def func1(h,*theta):
    '''
    Inputs: x, *theta
    * denotes vector
    Output: linear function with only one parameter, alpha
    '''
    alpha, = theta
    return alpha*h
p01 = np.ones(1)#initial guess for paramaters theta0 and theta1
thetahat1,cov1 = curve_fit(func1, h, d,p01 , sig, absolute_sigma=True)
'''
=-=-=-=-=-=
Equation 2
=-=-=-=-=-=
'''
def func2(h,*theta):
    '''
    Inputs: x, *theta
    * denotes vector
    Output: Quadratic function with two parameters, alpha and beta
    '''
    alpha, beta = theta
    return alpha*h + beta*h**2
p02 = np.ones(2)#initial guess for paramaters theta0 and theta1
thetahat2,cov2 = curve_fit(func2, h, d,p02 , sig, absolute_sigma=True)
'''
=-=-=-=-=-=
Equation 3
=-=-=-=-=-=
'''
def func3(h,*theta):
    '''
    Inputs: x, *theta
    * denotes vector
    Output: nonlinear function with two parameters, alpha and beta
    '''
    alpha, beta = theta
    return alpha*h**beta
p02 = np.ones(2)#initial guess for paramaters theta0 and theta1
thetahat3,cov3 = curve_fit(func3, h, d,p02 , sig, absolute_sigma=True)
def StDev(x,cov,M):
    k=[]
    for i in range(M):
        for j in range(M):
            k.append(x**(i+j)*cov[i,j])
    return (np.sqrt(sum(k)))
'''
=-=-=-=
Plot 1
=-=-=-=
'''
fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(1,1,1)

ax1.plot(h,d,'o',color='black',label='data')
ax1.errorbar(h,d,yerr=sig,fmt='o',color='black')
ax1.plot(x_,func1(x_,*thetahat1),color='tab:red',label='fit')

ax1.set_xlabel(r'$h$ $[punti]$')
ax1.set_ylabel(r'$d$ $[punti]$')

ax1.fill_between(x_,func1(x_,*thetahat1)+StDev(x_,cov1,1), func1(x_,*thetahat1)-StDev(x_,cov1,1), color='lightblue', zorder=-1000)

ax1.legend(frameon='true',edgecolor='black',loc='lower right')
ax1.set_xlim(xmin,xmax)
ax1.set_ylim(ymin,ymax)
#3ax1.set_title(r'$Fitted$ $Plot$')
plt.tight_layout()

fig1.savefig("Equation 1 Plot.pdf", format='pdf')



'''
=-=-=-=
Plot 2
=-=-=-=
'''
fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(1,1,1)

ax2.plot(h,d,'o',color='black',label='data')
ax2.errorbar(h,d,yerr=sig,fmt='o',color='black')
ax2.plot(x_,func2(x_,*thetahat2),color='tab:red',label='fit')

ax2.set_xlabel(r'$h$ $[punti]$')
ax2.set_ylabel(r'$d$ $[punti]$')



ax2.fill_between(x_,func2(x_,*thetahat2)+StDev(x_,cov2,2), func2(x_,*thetahat2)-StDev(x_,cov2,2), color='lightblue', zorder=-1000)

ax2.legend(frameon='true',edgecolor='black',loc='lower right')
ax2.set_xlim(xmin,xmax)
ax2.set_ylim(ymin,ymax)
#ax2.set_title(r'$Fitted$ $Plot$')
plt.tight_layout()

fig2.savefig("Equation 2 Plot.pdf", format='pdf')


'''
=-=-=-=
Plot 3
=-=-=-=
'''
fig3 = plt.figure(figsize=(10, 8))
ax3 = fig3.add_subplot(1,1,1)

ax3.plot(h,d,'o',color='black',label='data')
ax3.errorbar(h,d,yerr=sig,fmt='o',color='black')
ax3.plot(x_,func3(x_,*thetahat3),color='tab:red',label='fit')

ax3.set_xlabel(r'$h$ $[punti]$')
ax3.set_ylabel(r'$d$ $[punti]$')



ax3.fill_between(x_,func3(x_,*thetahat3)+StDev(x_,cov3,2), func3(x_,*thetahat3)-StDev(x_,cov3,2), color='lightblue', zorder=-1000)

ax3.legend(frameon='true',edgecolor='black',loc='lower right')
ax3.set_xlim(xmin,xmax)
ax3.set_ylim(ymin,ymax)
#ax3.set_title(r'$Fitted$ $Plot$')
plt.tight_layout()

fig3.savefig("Equation 3 Plot.pdf", format='pdf')

'''
=-=-=-=-=
Values
=-=-=-=-=
'''
t_hats=[thetahat1,thetahat2,thetahat3]
covs=[cov1,cov2,cov3]
stdevs=[]
stdevs2=[]
print(covs)
for i in range(len(t_hats)):
    if i==0:
        stdevs.append(np.sqrt(covs[i][0][0]))
        print('Parameter for equation {0}:\n  alpha = {1}+-{2}\n'.format(i+1,t_hats[i][0],stdevs[i]))
    elif i>=1:
        stdevs.append(np.sqrt(covs[i][0][0]))
        stdevs2.append(np.sqrt(covs[i][1][1]))
        print('Parameters for equation {0}:\n  alpha = {1}+-{2}\n  beta = {3}+-{4}\n  Covariance = {5}\n'.format(i+1,t_hats[i][0],stdevs[i],t_hats[i][1],stdevs2[i-1],covs[i]))

'''
---
p-values
---
'''
chisq_list1=[]
chisq_list2=[]
chisq_list3=[]
for a in range(len(d)):
    chisq_list1.append(((d[a]-func1(h[a],*thetahat1))/(sig[a]))**2)
    chisq_list2.append(((d[a]-func2(h[a],*thetahat2))/(sig[a]))**2)
    chisq_list3.append(((d[a]-func3(h[a],*thetahat3))/(sig[a]))**2)
chisq1=sum(chisq_list1)
chisq2=sum(chisq_list2)
chisq3=sum(chisq_list3)
print('Chisq1',chisq1,'\nChisq2',chisq2,'\nChisq3',chisq3)
print('\nChisq1/ndof',chisq1/6,'\nChisq2/ndof',chisq2/5,'\nChisq3/nof',chisq3/5)
print ("\np-value for equation 1 = {0}\n".format(chi2.sf(chisq1, df=6)))
print ("p-value for equation 2 = {0}\n".format(chi2.sf(chisq2, df=5)))
print ("p-value for equation 3 = {0}\n".format(chi2.sf(chisq3, df=5)))
'''
=-=-=-=
Tabel
=-=-=-=
'''
for o in range(len(h)):
    print('%.1f & %.1f & %.1f \\\\' % (h[o], d[o], sig[o]))

'''
=-=-=-=-=-=-=
Newtonian model
=-=-=-=-=-=-=
'''
fig4 = plt.figure(figsize=(10, 8))
ax4 = fig4.add_subplot(1,1,1)
H=770
g=9.81
v=np.linspace(0,1600,num=100)
y=np.sqrt(20/7*H*v)

ax4.plot(x_,func3(x_,*thetahat3),color='tab:red',label='fit')
ax4.errorbar(h,d,yerr=sig,fmt='o',color='black')
ax4.plot(v,y,color='tab:blue',label='Newtonian model')

ax4.set_xlabel(r'$h$ $[punti]$')
ax4.set_ylabel(r'$d$ $[punti]$')

ax4.legend(frameon='true',edgecolor='black',loc='lower right')
ax4.set_xlim(xmin,xmax)
ax4.set_ylim(ymin,ymax)

plt.tight_layout()

fig4.savefig("Newtonian model Plot.pdf", format='pdf')
