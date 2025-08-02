import numpy as np
import matplotlib.pyplot as plt

features = ['Wrist/Forearm Flows', 'Side Wound', 'Crown Punctures', 'Scourge Marks', 'Feet Wounds', 'Belt of Blood']
lrs = [3.5, 8.5, 5.3, 3, 0.5, 0.8]  # From paper
colors = ['green' if lr >= 1 else 'red' for lr in lrs]

plt.figure(figsize=(10, 6))
plt.bar(features, lrs, color=colors)
plt.axhline(y=1, color='black', linestyle='--', label='Neutral LR=1')
plt.ylabel('Likelihood Ratio (H1:H0)')
plt.title('Figure 6.1: LR Contributions for Trauma Features')
plt.xticks(rotation=45, ha='right')
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.show()  # Matches paper’s visualization
