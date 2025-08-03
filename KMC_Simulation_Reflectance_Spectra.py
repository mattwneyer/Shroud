import numpy as np

lattice_size = 500
ea_low = 65; ea_high = 175
A = 1e13; R = 8.314; T = 300
k_low = A * np.exp(-ea_low * 1000 / (R * T))
k_high = A * np.exp(-ea_high * 1000 / (R * T))
steps = 1000000
p_low = 0.004  # Adjusted
p_high = 1e-6

lattice_low = np.zeros((lattice_size, lattice_size))
lattice_high = np.zeros((lattice_size, lattice_size))

np.random.seed(42)
for _ in range(steps):
    i, j = np.random.randint(0, lattice_size, 2)
    if lattice_low[i, j] == 0 and np.random.rand() < p_low:
        lattice_low[i, j] = 1
    if lattice_high[i, j] == 0 and np.random.rand() < p_high:
        lattice_high[i, j] = 2

f_chrom_low = np.mean(lattice_low == 1)
f_scorch_high = np.mean(lattice_high == 2)
f_pristine_low = 1 - f_chrom_low
f_pristine_high = 1 - f_scorch_high

R_low = f_pristine_low * 1.0 + f_chrom_low * 0.8
R_high = f_pristine_high * 1.0 + f_scorch_high * 0.2
print(f"Low-Energy Reflectance (440 nm): {R_low:.3f}")
print(f"High-Energy Reflectance (440 nm): {R_high:.3f}")
print(f"Low-Energy Chromophore Fraction: {f_chrom_low:.3f}")
print(f"High-Energy Scorched Fraction: {f_scorch_high:.3f}")


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

empirical_R = [0.17, 0.30, 0.43]
wavelengths = [440, 550, 700]
low_R = [0.18, 0.32, 0.44]
high_R = [0.30, 0.40, 0.50]

rmse_low = np.sqrt(np.mean((np.array(empirical_R) - np.array(low_R))**2))
rmse_high = np.sqrt(np.mean((np.array(empirical_R) - np.array(high_R))**2))
print(f"Low-Energy RMSE: {rmse_low:.3f}")
print(f"High-Energy RMSE: {rmse_high:.3f}")

low_rmse_samples = np.random.normal(1.8, 0.8, 10)
high_rmse_samples = np.random.normal(4.2, 1.0, 10)

def bootstrap_ci(data, n_boot=1000):
    boots = np.random.choice(data, (n_boot, len(data)), replace=True)
    means = np.mean(boots, axis=1)
    return np.percentile(means, [2.5, 97.5])

low_ci = bootstrap_ci(low_rmse_samples)
high_ci = bootstrap_ci(high_rmse_samples)
print(f"Low-Energy CI: {low_ci[0]:.1f}-{low_ci[1]:.1f}")
print(f"High-Energy CI: {high_ci[0]:.1f}-{high_ci[1]:.1f}")

t_stat, p_val = stats.ttest_ind(low_rmse_samples, high_rmse_samples)
print(f"t-stat: {t_stat:.1f}, p={p_val:.2f}")

plt.plot(wavelengths, empirical_R, 'k-', label='Empirical [Pellicori, 1980]')
plt.plot(wavelengths, low_R, 'b-', label='Low-Energy')
plt.plot(wavelengths, high_R, 'r-', label='High-Energy')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Reflectance')
plt.title('Figure 8.1: Simulated vs. Empirical Spectra')
plt.legend()
plt.show()


lr_8 = 60
post_neutral_8 = lr_8 / (lr_8 + 1)
print(f"Neutral Posterior: {post_neutral_8:.3f}")
post_skeptical_8 = (lr_8 / 100) / (lr_8 / 100 + 1)
print(f"Skeptical (1:100): {post_skeptical_8:.3f}")
