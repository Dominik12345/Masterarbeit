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
Nd  = 2.
nfc = 6.
nsc = 0.
nfd = 0.
nsd = 1.
nfj = 0.
nsj = 9.



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
alpha11, alpha21, t1, alpha_SM1 = np.loadtxt( 
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_2_6_0_0_1_0_9.txt',unpack = True)

#scale appropriately
t1 = t1[t1<400]
alpha11 = alpha11[:len(t1)]
alpha21 = alpha21[:len(t1)]
alpha_SM1 = alpha_SM1[:len(t1)]



# <--- read data 
################



#############################
# RUNNING COUPLINGS 1 PLOT --->

fig2 = plt.figure()
ax21 = fig2.add_subplot(111)
#ax22 = fig2.add_subplot(212)

# coupling constants 
#ax2.plot(t,alpha2, 'g:',label=r'$\alpha_2$')

#along separatrix

ax21.plot(t1,alpha11, color='0.',linestyle='-',label=r'$\alpha_1^\mathrm{f}$')
#ax21.plot(t1,alpha21, color='0.5',linestyle='-',label=r'$\alpha_2^\mathrm{f}$')
ax21.plot(t1,alpha_SM1, 'k--',label=r'$\alpha$')
#SM running


#labels etc
ax21.xaxis.grid(True)
ax21.set_xlabel(r'$t$')
ax21.set_ylabel(r'Kopplungsstärke')
#ax21.set_xticklabels([])
box = ax21.get_position()
ax21.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax21.legend(loc='center left',bbox_to_anchor=(1,0.5),frameon=False)


#safe
fig2.savefig('plots/alpha_running/Kopplungen1_afix4.pdf', bbox_inches='tight')

# <--- RUNNING COUPLINGS PLOT
#############################


#########################
# RELATIVE DEVIATION --->
def A1loop(t):
	return(1./(1./amz - X1*t))




# plot

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)

#ax3.plot(t_SM,alpha_SM,'r.',label=r'2-Loop')
#ax3.plot(t_SM,A1loop(t_SM),'k-',label=r'1-Loop')

ax3.plot(t1,(alpha11-alpha_SM1)/alpha_SM1,color='0.',linestyle='-',label=r'$\Delta \alpha^\mathrm{f}$')



ax3.xaxis.grid(True)
ax3.set_xlabel(r'$t$')
ax3.legend(loc='center left',bbox_to_anchor=(1,0.5),frameon=False)
#safe
fig3.savefig('plots/alpha_running/relative_deviation_afix4.pdf', bbox_inches='tight')


# <--- RELATIVE DEVIATION 
#########################








