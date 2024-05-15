import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('clean_output.csv')

# Calculate correlation
correlation = data['average fee per tx'].corr(data['txs count'])

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['average fee per tx'], data['txs count'], color='blue', marker='o')  # Using dots as markers
plt.title('Correlation between Daily Transactions and Fees Paid (01.05.2023-01.05.2024)')
plt.xlabel('Average Fee per Transaction (USD)')
plt.ylabel('Daily Transactions')
plt.grid(True)

# Display correlation on the plot using a bounding box
plt.text(x=max(data['average fee per tx']) * 0.8, y=max(data['txs count']) * 0.9,
         s=f"Correlation Coefficient: {correlation:.2f}",
         fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

# Show the plot
plt.show()
