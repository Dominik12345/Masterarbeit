#name of the figure

name = 'various'



import matplotlib.pyplot as plt
import numpy as np



#read data 
alpha11, alpha21, t1,alpha_hat1 = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running1.txt',unpack = True)
alpha12, alpha22, t2,alpha_hat2 = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running2.txt',unpack = True)
alpha13, alpha23, t3,alpha_hat3 = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running3.txt',unpack = True)
alpha14, alpha24, t4,alpha_hat4 = np.loadtxt(
	'/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running4.txt',unpack = True)
#scale appropriately

t1 = t1[t1<40]
alpha11 = alpha11[:len(t1)]
alpha21 = alpha21[:len(t1)]
alpha_hat1 = alpha_hat1[:len(t1)]

t2 = t2[t2<40]
alpha12 = alpha12[:len(t2)]
alpha22 = alpha22[:len(t2)]
alpha_hat2 = alpha_hat2[:len(t2)]
t3 = t3[t3<40]
alpha13 = alpha13[:len(t3)]
alpha23 = alpha23[:len(t3)]
alpha_hat3 = alpha_hat3[:len(t3)]
t4 = t4[t4<40]
alpha14 = alpha14[:len(t4)]
alpha24 = alpha24[:len(t4)]
alpha_hat4 = alpha_hat4[:len(t4)]





# Phasediagram Plot --->

fig1 = plt.figure()
plt.title('Separatrix')
plt.plot(alpha11,alpha21, 'r--')




fig1.savefig('plots/alpha_running/Phasendiagramm.pdf', bbox_inches='tight')

# <--- Phasediagram Plot 






# running couplings Plot --->

fig2 = plt.figure()
ax21 = fig2.add_subplot(211)
ax22 = fig2.add_subplot(212)

# coupling constants 
#ax2.plot(t,alpha2, 'g:',label=r'$\alpha_2$')

ax21.plot(t1,alpha11, 'b-',label=r'$\alpha_1$')
ax21.plot(t2,alpha12, 'g-',label=r'$\alpha_1$')
ax21.plot(t3,alpha13, 'r-',label=r'$\alpha_1$')
ax21.plot(t4,alpha14, 'b-',label=r'$\alpha_1$')

ax21.plot(t1,alpha_hat1, 'r--',label=r'$\widehat{\alpha}$')
ax21.plot(t2,alpha_hat2, 'r--',label=r'$\widehat{\alpha}$')


ax21.xaxis.grid(True)
ax21.set_xticklabels([])
ax21.legend(frameon=False)



# relative deviation

ax22.plot(t1,(alpha11-alpha_hat1)/alpha_hat1,'b-',
	label=r'$\Delta\alpha$')
ax22.plot(t2,(alpha12-alpha_hat2)/alpha_hat2,'b-',
	label=r'$\Delta\alpha$')

ax22.set_xlabel(r'$t$')
ax22.xaxis.grid(True)
ax22.legend(frameon=False, loc=4)
#safe
fig2.savefig('plots/alpha_running/Kopplungen'+name+'.pdf', bbox_inches='tight')

# <--- Phasediagram Plot 










