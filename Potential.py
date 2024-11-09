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

# Calculate the center-of-mass energy and other
E_cm = E_lab * (M_target / (M_projectile + M_target))
print(f"Center-of-mass energy: {E_cm:.2f} MeV")

# Load potential values
data = np.loadtxt('Potentials_plot_data.txt', skiprows=3)
radius = data[:, 0]
potential_values = data[:, 1]

# Find the maximum potential value and its corresponding radius
max_potential = np.max(potential_values)
max_radius = radius[np.argmax(potential_values)]
theory_radius = 1.45 * (M_projectile**(1/3) + M_target**(1/3))
theory_potential = 1.44 * (Z_projectile * Z_target) / (theory_radius)
print(f"Maximum potential: {max_potential:.2f} MeV at radius: {max_radius:.2f} fm")
print(f"Maximum theorical potential : {theory_potential:.2f} Mev at theorical radius: {theory_radius:.2f} fm")

# Plot the potentials
plt.figure(figsize=(10, 6))
plt.plot(radius, potential_values, label="Coulomb Potential", color = "black")
plt.plot([0, 25], [E_cm, E_cm], color='red', linestyle='--', label=f"E_cm = {E_cm:.2f} MeV")

# Customize plot
plt.xlabel("r (fm)")
plt.ylabel("V(r) (MeV)")
#plt.title("Coulomb + Woods-Saxon Potential as a Function of Radius")
plt.legend()
plt.ylim(-100, 40) 
plt.xlim(-2.5, 27.5) 
plt.savefig('PotantialPlot.pdf')
plt.close()
