from numpy import *
import scipy.constants as const

def afX1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj): 
	return( (2./3.*1./2.*2.*(nfc+Nd*nfj)+1./3.*1./2.*(nsc+Nd*nsj)-11./3.*Nc)/(16.*const.pi**2) )

def afY1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return( ( (10./3.*Nc+2.*(Nc**2.-1.)/(2.*Nc) )*1./2.*2.*(nfc+Nd*nfj)+
		(2./3.*Nc+4.*(Nc**2.-1.)/(2.*Nc))*1./2.*(nsc+Nd*nsj)-34./3.*Nc**2. )/((16.*const.pi**2)**2) )

def afZ1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return( (2.*(Nc**2.-1.)/(2.*Nc)*1./2.*2.*(Nd*nfj)
		+4.*(Nc**2-1.)/(2.*Nc)*1./2.*Nd*nsj)/((16.*const.pi**2)**2))

def afX2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return(afX1(Nd,Nc,nfd,nsd,nfc,nsc,nfj,nsj))
def afY2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return(afY1(Nd,Nc,nfd,nsd,nfc,nsc,nfj,nsj))
def afZ2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj):
	return(afZ1(Nd,Nc,nfd,nsd,nfc,nsc,nfj,nsj))


Nc 	= 3
Nd 	= 'D'
nfc = 6
nsc = 0
nfd = 'F'
nsd = 0
nfj = 'J'
nsj = 0


X1 = afX1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)
Y1 = afY1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)
Z1 = afZ1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)
X2 = afX2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)
Y2 = afY2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)
Z2 = afZ2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)




print('X1 = ' + str(X1))
print('Y1 = ' + str(Y1))
print('Z1 = ' + str(Z1))
print('X2 = ' + str(X2))
print('Y2 = ' + str(Y2))
print('Z2 = ' + str(Z2))