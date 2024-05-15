import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'extracted_data.csv'  # Update this to your actual file path
data = pd.read_csv(file_path)

# Convert 'DateTime (UTC)' to datetime and extract the date part
data['DateTime (UTC)'] = pd.to_datetime(data['DateTime (UTC)']).dt.date

# Group by date and calculate the total fees and the count of transactions per day
daily_data = data.groupby('DateTime (UTC)').agg(
    Total_Fees=('TxnFee(USD)', 'sum'),
    Daily_Transactions=('TxnFee(USD)', 'count')
).reset_index()

# Calculate average fee per transaction for each day
daily_data['Avg_Fee_Per_Transaction'] = daily_data['Total_Fees'] / daily_data['Daily_Transactions']

# Calculate the correlation coefficient
correlation = daily_data['Avg_Fee_Per_Transaction'].corr(daily_data['Daily_Transactions'])

# Create a scatter plot with each point represented as a dot
plt.figure(figsize=(10, 6))
plt.scatter(daily_data['Avg_Fee_Per_Transaction'], daily_data['Daily_Transactions'], alpha=0.5, color='red', marker='.')
plt.title('Correlation between Daily Transactions and Fees Paid (01.05.2023-01.05.2024)')
plt.xlabel('Average Fee Paid by Users (USD)')
plt.ylabel('Total Daily Transactions')
plt.grid(True)

# Show correlation coefficient on plot
plt.text(x=max(daily_data['Avg_Fee_Per_Transaction']) * 0.6, y=max(daily_data['Daily_Transactions']) * 0.9,
         s=f"Correlation Coefficient: {correlation:.2f}",
         fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
