import pandas as pd
import ast

# Load the CSV file
file_path = 'output.csv'
data = pd.read_csv(file_path)

# The 'rows' field contains the data we need in a string format resembling a list of lists
# Assuming the data is in the 'Average Fee per TX' column at a specific index
rows_data = data.loc[4, 'Average Fee per TX']

# Parse the string representation of the list using ast.literal_eval to convert it into an actual list of lists
rows_data_list = ast.literal_eval(rows_data)

# Create a DataFrame from the extracted list
columns = ['date', 'average fee per tx', 'txs count', '__row_index']
processed_data = pd.DataFrame(rows_data_list, columns=columns)

# Save the processed DataFrame to a new CSV file
output_file_path = 'clean_output.csv'
processed_data.to_csv(output_file_path, index=False)

# Optionally, you can print a confirmation that the file was saved
print(f'File saved to {output_file_path}')
