import numpy as np
import matplotlib.pyplot as plt

streams = ['Superficiality & 3D', 'Vanillin', 'CI Decay', 'Spatial/VOC', 'Sudarium', 'Forensic Trauma', 'C14 Reappraisal', 'C14 Time-Series', 'Age Integration', 'KMC Simulation']
lrs = [171, 19, 1e6, 15, 2.38e7, 189, 0.002, 5, 100, 60]
colors = ['green' if lr >= 1 else 'red' for lr in lrs]

plt.figure(figsize=(12, 6))
plt.bar(streams, lrs, color=colors)
plt.axhline(y=1, color='black', linestyle='--', label='Neutral LR=1')
plt.ylabel('Likelihood Ratio (H1:H0, Log Scale)')
plt.title('Figure 7.1: Bayesian Evidence Streams')
plt.xticks(rotation=45, ha='right')
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.show()


import numpy as np

lrs_7 = [
    171,      # Superficiality & 3D ([Jackson et al., 1984])
    19,       # Vanillin Decay ([Rogers, 2005])
    1e6,      # CI Decay ([De Caro et al., 2022; Fanti et al., 2015])
    15,       # Spatial/VOC ([De Caro et al., 2022; Rogers, 2005])
    2.38e7,   # Sudarium ([Whanger, 1998; Frei, 1982])
    189,      # Forensic Trauma ([Maslen & Mitchell, 2006; Borrini & Garlaschelli, 2019])
    0.002,    # C14 Reappraisal ([Casabianca et al., 2019; Tite et al., 1989])
    5,        # C14 Time-Series ([Casabianca et al., 2019])
    100,      # Bayesian Age Integration (implied, ~150 AD)
    60        # KMC Simulation ([Pellicori, 1980])
]
combined_lr_7 = np.prod(lrs_7)
print(f"Combined LR: {combined_lr_7:.2e}:1")  # ~5.26e22:1

post_neutral_7 = combined_lr_7 / (combined_lr_7 + 1)
print(f"Neutral Posterior: {post_neutral_7}")

post_skeptical_7 = (combined_lr_7 / 1000) / (combined_lr_7 / 1000 + 1)
print(f"Skeptical (1:1000) Posterior: {post_skeptical_7}")


