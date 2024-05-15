import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import json

# Load JSON data
with open('test.json', 'r') as file:
    json_data = json.load(file)

# Normalize the data to create a DataFrame
if isinstance(json_data, dict):
    key = next(iter(json_data))  # Adjust if the data is nested under a specific key
    data = pd.json_normalize(json_data[key])
else:
    data = pd.json_normalize(json_data)

# Calculate the average fee per transaction
data['avg_fee_per_tx'] = data['fee'] / data['users']


# Calculate the correlation coefficient
correlation = pearsonr(data['users'], data['avg_fee_per_tx'])[0]

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['avg_fee_per_tx'], data['users'], alpha=0.5, color='blue', marker='o')  # Use blue dots
plt.title('Correlation between Daily Transactions and Fees Paid (01.05.2023-01.05.2024)')
plt.xlabel('Average Fee Paid by Users (USD)')
plt.ylabel('Number of Transactions')
plt.text(x=max(data['avg_fee_per_tx']) * 0.6, y=max(data['users']) * 0.9, 
         s=f"Correlation Coefficient: {correlation:.2f}",
         fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
plt.grid(True)
plt.show()
