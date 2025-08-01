# Replication of Version 8 Study: Vanillin Degradation and Age Classification
# Requirements: pip install numpy scikit-learn matplotlib
import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Step 1: Vanillin Decay Model [Rogers, 2005]
def vanillin_residual(age, k=0.00345):
    """Model: Vanillin Residual (%) = 100 * exp(-k * age) + 0.1"""
    return 100 * np.exp(-k * age) + 0.1

# Step 2: Decay Table
ages = [0, 500, 700, 1000, 1500, 2000]  # Extended; [Rogers, 2005]
residuals = [vanillin_residual(a) for a in ages]
print("Vanillin Decay Table (Age: Residual %):")
for a, r in zip(ages, residuals):
    print(f"{a}: {r:.2f}%")

# Step 3: SVM Classification
# Training data: Medieval (6.4%, model), Ancient (0.2%); Modern (100%) omitted (trivial)
X_train = np.array([[6.4], [0.2]])  # [Medieval], [Ancient]
y_train = np.array([0, 1])  # 0=Non-Ancient, 1=Ancient
svm = SVC(probability=True, kernel='linear', random_state=42)
svm.fit(X_train, y_train)

# Predict Shroud (0.1%, Rogers 2005, p. 192)
shroud_vanillin = np.array([[0.1]])
prob_ancient = svm.predict_proba(shroud_vanillin)[0][1]
print(f"\nSVM Classification:")
print(f"Shroud Vanillin: {shroud_vanillin[0][0]}%")
print(f"Probability Ancient: {prob_ancient:.2f}")

# Robustness Test (ChatGPT suggestion: Gaussian noise ±0.05%)
n_tests = 100
noisy_probs = []
for _ in range(n_tests):
    noisy_vanillin = np.array([[0.1 + np.random.normal(0, 0.05)]])
    noisy_probs.append(svm.predict_proba(noisy_vanillin)[0][1])
print(f"Noisy SVM Mean Probability Ancient: {np.mean(noisy_probs):.2f} ± {np.std(noisy_probs):.2f}")

# Step 4: LR and Posteriors
lr = 19  # Estimation: P|H1=0.95, P|H0=0.05
print(f"\nLikelihood Ratio: {lr}:1 (P|H1=0.95 / P|H0=0.05, estimation)")
prior_odds_neutral = 1
post_odds_neutral = prior_odds_neutral * lr
post_prob_neutral = post_odds_neutral / (post_odds_neutral + 1)
print(f"Neutral Posterior: {post_prob_neutral:.4f}")

prior_odds_skeptical = 1/100
post_odds_skeptical = prior_odds_skeptical * lr
post_prob_skeptical = post_odds_skeptical / (post_odds_skeptical + 1)
print(f"Skeptical Posterior (1:100): {post_prob_skeptical:.4f}")

# Step 5: Plot Figure 2.1
ages_plot = np.linspace(0, 2000, 1000)
residuals_plot = vanillin_residual(ages_plot)
plt.plot(ages_plot, residuals_plot, label='Decay Curve')
plt.scatter([0, 700, 2000], [100.1, 6.39, 0.2], color='red', label='Benchmarks')
plt.axhline(0.1, color='green', linestyle='--', label='Shroud ~0.1%')
plt.xlabel('Age (Years)')
plt.ylabel('Vanillin Residual (%)')
plt.title('Vanillin Degradation Over Time [Rogers, 2005]')
plt.legend()
plt.show()  # Or save: plt.savefig('figure2.1.png')