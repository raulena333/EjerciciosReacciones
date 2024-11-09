import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

params = {
    'xtick.labelsize': 17,    
    'ytick.labelsize': 17,      
    'axes.titlesize' : 18,
    'axes.labelsize' : 18,
    'legend.fontsize': 16
}
pylab.rcParams.update(params)  # Aplicar los cambios

E_lab = 31  # Energy in the laboratory in MeV
M_projectile = 8  # Mass of lithium-8 in atomic mass units
M_target = 206  # Mass of lead-206 in atomic mass units
Z_projectile = 3 # Charge of the projectile
Z_target = 82 # Charge of the target

E_cm = E_lab * (M_target / (M_projectile + M_target))  

# Calculate the center-of-mass energy
E_cm = E_lab * (M_target / (M_projectile + M_target))
print(f"Center-of-mass energy: {E_cm:.2f} MeV")

# Load potential values
data = np.loadtxt('deflection_function_8Li208Pb_31MeV.txt', skiprows=1)
b = data[:, 0]
theta = data[:, 1]
theta_rutherford = data[:, 2]

# Find the maximum potential value and its corresponding radius
max_theta = np.max(theta)
max_b = b[np.argmax(theta)]
print(f"Maximum angle: {max_theta:.2f} deg at paremetr of imapact: {max_b:.2f} fm")

# Plot the potentials
plt.figure(figsize=(10, 6))
plt.plot(b, theta, label="Deflection function", color = "blue")
plt.plot(b, theta_rutherford, color='red', linestyle='--', label=f"Rutherford deflection function")

# Customize plot
plt.xlabel("Impact parameter (fm)")
plt.ylabel(r"$\Theta$ (deg)")
plt.legend()
plt.ylim(-130, 190) 
plt.xlim(-2.5, 25) 
plt.savefig('DeflectionPlot.pdf')
plt.close()
