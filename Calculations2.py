import numpy as np

# Constants and given values
E_lab = 31  # Energy in the laboratory in MeV
M_projectile = 8  # Mass of lithium-8 in atomic mass units
M_target = 206  # Mass of lead-206 in atomic mass units
Z_projectile = 3  # Charge of the projectile
Z_target = 82  # Charge of the target
e2 = 1.44  # e^2/(4πε₀) in MeV·fm (Coulomb constant)

# Calculate the center-of-mass energy
E_cm = E_lab * (M_target / (M_projectile + M_target))
print(f"Center-of-mass energy: {E_cm:.2f} MeV")

# Calculate the reduced mass
mu = (M_projectile * M_target) / (M_projectile + M_target)
print(f"Reduced mass: {mu:.2f} MeV/c^2")

# Calculate the Coulomb diffusion parameter (a₀)
a_0 = (Z_projectile * Z_target * e2) / (2 * E_cm)
print(f"Coulomb diffusion parameter (a₀): {a_0:.2f} fm")

# Calculate the closest distance of approach (r₀)
r_0 = 2 * a_0
print(f"Closest approach distance (r₀): {r_0:.2f} fm")

# Planck's constant (reduced h-bar) in MeV·fm/c
hbar = 1.9732699e-14  # MeV·fm/c (value of h-bar in these units)
u = 1.6605e-27
j = 1.60218e-13

# Calculate the wave number (k) and lambda_0 (De Broglie wavelength)
k = np.sqrt(2 * mu * u * E_cm) / hbar
lambda_0 = 2*np.pi /k 
print(f" Wavelenght : {lambda_0:.4f} fm^-1")

# Sommerfeld parameter (η)
sommerfield = k * r_0 / 2
print(f"Sommerfeld parameter (η): {sommerfield:.2f}")
