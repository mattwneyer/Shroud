# Replication of Version 8 Study 3: Cellulose Crystallinity Index (CI) Decay
# Requirements: pip install numpy matplotlib scipy
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit, fsolve

# Step 1: CI Decay Model [Fanti et al., 2015]
def ci_decay(age, a, b, c):
    """Model: CI = a * exp(-b * age) + c"""
    return a * np.exp(-b * age) + c

# Step 2: Fit Model to Benchmarks
ages_fit = np.array([0, 700, 1965])  # Modern, Medieval, Masada
ci_fit = np.array([90, 71, 46])      # [Fanti et al., 2015; De Caro et al., 2022]
try:
    bounds = ([50, 0.0001, 0], [100, 0.001, 50])  # Constrain parameters
    popt, pcov = curve_fit(ci_decay, ages_fit, ci_fit, p0=[70, 0.000495, 20], bounds=bounds, maxfev=10000)
    a, b, c = popt
    print(f"Fitted Parameters: a={a:.2f}, b={b:.6f}, c={c:.2f}")
except RuntimeError as e:
    print(f"Curve fit failed: {e}. Using paper's parameters: a=70, b=0.000495, c=20")
    a, b, c = 70, 0.000495, 20

# Step 3: Decay Table
ages_table = [0, 500, 1000, 1500, 2000]
ci_table = [ci_decay(age, a, b, c) for age in ages_table]
print("\nCI Decay Table (Age: CI %):")
for age, ci in zip(ages_table, ci_table):
    print(f"{age}: {ci:.2f}%")

# Step 4: Study 3A - Humidity Variance
rates = [0.000345, 0.000495, 0.000645]
print("\nStudy 3A - Humidity Variance:")
for rate in rates:
    print(f"\nRate: {rate}")
    ci_var = [ci_decay(age, a=70, b=rate, c=20) for age in ages_table]
    for age, ci in zip(ages_table, ci_var):
        print(f"{age}: {ci:.2f}%")

# Step 5: Study 3B - Radiation Effects
rates_rad = [0.00055, 0.00065]  # UV Short, Long
print("\nStudy 3B - Radiation Effects:")
for rate in rates_rad:
    print(f"\nRate: {rate} (UV)")
    ci_rad = [ci_decay(age, a=70, b=rate, c=20) for age in ages_table]
    for age, ci in zip(ages_table, ci_rad):
        print(f"{age}: {ci:.2f}%")

# Step 6: Shroud Intersection
shroud_ci = 48
def find_age(age):
    return ci_decay(age, a, b, c) - shroud_ci
intersection_age = fsolve(find_age, 1800)[0]
print(f"\nShroud CI (48%) intersects at ~{intersection_age:.0f} years")

# Step 7: Plot Figure 3.1
os.makedirs('outputs', exist_ok=True)  # Create outputs directory
ages_plot = np.linspace(0, 2000, 1000)
ci_plot = ci_decay(ages_plot, a, b, c)
plt.plot(ages_plot, ci_plot, label='CI Decay Curve')
plt.scatter(ages_fit, ci_fit, color='red', label='Benchmarks')
plt.axhline(48, color='green', linestyle='--', label='Shroud CI 48%')
plt.xlabel('Age (Years)')
plt.ylabel('CI (%)')
plt.title('CI Decay Over Time [Fanti et al., 2015; De Caro et al., 2022]')
plt.legend()
plt.savefig('outputs/figure3.1.png')
plt.show()

# Step 8: Data-Driven LR
from scipy.stats import norm
p_h1 = norm.pdf(48, loc=46, scale=2)  # Ancient: mean 46%, sd 2%
p_h0 = norm.pdf(48, loc=71, scale=5)  # Medieval: mean 71%, sd 5%
lr = p_h1 / p_h0
print(f"\nData-driven LR: {lr:.2e}:1 (P|H1={p_h1:.2e}, P|H0={p_h0:.2e})")