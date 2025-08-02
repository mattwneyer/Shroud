import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Zone': ['Background', 'Edge', 'Image'] * 4,
    'Marker': ['CI (inverted/AF proxy)']*3 + ['Vanillin (inverted)']*3 + ['Oxidation VOCs']*3 + ['UV Fluorescence (inverted)']*3,
    'Value': [0, 0.5, 1,   # AF=10.0 high in degraded (image)
              0, 0.5, 1,   
              0.2, 0.4, 1, 
              0, 0.5, 1]   
}

df = pd.DataFrame(data)
fig, ax = plt.subplots()
for marker in df['Marker'].unique():
    subset = df[df['Marker'] == marker]
    ax.bar(subset['Zone'], subset['Value'], label=marker, alpha=0.6)
ax.set_ylabel('Normalized Degradation')
ax.set_title('Figure 4.1: Degradation Markers')
ax.legend()
plt.show()
