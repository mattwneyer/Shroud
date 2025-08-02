# Replication of Version 8 Study 1: Image Superficiality and 3D Encoding
# Requirements: pip install numpy
import numpy as np

# Step 1: LRs from Evidence [Jackson et al., 1984; Heller & Adler, 1981]
lr_superficiality = 9  # P|H1 ≈0.9, P|H0 ≈0.1
lr_3d = 19  # P|H1 ≈0.95, P|H0 ≈0.05
combined_lr = lr_superficiality * lr_3d
print(f"Combined LR: {combined_lr}:1")

# Step 2: Posteriors
prior_odds_neutral = 1
post_odds_neutral = prior_odds_neutral * combined_lr
post_prob_neutral = post_odds_neutral / (post_odds_neutral + 1)
print(f"Neutral Posterior: {post_prob_neutral:.4f}")

prior_odds_skeptical = 1/100
post_odds_skeptical = prior_odds_skeptical * combined_lr
post_prob_skeptical = post_odds_skeptical / (post_odds_skeptical + 1)
print(f"Skeptical Posterior (1:100): {post_prob_skeptical:.4f}")

# Step 3: Figures 1.1C - Penetration Depth Comparisons (Text-Based, as no data for plot)
print("\nFigure 1.1C Log-Scaled Penetration Depths (μm, approximate):")
print("Shroud: 0.4")
print("Paint: 40")
print("Dye: 300")
print("Scorch: 0.5")

print("\nLinear Comparison (μm):")
print("Shroud: 0.4")
print("Paint: 10-50")
print("Dye: 200-400")
print("Scorch: 0.2-1")
