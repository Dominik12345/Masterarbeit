#name of the figure




import matplotlib.pyplot as plt
import numpy as np
import pylab as p
import scipy.constants as const
import itertools

#####################################################
# Definition of the parameters and initial value --->

amz = 0.1185
Nc  = 3.
Nd  = 3.
nfc = 6.
nsc = 0.
nfd = 0.
nsd = 0.
nfj = 0.
nsj = 0.



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

X1 = afX1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**1
Y1 = afY1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2
Z1 = afZ1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2
X2 = afX2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**1
Y2 = afY2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2
Z2 = afZ2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2


# <--- Definition of the parameters and initial value 
#####################################################

################
# read data ---> 
alpha1, alpha2, t = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running.txt',unpack = True)
alpha_SM = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alphahat_running.txt',unpack = True)

#scale appropriately
t = t[t<400]
alpha1 = alpha1[:len(t)]
alpha2 = alpha2[:len(t)]
alpha_SM = alpha_SM[:len(t)]


# <--- read data 
################



#############################
# RUNNING COUPLINGS 1 PLOT --->

fig2 = plt.figure()
ax21 = fig2.add_subplot(111)
#ax22 = fig2.add_subplot(212)

#along separatrix

ax21.plot(t,alpha1, color='0.',linestyle='-',label=r'$\alpha_1$')
ax21.plot(t,alpha2, color='0.5',linestyle='-',label=r'$\alpha_2$')

#SM running
ax21.plot(np.append(0,t),np.append(0.093,alpha_SM), 'k--',label=r'$\alpha$')


#labels etc
ax21.xaxis.grid(True)
ax21.set_xlabel(r'$t$')
#ax21.set_xticklabels([])
box = ax21.get_position()
ax21.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax21.legend(loc='center left',bbox_to_anchor=(1,0.5),frameon=False)



#
#
#ax3 = fig2.add_subplot(222)
#
#ax3.plot(t,(alpha1-alpha_SM)/alpha_SM,color='0.',linestyle='-',label=r'$\Delta \alpha$')
#
#
#ax3.xaxis.grid(True)
#ax3.set_xlabel(r'$t$')
#ax3.legend(loc='center left',bbox_to_anchor=(1,0.5),frameon=False)

#safe
fig2.savefig('plots/alpha_running/Kopplungen1_afix3.pdf', bbox_inches='tight')









