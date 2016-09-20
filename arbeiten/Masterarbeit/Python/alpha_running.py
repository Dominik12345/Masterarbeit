import matplotlib.pyplot as plt
import numpy as np



#read data 
alpha1, alpha2, t = np.loadtxt('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running.txt',unpack = True)
alpha_hat = np.loadtxt('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alphahat_running.txt')

#scale appropriately

t = t[t<30]
alpha1 = alpha1[:len(t)]
alpha2 = alpha2[:len(t)]
alpha_hat = alpha_hat[:len(t)]






# Phasediagram Plot --->

fig1 = plt.figure()
plt.title('Separatrix')
plt.plot(alpha1,alpha2, 'r--')




fig1.savefig('plots/alpha_running/Phasendiagramm.pdf', bbox_inches='tight')

# <--- Phasediagram Plot 






# Phasediagram Plot --->

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

#ax.set_title(r'')
ax2.plot(t,alpha1, 'b-',label=r'$\alpha_1$')
ax2.plot(t,alpha2, 'g:',label=r'$\alpha_2$')
ax2.plot(t,alpha_hat, 'r--',label=r'$\widehat{\alpha}_1$')


ax2.set_xlabel(r'$t$')
#ax2.set_ylabel(r'Kopplungsstärke')

ax2.legend(frameon=False)


fig2.savefig('plots/alpha_running/Kopplungen.pdf', bbox_inches='tight')

# <--- Phasediagram Plot 

















