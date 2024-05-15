import pandas as pd

# Define file paths
file_path_transactions = 'TotalDailyTransactions.csv'
file_path_gas_price = 'AvgGasPrice.csv'
file_path_fees = 'AvgTransactionFee.csv'

# Load the datasets
transactions = pd.read_csv(file_path_transactions)
gas_price = pd.read_csv(file_path_gas_price)
fees = pd.read_csv(file_path_fees)

# Standardize Date formats and ensure they are datetime objects
transactions['Date(UTC)'] = pd.to_datetime(transactions['Date(UTC)'])
gas_price['Date(UTC)'] = pd.to_datetime(gas_price['Date(UTC)'])
fees['Date(UTC)'] = pd.to_datetime(fees['Date(UTC)'])

# Perform a full outer join on 'Date(UTC)' and 'UnixTimeStamp'
merged_data = pd.merge(transactions, gas_price, on=['Date(UTC)', 'UnixTimeStamp'], how='outer')
merged_data = pd.merge(merged_data, fees, on=['Date(UTC)', 'UnixTimeStamp'], how='outer')

# Convert Value (Wei) to USD
gwei_to_usd_rate = 0.057095459119  # USD value per Gwei
merged_data['GasPriceValue (USD)'] = (merged_data['Value (Wei)'].astype(float) / 1e9) * gwei_to_usd_rate

# Calculate total average fees paid (USD)
merged_data['AvgTotalAmountFeePaid'] = merged_data['Average Txn Fee (USD)'] + merged_data['GasPriceValue (USD)']

# Remove duplicates: Keep the first occurrence of each day
merged_data.drop_duplicates(subset='Date(UTC)', keep='first', inplace=True)

# Sort by Date and reset index
merged_data.sort_values('Date(UTC)', inplace=True)
merged_data.reset_index(drop=True, inplace=True)

# Filter data to only include dates from 2023-05-01 to 2024-05-01
start_date = pd.Timestamp('2023-05-01')
end_date = pd.Timestamp('2024-05-01')
merged_data = merged_data[(merged_data['Date(UTC)'] >= start_date) & (merged_data['Date(UTC)'] <= end_date)]

# Save the merged and filtered data to a new CSV file
output_file_path = 'MergedDataUSD.csv'
merged_data.to_csv(output_file_path, index=False)