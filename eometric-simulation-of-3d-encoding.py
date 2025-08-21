# study_d_integrative_analysis.py
# Replicates Study D scoring matrix and LR calculation for Shroud of Turin analysis

# Scoring matrix based on Study B (literature) and Study C (2D simulation)
matrix = {
    'VUV': {
        'Superficiality': 3,  # 0.1-0.6 μm [Di Lazzaro 2010]
        '3D_Encoding': 2,    # Partial match, Inverse Square [Study C]
        'Non_Thermal': 3,    # No scorching/fluorescence [Di Lazzaro 2010]
        'Chemistry': 3,      # Oxidized cellulose [Di Lazzaro 2010]
        'Half_Tone': 3,      # ~5 mm [Di Lazzaro 2012]
        'Double_Superficiality': 0  # Single-sided [Di Lazzaro 2012]
    },
    'Maillard': {
        'Superficiality': 0,  # >0.6 μm [Rogers & Arnoldi 2003]
        '3D_Encoding': 0,    # No 3D [Rogers & Arnoldi 2003]
        'Non_Thermal': 3,    # No scorching [Rogers & Arnoldi 2003]
        'Chemistry': 0,      # Melanoidins [Rogers & Arnoldi 2003]
        'Half_Tone': 0,      # Blurry >10 mm [Rogers & Arnoldi 2003]
        'Double_Superficiality': 0  # Single-sided [Rogers & Arnoldi 2003]
    },
    'CD': {
        'Superficiality': 3,  # 0.2-0.6 μm [Fanti 2010, 2015]
        '3D_Encoding': 3,    # Full match, Inverse Square [Study C, Fanti 2010]
        'Non_Thermal': 3,    # No scorching/fluorescence [Fanti 2015]
        'Chemistry': 3,      # Oxidized cellulose [Fanti 2010]
        'Half_Tone': 3,      # ~5 mm [Fanti 2015]
        'Double_Superficiality': 3  # Both surfaces [Fanti 2010, 2015]
    },
    'Latent': {
        'Superficiality': 3,  # 0.1-0.6 μm [Di Lazzaro 2012]
        '3D_Encoding': 2,    # Partial match, Inverse Square [Study C]
        'Non_Thermal': 3,    # No scorching/fluorescence [Di Lazzaro 2012]
        'Chemistry': 3,      # Oxidized cellulose [Di Lazzaro 2012]
        'Half_Tone': 3,      # ~5 mm [Di Lazzaro 2012]
        'Double_Superficiality': 0  # Single-sided [Di Lazzaro 2012]
    }
}

# Calculate total scores
scores = {mech: sum(values.values()) for mech, values in matrix.items()}
print("Scores:", scores)

# Bayes factor for mechanisms (approximation)
# Higher score = higher probability; scale relative to Maillard
bayes_factor = (scores['CD'] + scores['Latent']) / (scores['Maillard'] + 1) * 10  # ~10^2
print("Mechanism Bayes Factor:", bayes_factor)

# LR calculation
version_8_lr = 5.26e22  # From paper
forgery_null = 10  # Study E, conservative
combined_lr = version_8_lr * bayes_factor * forgery_null
print("Combined LR:", combined_lr)

# Sensitivity analysis: Adjust scores ±1
sensitivity_results = []
for mech in matrix:
    for bench in matrix[mech]:
        original = matrix[mech][bench]
        matrix[mech][bench] = min(3, original + 1)  # +1
        scores_plus = {m: sum(v.values()) for m, v in matrix.items()}
        bf_plus = (scores_plus['CD'] + scores_plus['Latent']) / (scores_plus['Maillard'] + 1) * 10
        lr_plus = version_8_lr * bf_plus * forgery_null
        matrix[mech][bench] = max(0, original - 1)  # -1
        scores_minus = {m: sum(v.values()) for m, v in matrix.items()}
        bf_minus = (scores_minus['CD'] + scores_minus['Latent']) / (scores_minus['Maillard'] + 1) * 10
        lr_minus = version_8_lr * bf_minus * forgery_null
        matrix[mech][bench] = original  # Reset
        sensitivity_results.append((mech, bench, lr_plus, lr_minus))

# Sensitivity range
lr_range = (min(r[2] for r in sensitivity_results), max(r[3] for r in sensitivity_results))
print("LR Sensitivity Range:", lr_range)
