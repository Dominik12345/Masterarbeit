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
alpha11, alpha21, t1, alpha_SM1 = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_2_6_0_3_0_1_0_her.txt',unpack = True)
alpha12, alpha22, t2, alpha_SM2 = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_3_6_0_9_0_1_0_her.txt',unpack = True)
alpha13, alpha23, t3, alpha_SM3 = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_4_6_0_17_0_1_0_her.txt',unpack = True)
alpha14, alpha24, t4, alpha_SM4 = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_5_6_0_24_0_1_0_her.txt',unpack = True)
alpha15, alpha25, t5, alpha_SM5 = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_3_6_0_10_0_2_0_her.txt',unpack = True)
#	
#alpha11, alpha21, t1, alpha_SM1 = np.loadtxt(
#	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_1.txt',unpack = True)
#alpha12, alpha22, t2, alpha_SM2 = np.loadtxt(
#	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_3_6_0_9_0_1_0.txt',unpack = True)
#alpha13, alpha23, t3, alpha_SM3 = np.loadtxt(
#	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_4_6_0_17_0_1_0.txt',unpack = True)
#alpha14, alpha24, t4, alpha_SM4 = np.loadtxt(
#	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_5_6_0_24_0_1_0.txt',unpack = True)
#alpha15, alpha25, t5, alpha_SM5 = np.loadtxt(
#	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3_3_6_0_10_0_2_0.txt',unpack = True)

#scale appropriately
t1 = t1[t1<100]
alpha11 = alpha11[:len(t1)]
alpha21 = alpha21[:len(t1)]
alpha_SM1 = alpha_SM1[:len(t1)]
t2 = t2[t2<100]
alpha12 = alpha12[:len(t2)]
alpha22 = alpha22[:len(t2)]
alpha_SM2 = alpha_SM2[:len(t2)]
t3 = t3[t3<100]
alpha13 = alpha13[:len(t3)]
alpha23 = alpha23[:len(t3)]
alpha_SM3 = alpha_SM3[:len(t3)]
t4 = t4[t4<100]
alpha14 = alpha14[:len(t4)]
alpha24 = alpha24[:len(t4)]
alpha_SM4 = alpha_SM4[:len(t4)]
t5 = t5[t5<100]
alpha15 = alpha15[:len(t5)]
alpha25 = alpha25[:len(t5)]
alpha_SM5 = alpha_SM5[:len(t5)]


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

ax21.plot(t1,alpha11, color='0.',linestyle='-',label=r'$\alpha_1^\mathrm{a}$')
ax21.plot(t2,alpha12, color='0',linestyle=':',label=r'$\alpha_1^\mathrm{b}$')
ax21.plot(t5,alpha15, color='0.7',linestyle='-',label=r'$\alpha_1^\mathrm{c}$')
ax21.plot(t3,alpha13, color='0.4',linestyle='-',label=r'$\alpha_1^\mathrm{d}$')
ax21.plot(t4,alpha14, color='0.2',linestyle='-',label=r'$\alpha_1^\mathrm{e}$')






#SM running
# ax21.plot(t1,alpha_SM1, 'r:',label=r'$\alpha_{\mathrm{SM-QCD1}}$')
ax21.plot(t2,alpha_SM2, 'k--',label=r'$\alpha_{\mathrm{SM-QCD}}$')
#ax21.plot(t3,alpha_SM3, 'g:',label=r'$\alpha_{\mathrm{SM-QCD3}}$')
#ax21.plot(t4,alpha_SM4, 'm:',label=r'$\alpha_{\mathrm{SM-QCD4}}$')

#labels etc
ax21.xaxis.grid(True)
ax21.set_xlabel(r'$t$')
#ax21.set_xticklabels([])
box = ax21.get_position()
ax21.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax21.legend(loc='center left',bbox_to_anchor=(1,0.5),frameon=False)


#safe
fig2.savefig('plots/alpha_running/Kopplungen1_her.pdf', bbox_inches='tight')

# <--- RUNNING COUPLINGS PLOT
#############################

#############################
# RUNNING COUPLINGS 2 PLOT --->

fig4 = plt.figure()
ax22 = fig4.add_subplot(111)
#ax22 = fig2.add_subplot(212)

# coupling constants 
#ax2.plot(t,alpha2, 'g:',label=r'$\alpha_2$')

#along separatrix
ax22.plot(t1,alpha21, color='0.0',linestyle='-',label=r'$\alpha_2^\mathrm{a}$')
ax22.plot(t2,alpha22, color='0.0',linestyle=':',label=r'$\alpha_2^\mathrm{b}$')
ax22.plot(t5,alpha25, color='0.7',linestyle='-',label=r'$\alpha_2^\mathrm{c}$')
ax22.plot(t3,alpha23, color='0.4',linestyle='-',label=r'$\alpha_2^\mathrm{d}$')
ax22.plot(t4,alpha24, color='0.2',linestyle='-',label=r'$\alpha_2^\mathrm{e}$')


#SM running
# ax21.plot(t1,alpha_SM1, 'r:',label=r'$\alpha_{\mathrm{SM-QCD1}}$')
#ax21.plot(t2,alpha_SM2, 'k--',label=r'$\alpha_{\mathrm{SM-QCD}}$')
#ax21.plot(t3,alpha_SM3, 'g:',label=r'$\alpha_{\mathrm{SM-QCD3}}$')
#ax21.plot(t4,alpha_SM4, 'm:',label=r'$\alpha_{\mathrm{SM-QCD4}}$')

#labels etc
ax22.xaxis.grid(True)
ax22.set_xlabel(r'$t$')
#ax21.set_xticklabels([])
box = ax22.get_position()
ax22.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax22.legend(loc='center left',bbox_to_anchor=(1,0.5),frameon=False)


#safe
fig4.savefig('plots/alpha_running/Kopplungen2_her.pdf', bbox_inches='tight')

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

ax3.plot(t1,(alpha11-alpha_SM1)/alpha_SM1,color='0.',linestyle='-',label=r'$\Delta \alpha^\mathrm{a}$')
ax3.plot(t2,(alpha12-alpha_SM2)/alpha_SM2,color='0.',linestyle=':',label=r'$\Delta \alpha^\mathrm{b}$')
ax3.plot(t5,(alpha15-alpha_SM5)/alpha_SM5,color='0.7',linestyle='-',label=r'$\Delta \alpha^\mathrm{c}$')
ax3.plot(t3,(alpha13-alpha_SM3)/alpha_SM3,color='0.4',linestyle='-',label=r'$\Delta \alpha^\mathrm{d}$')
ax3.plot(t4,(alpha14-alpha_SM4)/alpha_SM4,color='0.2',linestyle='-',label=r'$\Delta \alpha^\mathrm{e}$')

ax3.xaxis.grid(True)
ax3.set_xlabel(r'$t$')
ax3.legend(loc='center left',bbox_to_anchor=(1,0.5),frameon=False)
#safe
fig3.savefig('plots/alpha_running/relative_deviation_her.pdf', bbox_inches='tight')


# <--- RELATIVE DEVIATION 
#########################








