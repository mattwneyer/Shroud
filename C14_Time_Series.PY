# Replication of Version 8 Study 6B: C14 Time-Series Analysis
# Requirements: pip install numpy scipy matplotlib
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Step 1: Raw BP Data [Casabianca et al., 2019, Table 1]
arizona_bp = [606, 574, 753, 745, 632, 676, 540, 701]
oxford_bp = [795, 730, 690]
zurich_bp = [733, 722, 635, 617, 595]

# Step 2: Compute Slope and p-value
def compute_slope_p(bp_values):
    x = np.arange(1, len(bp_values) + 1)
    slope, intercept, r, p, std_err = stats.linregress(x, bp_values)
    return slope, p

slope_az, p_az = compute_slope_p(arizona_bp)
print(f"Arizona: Slope {slope_az:.2f}, p={p_az:.3f}")

slope_ox, p_ox = compute_slope_p(oxford_bp)
print(f"Oxford: Slope {slope_ox:.2f}, p={p_ox:.3f}")

slope_zu, p_zu = compute_slope_p(zurich_bp)
print(f"Zurich: Slope {slope_zu:.2f}, p={p_zu:.3f}")

# Step 3: Figure 6B.1 - Zurich Plot
os.makedirs('outputs', exist_ok=True)
x_zu = np.arange(1, len(zurich_bp) + 1)
plt.plot(x_zu, zurich_bp, 'o', label='Zurich BP')
plt.plot(x_zu, slope_zu * x_zu + stats.linregress(x_zu, zurich_bp)[1], 'r', label=f'Slope -38.1, p=0.011')
plt.xlabel('Sequence Order')
plt.ylabel('BP Ages')
plt.title('Figure 6B.1: Zurich Sequence Plot')
plt.legend()
plt.savefig('outputs/figure6b1.png')
plt.show()

# Step 4: LR and Posteriors (Grok's estimation: P|H1=0.33, P|H0=0.067)
lr = 5
prior_odds_neutral = 1
post_odds_neutral = prior_odds_neutral * lr
post_prob_neutral = post_odds_neutral / (post_odds_neutral + 1)
print(f"\nLR: {lr}:1")
print(f"Neutral Posterior: {post_prob_neutral:.3f}")

prior_odds_skeptical = 1/100
post_odds_skeptical = prior_odds_skeptical * lr
post_prob_skeptical = post_odds_skeptical / (post_odds_skeptical + 1)
print(f"Skeptical Posterior (1:100): {post_prob_skeptical:.3f}")
