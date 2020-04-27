lam=np.linspace(1,(w_max.result['tension']+1)**0.5,200)
E_11=0.5*(lam**2-1)
e_11=0.5*(1-lam**(-2))
e_lin_11=lam-1
plt.xlabel("$\lambda$ in -")
plt.ylabel("11-Component in -")
plt.title("Comparison of Strain Measures (Uniaxial Tension)")
plt.plot(lam,E_11,lam,e_11,lam,e_lin_11)
plt.gca().legend(('Green-Lagrange','Euler-Almansi','Linearization'))
plt.show()

gamma=np.linspace(0,(w_max.result['shear']/2.0)**0.5,200)
E_11=0.5*(gamma**2)
e_11=0.5*(1-(1.0+gamma**2)**(-1))
e_lin_11=np.zeros((200,1))
plt.xlabel("$\gamma$ in -")
plt.ylabel("11-Component in -")
plt.title("Comparison of Strain Measures (Pure Shear)")
plt.plot(gamma,E_11,gamma,e_11,gamma,e_lin_11)
plt.gca().legend(('Green-Lagrange','Euler-Almansi','Linearization'))
plt.show()