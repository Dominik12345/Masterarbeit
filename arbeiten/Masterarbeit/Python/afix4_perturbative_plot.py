import matplotlib.pyplot as plt
import numpy as np
import pylab as p
import scipy.constants as const
import itertools


def afX1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj): 
	return( (2./3.*1./2.*2.*(nfc+Nd*nfj)+1./3.*1./2.*(nsc+Nd*nsj)
		-11./3.*Nc)/(16.*const.pi**2) )

def afY1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return( ( (10./3.*Nc+2.*(Nc**2.-1.)/(2.*Nc) )*1./2.*2.*(nfc+Nd*nfj)+
		(2./3.*Nc+4.*(Nc**2.-1.)/(2.*Nc))*1./2.*(nsc+Nd*nsj)-
		34./3.*Nc**2. )/((16.*const.pi**2)**2) )

def afZ1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return( (2.*(Nd**2.-1.)/(2.*Nd)*1./2.*2.*(Nd*nfj)
		+4.*(Nd**2-1.)/(2.*Nd)*1./2.*Nd*nsj)/((16.*const.pi**2)**2))

# in afZ1 Nd <-> Nc ???

def afX2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return(afX1(Nd,Nc,nfd,nsd,nfc,nsc,nfj,nsj))
def afY2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return(afY1(Nd,Nc,nfd,nsd,nfc,nsc,nfj,nsj))
def afZ2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return(afZ1(Nd,Nc,nfd,nsd,nfc,nsc,nfj,nsj))


# right norm 1/4pi
def X1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return(afX1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**1)
def Y1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj): 
	return(afY1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2)
def Z1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj): 
	return(afZ1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2)
def X2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj): 
	return(afX2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**1)
def Y2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj): 
	return(afY2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2)
def Z2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj): 
	return(afZ2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2)

def afix4(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return(np.array([(Z1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*X2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)-
		X1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*Y2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj))/
	(Y1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*Y2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)-
		Z1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*Z2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj))
	,
	(Z2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*X1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)-
		X2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*Y1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj))/
	(Y1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*Y2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)-
		Z1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*Z2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj))
	]))



#make figure
fig = plt.figure()
ax = fig.add_subplot(111)

###
# 3,2,6,0,0,nsd=0,0,nsj
###

#creates 2 x len(nsd) matrix, plot line1-x, line2-y
nsj=np.linspace(2.98,14,100)

nsd=0
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 color='0.8',linestyle='-', label=r'$n_{\mathrm{s}_\mathrm{d}}=0$')

nsd=1
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 color='0.6',linestyle='-', label=r'$n_{\mathrm{s}_\mathrm{d}}=1$')

nsd=2
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 color='0.4',linestyle='-', label=r'$n_{\mathrm{s}_\mathrm{d}}=2$')

nsd=3
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 color='0.2',linestyle='-', label=r'$n_{\mathrm{s}_\mathrm{d}}=3$')

#
nsd=np.linspace(-1,4,50)


nsj=3
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 'k--',dashes=(3,2), label=r'$n_{\mathrm{s}_\mathrm{j}}$')

nsj=4
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 'k--',dashes=(3,2))#, label=r'$n_{\mathrm{s}_\mathrm{j}}=4$')

nsd=np.linspace(-2,5,50)

nsj=5
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 'k--',dashes=(3,2))#, label=r'$n_{\mathrm{s}_\mathrm{j}}=5$')


nsj=6
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 'k--',dashes=(3,2))#, label=r'$n_{\mathrm{s}_\mathrm{j}}=6$')

nsj=7
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 'k--',dashes=(3,2))#, label=r'$n_{\mathrm{s}_\mathrm{j}}=7$')

nsj=8
ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
	 'k--',dashes=(3,2))#, label=r'$n_{\mathrm{s}_\mathrm{j}}=8$')

#nsj=9
#ax.plot(afix4(3,2,6,0,0, nsd,0,nsj)[0],
#	    afix4(3,2,6,0,0, nsd,0,nsj)[1],
#	 'k-')#, label=r'$n_{\mathrm{s}_\mathrm{j}}=9$')








#legend etc
ax.set_xlabel(r'$\alpha_\mathrm{s}$')
ax.set_ylabel(r'$\alpha_\mathrm{d}$')

p.ylim([0,22])

#box = ax.get_position()
ax.xaxis.grid(True)
ax.yaxis.grid(True)
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left',bbox_to_anchor=(1,0.5),frameon=False)

#save fig
#plt.show()
fig.savefig('plots/afix4_perturbative/afix4_perturbative.pdf', bbox_inches='tight')
