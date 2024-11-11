import numpy as np

# Constants and given values
E_lab = 31  # Energy in the laboratory in MeV
M_projectile = 8  # Mass of lithium-8 in atomic mass units
M_target = 206  # Mass of lead-206 in atomic mass units
Z_projectile = 3  # Charge of the projectile
Z_target = 82  # Charge of the target
e2 = 1.44  # e^2/(4πε₀) in MeV·fm (Coulomb constant)
massUnits_toMev = 931.5 # conversion for mass units to energy units

excitation = 0.9808  # excitation from excitated state to ground state in MeV

# Calculate the center-of-mass energy
E_cm = E_lab * (M_target / (M_projectile + M_target))
print(f"Center-of-mass energy: {E_cm:.2f} MeV")

# Calculate the reduced mass
mu = (M_projectile * M_target) / (M_projectile + M_target)
muMev = mu * massUnits_toMev
print(f"Reduced mass: {mu:.2f} uma")
print(f'Reduced mass, {muMev:.2f} Mev/c^2')

# Calculate the Coulomb diffusion parameter (a₀)
a_0 = (Z_projectile * Z_target * e2) / (2 * E_cm)
print(f"Coulomb diffusion parameter (a₀): {a_0:.3f} fm")

# Calculate the closest distance of approach (r₀)
r_0 = 2 * a_0
print(f"Closest approach distance (r₀): {r_0:.2f} fm")

# Planck's constant (reduced h-bar) in MeV·fm/c
hbar = 4.135667696e-12  # MeV /s (value of h-bar in these units)
hbarc = 197.327 # Value in Mev/fm

# Calculate the wave number (k) and lambda_0 (De Broglie wavelength)
k = (np.sqrt(2 * muMev * E_cm)) /hbar * 1e-15 
lambda_0 = 1 / k
print(f" Wavelenght : {lambda_0:.4f} fm^-1")
print(f' Wavenumber : {k:.4f} fm')

# Sommerfeld parameter (η)
sommerfield = lambda_0 * r_0 / 2
sommerfield2 = a_0 / k
print(f"Sommerfeld parameter (η): {sommerfield:.3f}")
print(f'Sommerfield parameter : {sommerfield2:.3f}')

angles = {30, 60, 90, 120, 150, 180}

# Cotangent function
def cotan(x):
    return np.cos(x) / np.sin(x)

# Function to calculate b, maximum approach distance, and cross-section
def b_maxacercamiento_seccion(theta):
    theta_rad = np.radians(theta)  # Convert degrees to radians
    b = a_0 * cotan(theta_rad / 2)
    max_acercamiento = a_0 * (1 / (1 + np.sin(theta_rad / 2)))
    seccion_eficaz = (a_0 / 2)**2 / (np.sin(theta_rad / 2)**4)
    return b, max_acercamiento, seccion_eficaz

# Loop through each angle and calculate values
for theta in angles:
    b, max_acerca, seccion = b_maxacercamiento_seccion(theta)
    print(f'For angle {theta}°:')
    print(f'b = {b:.2f} fm , r_ca = {max_acerca:.2f} fm , dsigma = {10*seccion:.2f} mb/sr\n')

v = np.sqrt(2 * E_lab / (8 * muMev))
tau_col = (a_0 / v)
adiabaticidad = excitation / hbarc *tau_col
print(f'Adiabatic parameter for $^8Li$ : {adiabaticidad:.3f}')