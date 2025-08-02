import numpy as np

lrs_5 = [
    99,   # Blood Type AB match ([Rogers, 2005; Adler, 1999])
    20,   # Vanillin Decay ([Rogers, 2005])
    15,   # Jerusalem Carbonates ([Weaver, 1980; Whanger, 1998])
    10,   # FTIR Serum Signals ([Krantz, 2002; Garza-Valdés, 1999])
    50,   # Geometric Blood Match ([Whanger, 1998])
    10,   # Pollen Match (adjusted) ([Frei, 1982])
    0.02, # C14 Discrepancy ([Guscin, 1997; Tite et al., 1989])
    8     # Weave Match ([Flury-Lemberg, 2003])
]
combined_lr_5 = np.prod(lrs_5)
print(f"Combined LR: {combined_lr_5:.2e}:1")  # ~2.38e7:1

post_neutral_5 = combined_lr_5 / (combined_lr_5 + 1)
print(f"Neutral: {post_neutral_5}")

post_skeptical_5 = (combined_lr_5 / 1000) / (combined_lr_5 / 1000 + 1)
print(f"Skeptical (1:1000): {post_skeptical_5}")
