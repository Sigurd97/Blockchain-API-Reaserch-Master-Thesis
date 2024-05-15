import csv
from flipside import Flipside

# Initialize Flipside with your API Key and API URL
api_key = "6ccb796f-c342-4ed1-980d-d8f66360b053"
api_url = "https://api-v2.flipsidecrypto.xyz"
flipside = Flipside(api_key, api_url)

sql = """
SELECT block_timestamp::date AS "Date", AVG(fee)/pow(10,6) AS "Average Fee per TX", COUNT(DISTINCT tx_id) AS "TXs Count"
FROM axelar.core.fact_transactions
WHERE block_timestamp::date >= '2023-05-01' AND block_timestamp::date <= '2024-05-01'
AND fee_denom='uaxl' AND tx_succeeded='true'
GROUP BY 1
ORDER BY 1
"""

try:
    query_result_set = flipside.query(sql)
    print("Query Result Type:", type(query_result_set))

    # Assuming the result set is iterable and contains tuples
    data = list(query_result_set)

    # Write to CSV
    if data:
        headers = ["Date", "Average Fee per TX", "TXs Count"]  # Specify headers based on your SQL SELECT
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)  # Write headers
            writer.writerows(data)  # Write the data rows
        print("Data has been written to 'output.csv'")
    else:
        print("No data to write to CSV.")
except Exception as e:
    print(f"An error occurred: {e}")
