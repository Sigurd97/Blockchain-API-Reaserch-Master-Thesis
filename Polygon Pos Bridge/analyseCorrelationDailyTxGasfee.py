import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load the dataset
file_path = 'MergedDataUSD.csv'
data = pd.read_csv(file_path)

# Calculate the correlation
correlation = data['GasPriceValue (USD)'].corr(data['Value'])
print(f"Correlation Coefficient: {correlation}")

# Function to format y-axis in millions
def millions(x, pos):
    return '%1.1fM' % (x * 1e-6)

formatter = FuncFormatter(millions)

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['GasPriceValue (USD)'], data['Value'], alpha=0.5, color='green')  # Set color to green
plt.title('Correlation between Daily Transactions and Gas Fees Paid (01.05.2023-01.05.2024)')
plt.xlabel('Average Gas Fee Paid(USD)')
plt.ylabel('Amount of Daily Transactions (in millions)')
plt.gca().yaxis.set_major_formatter(formatter)
plt.grid(True)

# Show the correlation coefficient on the plot
plt.text(x=max(data['GasPriceValue (USD)']) * 0.6, y=max(data['Value']) * 0.9, 
         s=f"Correlation Coefficient: {correlation:.2f}", 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
