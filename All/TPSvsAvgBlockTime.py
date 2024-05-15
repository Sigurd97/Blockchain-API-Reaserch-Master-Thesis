import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data setup
data = {
    "Bridge": ["Gravity Bridge", "Axelar Bridge", "Polygon PoS Bridge"],
    "TPS": [1.543, 13.961, 27.4],
    "Block Count": [13437, 14419, 38303],
    "Tx Count": [13416, 310394, 3499644],
    "Avg Block Time": [6.25, 5.97, 2.2]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate efficiency as TPS / Avg Block Time
df['Efficiency'] = df['TPS'] / df['Avg Block Time']

# Calculate standard deviations for the metrics
std_deviation = df.std()

# Printing the DataFrame with efficiency and standard deviations
print(df)
print("Standard Deviations:", std_deviation)

# Setting up the plotting environment
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plotting TPS and Avg Block Time comparison
axes[0].bar(df['Bridge'], df['TPS'], color='skyblue')
axes[0].set_title('Transactions Per Second (TPS)')
axes[0].set_ylabel('TPS')

axes[1].bar(df['Bridge'], df['Avg Block Time'], color='salmon')
axes[1].set_title('Average Block Time (Seconds)')
axes[1].set_ylabel('Seconds')

# Enhance layout
plt.tight_layout()
plt.show()
