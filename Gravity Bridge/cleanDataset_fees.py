import pandas as pd

def extract_txn_fee_and_date(file_path, output_file_path):
    # Read the file using a context manager
    with open(file_path, 'r') as file:
        # Read the header and determine the indexes
        header = file.readline().strip().split(',')
        txn_fee_usd_index = header.index('""TxnFee(USD)""')
        date_index = header.index('""DateTime (UTC)""')  # Adjust if the actual header name is different

        # Extract "TxnFee(USD)" and "DateTime (UTC)" values
        data_values = []
        for line in file:
            values = line.strip().split(',')
            # Ensure the indexes are within the range of columns available in this row
            if len(values) > txn_fee_usd_index and len(values) > date_index:
                txn_fee_usd = values[txn_fee_usd_index].replace('"', '')
                date_value = values[date_index].replace('"', '')
                data_values.append([date_value, txn_fee_usd])

    # Create a DataFrame from the extracted values
    df = pd.DataFrame(data_values, columns=['DateTime (UTC)', 'TxnFee(USD)'])

    # Save the DataFrame to a new CSV file
    df.to_csv(output_file_path, index=False)

# Usage
file_path = 'GravityBridge1year.csv'  # Change this to the path of your CSV file
output_file_path = 'extracted_data.csv'  # Desired output file path
extract_txn_fee_and_date(file_path, output_file_path)
