import pandas as pd

# Load the merged dataset
file_path = 'MergedDataPolygon.csv'  # Update this path
data = pd.read_csv(file_path)

# Conversion rate from USD to Ether (this needs to be updated based on current or relevant historical rates)
# Example rate: 1 USD = 0.00046 Ether (this is a hypothetical rate)
usd_to_ether_rate = 0.00046

# Convert Average Txn Fee from USD to Wei
# 1 Ether = 10^18 Wei
data['Average Txn Fee (Wei)'] = data['Average Txn Fee (USD)'] * usd_to_ether_rate * 10**18

# Optionally, drop the original USD fee column if it is no longer needed
# data.drop('Average Txn Fee (USD)', axis=1, inplace=True)

# Save the modified data to a new CSV file
output_file_path = 'UpdatedMergedDataPolygon.csv'
data.to_csv(output_file_path, index=False)

print("Data updated and saved to:", output_file_path)
