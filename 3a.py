'''
=-=-=-=-=-=-=-=
  Exercise 3
=-=-=-=-=-=-=-=
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2

'''
=-=-=
Data
=-=-=
'''
xmin=0
xmax=100
ymin=0
ymax=60
i   = np.arange(10, 90,step=10)
r   = np.array([8,15.5,22.5,29,35,40.5,45.5,50])
sig = np.ones(8)*0.5
x_= np.linspace(xmin,xmax,num=100)
'''
=-=-=-=-=-=-=-=-=
Functions 1 & 2
=-=-=-=-=-=-=-=-=
'''
def func1(i,*theta_r):
    '''
    Inputs: i, *theta_r
    * denotes vector
    Output: linear function with only one parameter, alpha
    '''
    alpha, = theta_r
    return alpha*i
p01 = np.ones(1)
thetahat1,cov1 = curve_fit(func1, i, r,p01 , sig, absolute_sigma=True)

def func2(i,*theta_r):
    alpha, beta = theta_r
    return alpha*i-beta*i**2
p02 = np.ones(2)
thetahat2,cov2 = curve_fit(func2, i, r,p02 , sig, absolute_sigma=True)

def StDev(x,cov,M):
    k=[]
    for i in range(M):
        for j in range(M):
            k.append(x**(i+j)*cov[i,j])
    return (np.sqrt(sum(k)))

'''
=-=-=-=-=-=
Function 3
=-=-=-=-=-=

'''
i_=np.deg2rad(i)
r_=np.deg2rad(r)
sig_=np.deg2rad(sig)
def func3(i_,*theta_r):
    alpha, = theta_r
    return np.arcsin(np.sin(i_)/(alpha))
p03 = np.ones(1)
thetahat3,cov3 = curve_fit(func3, i_, r_,p03 , sig, absolute_sigma=True)
'''
=-=-=-=
Tabel
=-=-=-=
'''
for o in range(len(i)):
    print('%.1f & %.1f & %.1f \\\\' % (i[o], r[o], sig[o]))
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
for p in range(len(t_hats)):
    if p!=1:
        stdevs.append(np.sqrt(covs[p][0][0]))
        print('Parameter for equation {0}:\n  alpha = {1}+-{2}\n'.format(p+1,t_hats[p][0],stdevs[p]))
    elif p==1:
        stdevs.append(np.sqrt(covs[p][0][0]))
        stdevs2.append(np.sqrt(covs[p][1][1]))
        print('Parameters for equation {0}:\n  alpha = {1}+-{2}\n  beta = {3}+-{4}\n'.format(p+1,t_hats[p][0],stdevs[p],t_hats[p][1],stdevs2[p-1]))
'''
=-=-=-=
Plot 1
=-=-=-=
'''
fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(1,1,1)

ax1.plot(i,r,'o',color='black',label='data')
ax1.errorbar(i,r,yerr=sig,fmt='o',color='black')
ax1.plot(x_,func1(x_,*thetahat1),color='tab:red',label='fit')

ax1.set_xlabel(r'$\theta_{i}$ $[degrees]$')
ax1.set_ylabel(r'$\theta_{r}$ $[degrees]$')

ax1.legend(frameon='true',edgecolor='black',loc='lower right')
ax1.set_xlim(xmin,xmax)
ax1.set_ylim(ymin,ymax)
plt.tight_layout()

fig1.savefig("Plot 1.pdf", format='pdf')

'''
=-=-=-=
Plot 2
=-=-=-=
'''

fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(1,1,1)

ax2.plot(i,r,'o',color='black',label='data')
ax2.errorbar(i,r,yerr=sig,fmt='o',color='black')
ax2.plot(x_,func2(x_,*thetahat2),color='tab:green',label='fit')

ax2.set_xlabel(r'$\theta_{i}$ $[degrees]$')
ax2.set_ylabel(r'$\theta_{r}$ $[degrees]$')

ax2.legend(frameon='true',edgecolor='black',loc='lower right')
ax2.set_xlim(xmin,xmax)
ax2.set_ylim(ymin,ymax)
plt.tight_layout()

fig2.savefig("Plot 2.pdf", format='pdf')

'''
=-=-=-=-=
Goodness
 of fit
=-=-=-=-=
'''
chisq_list1=[]
chisq_list2=[]
chisq_list3=[]
for a in range(len(i)):
    chisq_list1.append(((r[a]-func1(i[a],*thetahat1))/(sig[a]))**2)
    chisq_list2.append(((r[a]-func2(i[a],*thetahat2))/(sig[a]))**2)
    chisq_list3.append(((r_[a]-func3(i_[a],*thetahat3))/(sig_[a]))**2)
chisq1=sum(chisq_list1)
chisq2=sum(chisq_list2)
chisq3=sum(chisq_list3)
print('Chisq1',chisq1,'\nChisq2',chisq2)
print('\nChisq1/ndof',chisq1/8,'\nChisq2/ndof',chisq2/7)
print ("\np-value for equation 1 = {0}\n".format(chi2.sf(chisq1, df=7)))
print ("p-value for equation 2 = {0}\n".format(chi2.sf(chisq2, df=6)))
print ("p-value for equation 3 = {0}\n".format(chi2.sf(chisq3, df=7)))

'''
=-=-=-=
Test Plot
=-=-=-=
'''
x=np.linspace(0,np.pi/2,num=100)
fig3 = plt.figure(figsize=(10, 8))
ax3 = fig3.add_subplot(1,1,1)

ax3.errorbar(i_,r_,yerr=sig_,fmt='o',color='black')
ax3.plot(x,func3(x,*thetahat3),color='tab:green',label='fit')

ax3.legend(frameon='true',edgecolor='black',loc='lower right')
ax3.set_xlim(0,np.pi/2)
ax3.set_ylim(0,1)
#ax3.set_title(r'$Fitted$ $Plot$')
plt.tight_layout()

fig3.savefig("Equation 3 Plot.pdf", format='pdf')
