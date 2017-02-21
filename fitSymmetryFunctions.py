import numpy as np
import matplotlib.pyplot as plt

# define symmetry functions without the sum to plot

def cutoffFunction(rVector, cutoff, cut=False):   
    
    value = 0.5 * (np.cos(np.pi*rVector / cutoff) + 1)

    # set elements above cutoff to zero so they dont contribute to sum
    if cut:
        value[np.where(rVector > cutoff)[0]] = 0
        
    return value
 
    
def G1(Rij, cutoff):
    
    return cutoffFunction(Rij, cutoff)
    
    
def G2(Rij, width, cutoff, center):
    
    return np.exp(-width*(Rij - center)**2) * cutoffFunction(Rij, cutoff)
    
    
def G3(Rij, cutoff, kappa):
    
    return np.cos(kappa*Rij) * cutoffFunction(Rij, cutoff)
    
    
def G4(Rij, Rik, Rjk, theta, width, cutoff, thetaRange, inversion):
    
    return 2**(1-thetaRange) * (1 + inversion*cos(theta))**thetaRange * \
           np.exp( -width*(Rij**2 + Rik**2 + Rjk**2) ) * \
           cutoffFunction(Rij, cutoff) * cutoffFunction(Rik, cutoff) * cutoffFunction(Rjk, cutoff, cut=True)
           
           
def G5(Rij, Rik, cosTheta, width, cutoff, thetaRange, inversion):
    
    return 2**(1-thetaRange) * (1 + inversion*cosTheta)**thetaRange * \
           np.exp( -width*(Rij**2 + Rik**2) ) * \
           cutoffFunction(Rij, cutoff) * cutoffFunction(Rik, cutoff)

##### test LJ #####

"""Rij = np.linspace(0, 12, 200)

widths = [0.05]#, 0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.1, 0.3, 0.7]
cutoffs = [8.5125]
centers = [0.0, 3.1, 4.5, 5.2, 5.9, 6.8, 7.8]

legends = []
for width in widths:
    for cutoff in cutoffs:
        for center in centers:   
            functionValue = G2(Rij, width, cutoff, center)
            functionValue[np.where(Rij > cutoff)[0]] = 0
            plt.plot(Rij, functionValue)
            legends.append(r'$\eta = %3.2f, R_c = %1.2f, R_s = %1.1f$' % (width, cutoff, center))
            plt.hold('on')
plt.legend(legends)    
plt.show()"""


##### test SW #####

# G2
Rij = np.linspace(0, 5, 200)

widthG2 = [0.01, 0.1, 1.0]
cutoffG2 = [5.0]
centerG2 = [0.0, 2.0, 4.0]

legends = []
for width in widthG2:
    for cutoff in cutoffG2:
        for center in centerG2:   
            functionValue = G2(Rij, width, cutoff, center)
            functionValue[np.where(Rij > cutoff)[0]] = 0
            plt.plot(Rij, functionValue)
            legends.append(r'$\eta = %3.2f, R_c = %1.2f, R_s = %1.1f$' % (width, cutoff, center))
            plt.hold('on')
plt.legend(legends)    
plt.show()

plt.figure()

# G4
Rij = 
Rik = 3.0
theta = np.linspace(0, 2*np.pi, 1000)
Rjk = Rij**2 + Rik**2 - 2*Rij*Rik*np.cos(theta)

widthG4 = [0.01]      
cutoffG4 = [5.0]
thetaRangeG4 = [1, 2, 4] 
inversionG4 = [1.0, -1.0]

legends = []
for width in widthG4:
    for cutoff in cutoffG4:
        for zeta in thetaRangeG4:   
            for inversion in inversionG4:
                functionValue = G4(Rij, Rik, Rjk, theta, width, cutoff, zeta, inversion)
                #functionValue[np.where(Rij > cutoff)[0]] = 0
                plt.plot(theta, functionValue)
                legends.append(r'$\eta = %3.2f, R_c = %1.2f, \zeta = %1.1f, \lambda = %d$' \
                               % (width, cutoff, zeta, inversion) )
                plt.hold('on')
plt.legend(legends)    
plt.show()






