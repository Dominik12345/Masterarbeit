from numpy import *
import pylab as p
import scipy.constants as const
import itertools


# Definition of the parameters and initial value


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



#reduced parameters

B=array([
#	[ 3, 1, 6, 1, 6,3*15, 0,15],
#	[ 3, 1, 6, 2, 6,3*15, 0,15],
#	[ 3, 1, 6, 3, 6,3*15, 0,15],
#	[ 3, 1, 6, 4, 6,3*15, 0,15],
#	[ 3, 1, 6, 5, 6,3*15, 0,15],
#	[ 3, 1, 6, 6, 6,3*15, 0,15],
#	[ 3, 1, 6, 7, 6,3*15, 0,15],
#	[ 3, 1, 6,14, 6,3*14, 0,14],
#	[ 3, 2,17, 0, 12, 0, 1, 0],
#	[ 3, 2,18, 0,13, 0, 1, 0]
	])

#A=array([ B[:,0] ,
#		  B[:,1] ,
#		  B[:,2] - B[:,1] * B[:,6] ,
#		  B[:,3] - B[:,1] * B[:,7] ,
#		  B[:,4] - B[:,0] * B[:,6] ,
#		  B[:,5] - B[:,0] * B[:,7] ,
#		  B[:,6] ,
#		  B[:,7] 
#	]).transpose()
#real parameters

A=array([
#	[ 3, 3, 6, 0, 8, 0, 1, 0],
#	[ 3, 3, 6, 0, 9, 0, 1, 0],
#	[ 3, 3, 6, 0,10, 0, 1, 0],
#	[ 3, 3, 6, 0,11, 0, 1, 0],
#	[ 3, 3, 6, 0,12, 0, 1, 0],
#	[ 3, 3, 6, 0,13, 0, 1, 0],
#	[ 3, 2, 6, 0, 3, 0, 1, 0],
#	[ 3, 3, 6, 0, 0, 0, 0, 3],
#	[ 3, 3, 6, 0, 5, 2, 3, 0],
	[ 3, 3, 6, 0, 5, 2, 3, 0]
	])





for (Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj) in A:

	X1 = afX1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**1
	Y1 = afY1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2
	Z1 = afZ1(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2
	X2 = afX2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**1
	Y2 = afY2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2
	Z2 = afZ2(Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj)*2*(4*const.pi)**2
	counter = str(Nc)+"_"+str(Nd)+"_"+str(nfc)+"_"+str(nsc)+"_"+str(nfd)+"_"+str(nsd)+"_"+str(nfj)+"_"+str(nsj)







	if (Y1*Y2-Z1*Z2==0):
	 	print(str(Nc)+"_"+str(Nd)+"_"+str(nfc)+"_"+str(nsc)+"_"+str(nfd)+"_"+str(nsd)+"_"+str(nfj)+"_"+str(nsj)+"unzulässig")
	
	
	
	delta_a=array([0.1, 0.1])
	
	
	# ---BETA FUNCTION SETUP---
	
	#beta-function
	def beta(a,t=0):
		return array([X1*a[0]**2+Y1*a[0]**3+Z1*a[0]**2*a[1],
					  X2*a[1]**2+Y2*a[1]**3+Z2*a[1]**2*a[0]])
	
	# Fixedpoints afix
	
	afix1 = array([0,0])
	if (Y2!=0 and -X2/Y2>=0):
		afix2 = array([0,-X2/Y2])	
	else: 
		afix2 = array([0,0])
	if (Y1!=0 and -X1/Y1>=0):
		afix3 = array([-X1/Y1,0])
	else:
		afix3 = array([0,0])
	if ((Y1*Y2-Z1*Z2)!=0 and (Z1*X2-X1*Y2)/(Y1*Y2-Z1*Z2)>=0 and (Z2*X1-X2*Y1)/(Y1*Y2-Z1*Z2)>=0):
		afix4 = array([(Z1*X2-X1*Y2)/(Y1*Y2-Z1*Z2),(Z2*X1-X2*Y1)/(Y1*Y2-Z1*Z2)])
	else:
		afix4 = array([0,0])
	
	#stability matrix
	def db_da(a, t=0):
		return array ([ [2*X1*a[0]+3*Y1*a[0]**2+2*Z1*a[0]*a[1], Z1*a[0]**2],
						[Z2*a[1]**2, 2*X2*a[1]+3*X2*a[1]**2+2*Z2*a[0]*a[1]]   ])
	
	

	#RG-time and initial value
	t = linspace(0, 10, 1000)
	a0 = afix4+delta_a

	# == Integrating the ODE using scipy.integate ==
	from scipy import integrate

	f2 = p.figure()
	
	# define a grid and compute direction at each point
	ymax = max(afix1[1],afix2[1],afix3[1],afix4[1])              # get axis limits
	xmax = max(afix1[0],afix2[0],afix3[0],afix4[0])
	ymin = min(afix1[1],afix2[1],afix3[1],afix4[1])             # get axis limits
	xmin = min(afix1[0],afix2[0],afix3[0],afix4[0])
	
	ymax += 0.2*abs(max(ymax,xmax))
	xmax += 0.2*abs(max(ymax,xmax))
	ymin -= 0.2*abs(min(ymax,xmax))
	xmin -= 0.2*abs(min(ymax,xmax))
	
	
	
	
	nb_points   = 22

	x = linspace(xmin, xmax, nb_points)
	y = linspace(ymin, ymax, nb_points)
	
	a1 , b1  = meshgrid(x, y)                       # create a grid
	Da1, Db1 = beta([a1, b1])                      # compute growth rate on the gridt
	M = (hypot(Da1, Db1))                           # Norm of the growth rate 
	M[ M == 0] = 1.                                 # Avoid zero division errors 
	Da1 /= M                                        # Normalize each arrows
	Db1 /= M                                  
	
	#-------------------------------------------------------
	# Drow direction fields, using matplotlib 's quiver function
	# I choose to plot normalized arrows and to use colors to give information on
	# the growth speed
	#p.title('Nc='+str(Nc)+ ', Nd='+str(Nd)+', nfc='+str(nfc)+', nsc='+str(nsc)+', nfd='+str(nfd)+', nsd='+str(nsd)+', nfj='+str(nfj)+', nsj=' + str(nsj))
	Q = p.quiver(a1, b1, Da1, Db1,  pivot='mid', cmap=p.cm.jet)
	

	
	p.plot(afix1[0],afix1[1], 'go', label=r'$\alpha^{*}_\mathrm{Gauß}$' ,markersize=9)
	if (afix2[1]>0):
		p.plot(afix2[0],afix2[1], 'g^', label=r'$\alpha^{*}_\mathrm{tw2}$' ,markersize=9)
	if (afix3[0]>0):
		p.plot(afix3[0],afix3[1], 'gv', label=r'$\alpha^{*}_\mathrm{tw1}$' ,markersize=9)
	if (afix4[0]>0):
		p.plot(afix4[0],afix4[1], 'g*', label=r'$\alpha^{*}_\mathrm{vw}$' ,markersize=9)

	
	p.grid()
	p.xlim(xmin, xmax)
	p.ylim(ymin, ymax)

	p.xlabel(r'$\alpha_1$')
	p.ylabel(r'$\alpha_2$')
	p.legend(numpoints=1)
	

	f2.savefig('plots/RG_flow/RG_flow'+counter+'.png')
	
